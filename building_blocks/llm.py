from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

def batch():
    chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768", groq_api_key=os.getenv("GROQ_API_KEY"))

    system = "Eres un asistente amable que llama a prospectos"
    human = "{text}"
    prompt = ChatPromptTemplate.from_messages([("system", system), ("human", human)])

    chain = prompt | chat
    print(chain.invoke({"text": "Agenda una sesión demo para el prospecto."}))

# Streaming
def streaming():
    chat = ChatGroq(temperature=0, model_name="llama2-70b-4096",groq_api_key=os.getenv("GROQ_API_KEY"))
    prompt = ChatPromptTemplate.from_messages([("human", "Eres un agente de ventas sobre {topic}, tu respuesta debe ser de hasta 15 caracteres")])
    chain = prompt | chat
    for chunk in chain.stream({"topic": "QuestionPro, software de encuestas"}):
        print(chunk.content, end="", flush=True)

# batch()
streaming()