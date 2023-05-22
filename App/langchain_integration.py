import os
from langchain.llms import OpenAI
from langchain.prompts import PromptTemplate
import openai
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv('OPENAI_API_KEY')

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


'''
    generate a prompt that summarizes the generated job listing into a description - 
'''


def summarize_job_listing(job_listing):
    prompt = PromptTemplate(
        input_variables=["job_listing"],
        template="Summarize the following job listing in the following format: '[company name]"
                 " - [technologies mentioned]' - disregard everything else other than the format."
                 "here's the job listing: {job_listing}"

    )
    formatted_prompt = prompt.format(
        job_listing=job_listing
    )
    return llm(formatted_prompt)


def filter_tech_stack(tech_stack):
    prompt = PromptTemplate(
        input_variables=["tech_stack"],
        template="Filter the following text extracting only the technologies mentioned in the text."
                 " If you can only detect technologies, leave it as is. Here's the text: {tech_stack}"

    )
    formatted_prompt = prompt.format(
        tech_stack=tech_stack
    )
    return llm(formatted_prompt)
