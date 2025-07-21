import streamlit as st
from graph_builder import build_graph

st.set_page_config(page_title="🧠 Research Agent", layout="centered")
st.title("🧠 LangGraph Research Agent")

topic = st.text_input("Enter a research topic:", placeholder="e.g. Cybersecurity in fintech")

if st.button("Run Research"):
    if not topic:
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Running agent..."):
            graph = build_graph()
            final_state = graph.invoke({"topic": topic})

        st.success("✅ Research complete!")
        st.subheader("Executive Summary")
        st.write(final_state["summary"])

        st.subheader("Findings")
        for f in final_state["findings"]:
            st.markdown(f"**{f['question']}**\n\n{f['answer']}\n")

        st.subheader("Sources")
        for s in set([url for r in final_state["search_results"] for url in r["urls"]]):
            st.markdown(f"- {s}")

        st.download_button(
            "📄 Download Report",
            final_state["report"],
            file_name="research_report.md",
            mime="text/markdown"
        )
