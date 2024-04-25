from langchain.serpapi import SerpAPIWrapper
from langchain.agents import tool


@tool
def get_profile_url(text: str) -> str:
    """
    Searches for Linkedin Profile Page.
    """
    # search = SerpAPIWrapper()
    # res = search.run(f"{text}")
    # return res
    return "Andrew ng is a remarkable person their twitter link is 'https://www.linkedin.com/in/andrewyng/'"
