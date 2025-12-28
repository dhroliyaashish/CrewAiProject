from crewai import Task
from tools import yt_tool
from agents import blogresearcher, blogwriter

# Task for researching blog content
research_blog_task = Task(
    description="Research and gather relevant information for blog posts on various {topics}.",
    expected_output="A comprehensive research report with key insights and sources.",
    agent=blogresearcher,
    tools= [yt_tool])

# Task for writing blog content
write_blog_task = Task(
    description="Create engaging and well-structured blog posts based on researched information about {topics}.",
    expected_output="A well-written blog post with a clear narrative and structure.",
    agent=blogwriter,
    tools= [yt_tool]
)   