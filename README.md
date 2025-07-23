# langgraph_research_assistant

🧠 Streamlit Project  
📄 AI Research Agent using Groq + LangGraph

📌 Project Overview

Welcome to my AI Research Agent! This web app allows you to input any research topic and automatically:

✅ Plans the research  
✅ Gathers key insights from the web  
✅ Synthesizes the information using an LLM  
✅ Summarizes findings into an executive brief  
✅ *Provides citations and source URLs*  
✅ Exports everything into a downloadable Markdown report

It’s powered by Groq’s blazing-fast LLaMA3-70B model, built using LangGraph, and wrapped in an interactive Streamlit UI — perfect for students, researchers, or anyone curious!

---

🚀 How I Built & Ran the App (Step-by-Step)

Here’s the exact process I followed to bring this research assistant to life 👇

1. Created a project folder: ai_research_agent

2. Added the main code files:
    - app.py: Streamlit frontend
    - graph_builder.py: LangGraph nodes for planning, searching, and summarizing

3. Created a .env file to store my API keys:
   GROQ_API_KEY=your_groq_api_key  
   TAVILY_API_KEY=your_tavily_api_key

4. Created a requirements.txt with these dependencies:
   streamlit  
   langchain  
   langgraph  
   langchain-groq  
   tavily-python  
   jinja2  
   python-dotenv

5. Installed everything using:
   pip install -r requirements.txt

6. Launched the Streamlit app:
   streamlit run app.py

7. Opened it in my browser:
   http://localhost:8501

---

🔁 GitHub Upload Steps

1. Created a new repository on GitHub
2. Opened terminal in my project folder
3. Ran:
   git init  
   git add .  
   git commit -m "Add AI Research Agent with LangGraph and Groq"  
   git remote add origin https://github.com/your-username/your-repo-name.git  
   git push -u origin main

Replace your-username and your-repo-name with your actual GitHub details.

---

📁 Project Folder Structure

📦 ai_research_agent  
┣ 📄 app.py → Streamlit UI + Graph Runner  
┣ 📄 graph_builder.py → LangGraph nodes: PLAN → SEARCH → RETRIEVE → SYNTHESIZE → SUMMARY → REPORT  
┣ 📄 report_template.md → Jinja2 template for final report  
┣ 📄 requirements.txt → Python dependencies  
┣ 📄 .env → API keys (excluded from Git)  
┣ 📄 README.md → You’re reading it!  
┗ 📄 LICENSE → MIT License

---

💡 What the App Can Do

✔ Accepts any research topic  
✔ Breaks it into sub-questions  
✔ Uses Tavily API to perform advanced web search  
✔ Extracts and retrieves top source content  
✔ Synthesizes answers via Groq LLaMA3-70B  
✔ *Displays source citations under every answer*  
✔ Summarizes all findings and generates a full Markdown report  
✔ Allows the report to be downloaded in one click

---

📚 Citation Support

The app collects the top 3 URLs for each sub-question from Tavily's search engine. These source URLs are:

- Included under the "Sources" section in the Streamlit app
- Added directly into the generated Markdown report for proper citation
- Help trace each insight back to the original source

✅ This ensures transparency and supports academic/research use cases.

---

✨ Tech Stack Used

- *Streamlit* — For the interactive UI
- *Groq (LLaMA3-70B)* — LLM for question generation and synthesis
- *LangGraph* — Node-based workflow orchestration
- *LangChain* — Agent tools + memory
- *Tavily API* — For web search and content extraction
- *Jinja2* — For Markdown templating
- *Python-dotenv* — For secure key management

---

👩‍💻 Created By

*Raama Katragadda*
*Ushmitha Annapaneni*  
*Vedasri Narla*
If you found this project helpful, feel free to star ⭐ or fork 🍴 it on GitHub!

---

📄 License

MIT License — Free to use, modify, and distribute.
