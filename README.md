# 🔍 Agentic Research Engine

This project demonstrates a powerful Agentic Research Engine built using the LangChain and LangGraph frameworks. It showcases how to orchestrate specialized AI agents to perform complex, multi-step tasks like web research and information synthesis, offering a robust and transparent approach to automated knowledge gathering.

# 🌟 Project Overview

This project is a practical demonstration of building and managing advanced AI agent workflows. It focuses on breaking down complex research tasks into manageable steps handled by different specialized agents, providing a foundation for more sophisticated AI applications.


# ✨ Key Features
Multi-Agent Architecture: Implements a system with distinct AI agents (e.g., a "Researcher" and a "Writer") that collaborate to achieve a common goal.

1.Automated Web Research: Utilizes tools to perform targeted web searches and gather relevant information based on user queries.

2.Information Synthesis: Agents process raw research data to provide concise summaries and structured reports.

3.Workflow Orchestration with LangGraph: Leverages LangGraph to define and manage the stateful flow between different agents, ensuring controlled and reliable execution.

4.Debugging & Observability: Integrates LangSmith for real-time tracing and monitoring of agent actions and tool calls, aiding in debugging and understanding agent reasoning.

5.Human-in-the-Loop Capabilities: Demonstrates how to design workflows where human intervention can occur at specific points for feedback or critical decision-making.

# 🧠 How It Works
The core of this project is a graph-based state machine defined using LangGraph. The workflow typically involves:

Initial Query: A user provides a research topic.

Researcher Agent: An agent, often powered by an LLM, uses a web search tool (e.g., Tavily) to gather information related to the query.

Writer Agent (or Analyst/Supervisor): The gathered information is then passed to another agent responsible for analyzing, synthesizing, and summarizing the findings into a structured report.

Dynamic Routing: LangGraph's state management enables dynamic transitions between agents based on the current state and task completion.

Observability: Throughout this process, LangSmith captures every step, tool call, and LLM interaction, providing a detailed trace for debugging and analysis.

# 🛠️ Setup and Installation
To get this project up and running, follow these steps:

Create a virtual environment:

python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set up API Keys:
Rename sample.env (or create a new .env file) to .env in the root of your project directory and add your API keys. You will need:

GROQ_API_KEY (for LLM access)

TAVILY_API_KEY (for web search tool)

LANGCHAIN_API_KEY (for LangSmith tracing)

Your .env file should look like this:

GROQ_API_KEY="your_groq_api_key_here"
TAVILY_API_KEY="your_tavily_api_key_here"
LANGCHAIN_API_KEY="your_langchain_api_key_here"

Also set LANGSMITH_TRACING="true" and LANGSMITH_PROJECT="TestProject" as environment variables or directly in your Python files (as seen in debugging.ipynb and agent.py).

🚀 Usage
The project is primarily demonstrated through Jupyter notebooks, each showcasing a different aspect of agentic development:

multiaiagent.ipynb: Explores the basic multi-agent architecture for research and summarization.

basicchatbot.ipynb: Demonstrates the fundamentals of building a conversational chatbot with LangGraph.

debugging.ipynb: Focuses on using LangSmith for tracing and debugging agent workflows.

humaninloop.ipynb: Illustrates how to integrate human intervention into an agent's process.

agent.py: Contains modular agent definitions and graph construction logic.

To run a notebook, execute:

jupyter notebook

Then open the desired .ipynb file and run the cells.

💡 Future Enhancements
Streamlit Web UI: Develop a user-friendly Streamlit application to allow interactive queries and display agent outputs.

Advanced Tooling: Integrate more diverse tools (e.g., YouTube transcript fetcher, data analysis tools, image generation).

Self-Healing Capabilities: Implement robust error handling, retry mechanisms, and dynamic re-planning within the graph to enable the agents to autonomously recover from failures.

Persistent Memory: Explore different memory solutions beyond in-memory for long-term context retention across sessions.

Deployment: Package the application for deployment to cloud platforms.

