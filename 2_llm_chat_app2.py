import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

st.title("Generative AI app")

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

if "messages" not in st.session_state:
	st.session_state.messages = []

messages = st.session_state.messages

for m in messages:
	with st.chat_message(m["role"]):
		st.markdown(m["content"])

prompt = st.chat_input("Ask your question")


if prompt:
	with st.chat_message("user"):
		st.markdown(prompt)
	
	messages.append({"role": "user", "content": prompt})

	chain = llm | StrOutputParser()
	ai_ans = chain.stream(prompt)
	
	with st.chat_message("assistant"):
		st.markdown(ai_ans)
		messages.append({"role": "assistant", "content": ai_ans})