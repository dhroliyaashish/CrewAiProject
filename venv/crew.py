from crewai import Process, crew
from agents import blogresearcher, blogwriter
from tasks import research_blog_task, write_blog_task
from tools import yt_tool

# Initialize Crew with agents and tasks
my_crew = crew.Crew(
    name="Content Creation Crew",
    agents=[blogresearcher, blogwriter],
    tasks=[research_blog_task, write_blog_task],    
    tools=[yt_tool],
    verbose=True,   
    memory=True,
    process=Process.sequential,
    cache=True,
    share_crew=True)
    
result = my_crew.kickoff(inputs={"topics":'Langchain'})
print(result)



