import os
from langchain_groq import ChatGroq
from langchain.schema import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, END
from tavily import TavilyClient
from jinja2 import Template
from dotenv import load_dotenv

MAX_QUERY_LENGTH = 400

def summarize_question(q):
    # If it fits, return it directly
    if len(q) <= MAX_QUERY_LENGTH:
        return q

    # Otherwise, summarize using LLM
    prompt = f"Summarize the following research question in under {MAX_QUERY_LENGTH} characters while keeping its original meaning:\n\n{q}"
    return groq_llm.invoke([HumanMessage(content=prompt)]).content.strip()



load_dotenv()  # Load from .env file

groq_llm = ChatGroq(api_key=os.getenv("GROQ_API_KEY"), model="llama-3.3-70b-versatile")
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def plan_node(state: dict) -> dict:
    topic = state["topic"]
    msgs = [
        SystemMessage(content="You are a research assistant meant to answer complex questions with high levels of detail and accuracy. You must prioritize the most recent data and have full access to the internet."),
        HumanMessage(content=f"Break this topic into 5 insightful research questions:\n\n{topic}")
    ]
    output = groq_llm.invoke(msgs).content
    state["sub_questions"] = [line.strip(" -•\n") for line in output.strip().split("\n") if line.strip()]
    return state

def search_node(state: dict) -> dict:
    results = []
    for q in state["sub_questions"]:
        try:
            short_q = summarize_question(q)
            resp = tavily.search(short_q, search_depth="advanced", include_answers=True)
            urls = [r["url"] for r in resp["results"][:3]]
            results.append({"question": q, "urls": urls})
        except Exception as e:
            print(f"Search failed for question: {q[:100]}... Error: {e}")
            results.append({"question": q, "urls": []})

    state["search_results"] = results
    state["retry_search"] = any(len(group["urls"]) == 0 for group in results)
    return state



def retrieve_node(state: dict) -> dict:
    collected = []
    for item in state["search_results"]:
        text = ""
        for url in item["urls"]:
            try:
                text += f"\n[From {url}]\n"
                content = tavily.extract_content(url).get("content", "")
                text += content
            except:
                continue
        collected.append({"question": item["question"], "content": text})
    state["retrieved"] = collected
    return state

def synthesize_node(state: dict) -> dict:
    findings = []
    for item in state["retrieved"]:
        q = item["question"]
        context = item["content"]
        prompt = f"Using the following text, answer the question:\n\nQuestion: {q}\n\nText:\n{context}"
        output = groq_llm.invoke([HumanMessage(content=prompt)]).content
        findings.append({"question": q, "answer": output})
    state["findings"] = findings
    return state

def summary_node(state: dict) -> dict:
    answers = "\n".join([f["answer"] for f in state["findings"]])
    prompt = f"Summarize the key findings in 3 sentences:\n\n{answers}"
    summary = groq_llm.invoke([HumanMessage(content=prompt)]).content
    state["summary"] = summary
    return state

def report_node(state: dict) -> dict:
    with open("report_template.md") as f:
        template = Template(f.read())

    sources = [url for group in state["search_results"] for url in group["urls"]]
    report = template.render(
        topic=state["topic"],
        summary=state["summary"],
        findings=state["findings"],
        sources=sources
    )

    state["report"] = report
    return state

def build_graph():
    builder = StateGraph(dict)
    builder.add_node("PLAN", plan_node)
    builder.add_node("SEARCH", search_node)
    builder.add_node("RETRIEVE", retrieve_node)
    builder.add_node("SYNTHESIZE", synthesize_node)
    builder.add_node("SUMMARY", summary_node)
    builder.add_node("REPORT", report_node)

    builder.set_entry_point("PLAN")
    builder.add_edge("PLAN", "SEARCH")
    builder.add_conditional_edges("SEARCH", lambda s: "SEARCH" if s["retry_search"] else "RETRIEVE")
    builder.add_edge("RETRIEVE", "SYNTHESIZE")
    builder.add_edge("SYNTHESIZE", "SUMMARY")
    builder.add_edge("SUMMARY", "REPORT")
    builder.add_edge("REPORT", END)

    return builder.compile()
