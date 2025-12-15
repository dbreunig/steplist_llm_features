from tavily import TavilyClient
from typing import Literal
from dotenv import dotenv_values

# Load environment variables from .env file
config = dotenv_values(".env")

# Search Tool
tavily_client = TavilyClient(api_key=config["TAVILY_API_KEY"])

def internet_search(
	query: str, 
	max_results: int = 5, 
	topic: Literal["general", "news", "finance"] = "general",
	include_raw_content: bool = False,
): 
	"""Run a web search""" 
	print(f"Running internet search for query: {query}")
	return tavily_client.search(
		query, max_results=max_results, 
		include_raw_content=include_raw_content, 
		topic=topic, # type: ignore
	)

def read_webpage(url: str) -> dict:
	"""Read the content of a URL."""
	print(f"Reading URL: {url}")
	response = tavily_client.extract(url)
	return response