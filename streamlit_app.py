# Chatbot dedicado à vítima de violência doméstica 
# Adaptado de https://blog.streamlit.io/build-a-chatbot-with-custom-data-sources-powered-by-llamaindex/#what-is-llamaindex
# por José Eduardo de Souza Pimentel
# para uso da Promotoria de Justiça de Piracicaba sob supervisão de Promotor de Justiça ou funcionário

import streamlit as st
import openai
from llama_index.llms.openai import OpenAI
try:
  from llama_index import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader
except ImportError:
  from llama_index.core import VectorStoreIndex, ServiceContext, Document, SimpleDirectoryReader

st.set_page_config(page_title="Pergunte-me qualquer coisa sobre violência domestica...", page_icon="🏠", layout="centered", initial_sidebar_state="auto", menu_items=None)
openai.api_key = st.secrets["OpenAI_key"]
st.title("Promotoria de Justiça de Piracicaba/SP - Projeto Experimental")
st.header("Pergunte-me qualquer coisa sobre violência doméstica... 🏠")
st.info("Baseado em cartilhas publicadas por órgãos oficiais e de acesso livre na web. Use como simples referência. SUJEITO A ERROS. Não dispensa a consulta ao Promotor e seus auxiliares. Não tome atitudes fundadas exclusivamente nessas respostas.")
         
if "messages" not in st.session_state.keys(): # Initialize the chat messages history
    st.session_state.messages = [
        {"role": "assistant", "content": "Pergunte-me qualquer coisa sobre violência domestica..."}
    ]

@st.cache_resource(show_spinner=False)
def load_data():
    with st.spinner(text="Aprendendo com o conteúdo novo... Aguarde alguns minutos..."):
        reader = SimpleDirectoryReader(input_dir="./data", recursive=True)
        docs = reader.load_data()
        # llm = OpenAI(model="gpt-3.5-turbo", temperature=0.5, system_prompt="You are an expert o$
        # index = VectorStoreIndex.from_documents(docs)
        system_prompt = """Você é um promotor de justiça especializado em violência doméstica. Seu trabalho é responder a questões técnicas, com empatia. Suas respostas devem ser baseada nos dados fornecidos. Não responsa nada fora dos dados. Não responda nada fora do assunto violência doméstica. Responda em português. Não alucine."""
        service_context = ServiceContext.from_defaults(llm=OpenAI(model="gpt-3.5-turbo-0125", temperature=0.9, system_prompt=system_prompt))
        index = VectorStoreIndex.from_documents(docs, service_context=service_context)
        return index

index = load_data()

if "chat_engine" not in st.session_state.keys(): # Initialize the chat engine
        st.session_state.chat_engine = index.as_chat_engine(chat_mode="condense_question", verbose=True)

if prompt := st.chat_input("Sua pergunta?"): # Prompt for user input and save to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})

for message in st.session_state.messages: # Display the prior chat messages
    with st.chat_message(message["role"]):
        st.write(message["content"])

# If last message is not from assistant, generate a new response
if st.session_state.messages[-1]["role"] != "assistant":
    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = st.session_state.chat_engine.chat(prompt)
            st.write(response.response)
            message = {"role": "assistant", "content": response.response}
            st.session_state.messages.append(message) # Add response to message history