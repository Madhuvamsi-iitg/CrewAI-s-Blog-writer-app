import streamlit as st
from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Streamlit UI setup
st.set_page_config(page_title="Agentic AI Blog Writer", layout="centered")
st.title("🧠 Agentic AI Blog Writer")
st.write("Create well-researched blog posts using intelligent agents powered by LLMs!")

# Sidebar inputs
st.sidebar.header("🛠️ Configuration")

# Topic input
topic = st.sidebar.text_input("📌 Enter a topic:", "Medical industry using Generative AI")

# LLM temperature selection
temperature = st.sidebar.selectbox(
    "🔥 Choose LLM Temperature",
    options=[0.0, 0.5, 0.7, 1.0],
    index=2,
    help="Higher temperature = more creativity, Lower = more accuracy"
)

# Generate button
generate = st.sidebar.button("🚀 Generate Article")

# Main app logic
if generate:
    with st.spinner("⏳ Working hard to craft your article..."):

        # Tool setup
        llm = LLM(model="gpt-4o-2024-08-06", temperature=temperature)
        search_tool = SerperDevTool(n=10)

        # Agents
        senior_research_analyst = Agent(
            role="Senior Research Analyst",
            goal=f"research, analyze and synthesize comprehensive information on {topic} from reliable web sources",
            backstory="""
            You are an expert resarch analyst with advanced web search skills.
            You excel at finding and synthesizing information from multiple sources.
            You are skilled at analyzing data and extracting key insights.
            You are able to identify trends and patterns in the data you collect.
            You provide well - organized research briefs with proper citations and source verification.
            Your analysis includes both raw data and interpreted insights, making complex 
            information accessible to a wide audience.
            """,   
            allow_delegation=False,
            verbose=True,
            tools=[search_tool],
            llm=llm
        )

        content_writer = Agent(
            role="Content Writer",
            goal="Transform research findings into a well-structured, engaging blog post",
            backstory="""
            You are an expert content writer with advanced writing skills.
            You excel at creating engaging and informative content.
            You are skilled at structuring articles and ensuring clarity and coherence.
            You are able to adapt your writing style to suit different audiences.
            Your articles are well - researched, properly cited, and free of plagiarism.
            """,
            allow_delegation=False,
            verbose=True,
            llm=llm
        )

        # Tasks
        research_task = Task(
            description=f"""
                Conduct comprehensive research on {topic} including:
                - recent developments and news
                - key industry trends and innovations
                - expert opinions and analyses
                - statistical data and market insights
                Evaluate source credibility and fact-check all information.
                Organize findings into a structured research brief.
                Provide proper citations and source verification.
            """,
            expected_output="""
                A detailed research report including:
                - recent developments and news
                - key trends and innovations
                - expert opinions
                - data and market insights
                - sources with proper citations
            """,
            agent=senior_research_analyst
        )

        writing_task = Task(
            description="""
                Transform the research into a blog post:
                - Write an engaging introduction
                - Structure content clearly
                - Maintain clarity and accuracy
                - Cite sources in [Source: URL] format
                - Add compelling conclusion
            """,
            expected_output="""
                A well-structured blog post:
                - Engaging intro
                - Key sections
                - Clear formatting and bullet points
                - Proper source citations
            """,
            agent=content_writer
        )

        # Crew setup and kickoff
        crew = Crew(
            name="Generative AI Research Crew",
            agents=[senior_research_analyst, content_writer],
            tasks=[research_task, writing_task],
            verbose=True,
        )

        result = crew.kickoff(inputs={"topic": topic})

        # Show result
        st.success("✅ Article generated successfully!")
        st.subheader("📄 Generated Blog Post")
        st.text_area("Blog Content", value=str(result), height=500)

        # Download button
        st.download_button(
            label="📥 Download as .txt",
            data=str(result),
            file_name=f"{topic.replace(' ', '_')}_blog_post.txt",
            mime="text/plain"
        )

