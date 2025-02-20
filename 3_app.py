import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage
from _3_ai_handler import generate_message_response

load_dotenv()

st.title("Generative AI app")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

if "messages" not in st.session_state:
	st.session_state.messages = []


messages = st.session_state.messages

for msg in messages:
	with st.chat_message(msg.type):
		st.markdown(msg.content)

prompt = st.chat_input("Ask your question")


if prompt:
	with st.chat_message("human"):
		st.markdown(prompt)
	
	messages.append(HumanMessage(content=prompt))

	[ans, updatesMessages] = generate_message_response(prompt, messages)
	
	
	with st.chat_message("assistant"):
		st.markdown(updatesMessages[-1].content)
		st.session_state.messages = updatesMessages
