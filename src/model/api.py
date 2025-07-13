import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq        

# Load environment variable
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")   

llm = ChatGroq(
    model_name="llama3-70b-8192",           
    groq_api_key=GROQ_API_KEY,
    temperature=0.2,
    max_tokens=1000,
)

prompt = PromptTemplate(
    input_variables=["text"],
    template=(
        "Extract only relevant technical and soft skills from this text. "
        "Return them as a comma-separated list.\n\n{text}"
    )
)

def extract_skills_with_langchain(text: str):
    chain = prompt | llm
    response = chain.invoke({"text": text})
    reply = response.content.strip()
    skills = [s.strip() for s in reply.split(',') if s.strip()]
    return skills
