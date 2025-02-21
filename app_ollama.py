from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
import streamlit as st


st.title("Let's run llm locally")

llm = OllamaLLM(model="qwen2.5:0.5b")


user_message = st.chat_input("Ask any questions")

if user_message:
	with st.chat_message("user"):
		st.markdown(user_message)

	chain = llm | StrOutputParser()

	ai_ans = chain.invoke(user_message)

	with st.chat_message("assistant"):
		st.markdown(ai_ans)


