import os
from langchain_openai import ChatOpenAI
from backend.tools import skills
tools = [skills.getCompanyPolicy, skills.requestTimeOff, skills.getRemainingVacationDays, skills.getHolidaysByCountry]
MODEL = os.getenv('MODEL')
llm = ChatOpenAI(model=MODEL)
llm_with_tools = llm.bind_tools(tools)