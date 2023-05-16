import os

import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate

llm = OpenAI(temperature=0.9)


def generate_job_listing(job_position, tech_stack, company_name, company_values):
    prompt = PromptTemplate(
        input_variables=["job_position", "company_name", "tech_stack", "company_values"],
        template="You are an expert job listing creator.Generate a job listing for a {job_position}"
                 " at {company_name} using {tech_stack} and following company values: {company_values}."

    )
    formatted_prompt = prompt.format(
        job_position=job_position,
        tech_stack=tech_stack,
        company_name=company_name,
        company_values=company_values
    )
    return llm(formatted_prompt)
