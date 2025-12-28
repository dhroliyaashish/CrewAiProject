from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv

load_dotenv()
#Content researcher agent

blogresearcher = Agent(
 role = "Blog Researcher",
 goal = "Research and gather relevant information for blog posts on various {topics}.",
 name = "blog_researcher",
verbose = True,
memory =True,
backstory = "An experienced researcher skilled in finding credible sources and compiling information efficiently.",
tool=[yt_tool],
allow_delegration = True
)

#Content writer agent
blogwriter = Agent(
 role = "Blog Writer",
 goal = "Create engaging and well-structured blog posts based on researched information about {topics}.",
 name = "blog_writer",
verbose = True,
memory =True,
backstory = "An experienced writer skilled in crafting compelling narratives and structuring content effectively.",
tool=[yt_tool],
allow_delegration = False
)