import streamlit as st
from openai import OpenAI
from RagClient import RagClient

rag_client = RagClient()

st.title("💬 Freire - Nerd Chatbot")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "Me pergunte algo sobre os documentos que me enviou!"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = rag_client.askChat(prompt)
    msg = response.response
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)