from pydantic import BaseModel

from src.agents.prompts import SYSTEM_PROMPT

from langchain_community.tools.ddg_search import DuckDuckGoSearchRun
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_classic.agents import initialize_agent, AgentType


class ResultModel(BaseModel):
    result: str


def run_agent_gemini(api_key: str, model: str, topic: str):
    web_search = DuckDuckGoSearchRun()

    llm = ChatGoogleGenerativeAI(model=model, api_key=api_key)

    agent = initialize_agent(
        tools=[web_search],
        llm=llm,
        agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
        output_parser=PydanticOutputParser(pydantic_object=ResultModel),
        handle_parsing_errors=True,
    )

    prompt = SYSTEM_PROMPT.format(topic=topic)

    result = agent.invoke({"input": prompt})

    return result["output"]
