import os
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(temperature=0.4, model="gpt-4", openai_api_key=os.getenv(openai.api_key))

def generate_zeugnis(user_data: dict) -> str:
    with open("prompts/zeugnis_template.txt", "r", encoding="utf-8") as f:
        template = f.read()

    prompt = PromptTemplate.from_template(template)
    prompt_filled = prompt.format(**user_data)

    response = llm.predict(prompt_filled)
    return response
