from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

st.title("Let's run llm locally")

# TODO: Update to any other lightweight model
llm = OllamaLLM(model="qwen2.5:0.5b")

# TODO: Use streamlit chat_input to get the user question and assign it to variable 'user_message' 
user_message = ""

if user_message:
	# TODO: Display the user message on the website.
	with st.chat_message("user"):
		st.markdown(user_message)

	# TODO: Create a chain llm | StrOutputParser()

	# TODO: invoke the chain with the user question to get the AI response

	# TODO: Display the AI Response on the website.

