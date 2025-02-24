from langchain_ollama import OllamaLLM
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

st.title("Let's run llm locally")

# TODO: Update to any other lightweight model
# Define the LLM instance
llm = OllamaLLM(model="qwen2.5:0.5b")

if "messages" not in st.session_state:
    st.session_state.messages = []

# Use streamlit chat_input to get the user question
user_message = st.chat_input("Type your message here...")

if user_message:
    st.session_state.messages.append({"role": "user", "content": user_message})

	# TODO: Create a chain llm | StrOutputParser()
    chain = llm | StrOutputParser()

	# TODO: invoke the chain with the user question to get the AI response
    response = chain.invoke(user_message)
	
		# Add AI response to the chat history
    st.session_state.messages.append({"role": "ai", "content": response})

	# TODO: Display the AI Response on the website.
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("ai").write(message["content"])

