from crewai import Agent, Task, Crew, LLM
from crewai_tools import SerperDevTool

from dotenv import load_dotenv
load_dotenv()

topic = "Medial industry using Generative AI"

#tool 1
llm = LLM(model="gpt-4")

#tool 2
search_tool = SerperDevTool(n=10)

#Agent 1
senior_research_analyst = Agent(
    role = "Senior Research Analyst",
    goal = "research , analyze and synthesize comprehensive  information on {topic} from reliable web sources",
    backstory="""
    You are an expert resarch analyst with advanced web search skills.
    You excel at finding and synthesizing information from multiple sources.
    You are skilled at analyzing data and extracting key insights.
    You are able to identify trends and patterns in the data you collect.
    You provide well - organized research briefs with proper citations and source verification.
    Your analysis includes both raw data and interpreted insights, making complex 
    information accessible to a wide audience.
    """,

    allow_delegation= False,
    verbose= True,
    tools = [search_tool],
    llm = llm
)

#Agent 2 content writer
content_writer = Agent(
    role = "Content Writer",
    goal = "Transform research findings into a well-structured, engaging blog posts while maintaining accuracy and clarity",
    backstory="""
    You are an expert content writer with advanced writing skills.
    You excel at creating engaging and informative content.
    You are skilled at structuring articles and ensuring clarity and coherence.
    You are able to adapt your writing style to suit different audiences.
    Your articles are well - researched, properly cited, and free of plagiarism.
    """,

    allow_delegation= False,
    verbose= True,
    llm = llm
)


#define tasks
research_task = Task(
    description= (""""
                  1. conduct comprehensive research on {topic} including:
                     - recent developments and news
                     - key industry trends and innovations
                     - expert opinions and analyses
                     - statistical data and market insights
                  2. evaluate source credibility and fct-check all information
                  3. organize findings into a structured research brief
                  4. provide proper citations and source verification
                
    """),
    expected_output= """
                  A detailed research report containing:
                  - a summary of recent developments and news
                  - comprehensive analyisis of current trends and innovations
                  - expert opinions and analyses
                  - statistical data and market insights
                  - a list of credible sources with proper citations
                  - clear categorizarion of main themes and patterns
                  please format with clear sections and bullet points for easy readability
                  """,
    agent= senior_research_analyst
)

writing_task = Task(
    description= (""""
                  1. transform the research findings into a well-structured blog post
                  2. ensure the content is engaging, informative, and easy to read
                  3. maintain accuracy and clarity throughout the article
                  4. adapt the writing style to suit a general audience
                  5. include proper citations and references to the research sources
                  6. Preserves all source citations in [Source: URL] format
                  7. Attention-grabing intrduction with well structured body sections and clear headings and compelling conclusion
                
    """),
    expected_output= """
                  A well-structured blog post containing:
                  - an engaging introduction to the topic
                  - clear sections addressing key points from the research
                  - a conclusion summarizing the main insights and implications
                  - proper citations and references to the research sources
                  please format with clear sections and bullet points for easy readability
                  """,
    agent= content_writer
)

crew = Crew(
    name="Generative AI Research Crew",
    agents=[senior_research_analyst, content_writer],
    tasks=[research_task, writing_task],
    verbose=True,
)

result = crew.kickoff(inputs={"topic": topic})
print(result)