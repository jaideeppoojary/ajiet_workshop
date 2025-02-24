import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

st.title("Generative AI app")

#TODO: Task 1 - Write some text on the browser. (use can use st.write("hi") or st.markdown("hi"))
st.write("Welcome to the Generative AI App!")
st.markdown("You can ask questions and get responses powered by Google's Generative AI.")

#TODO: Task 2 - Design Chat-Gpt like UI to get user input. (hint: st.chat_input)
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Type your message here...")

#TODO: Task 3 - Defined the LLM instance
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

#TODO: Task 4 - Create a LLM chain using the 'StrOutputParser()'
chain = llm | StrOutputParser()

#TODO: Task 5 - Display the 'user' and 'AI response'. (hint: st.chat_message("user"), st.chat_message("ai"))
if user_input:
    # Add user message to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})

    # Get the AI response
    response = chain.invoke(user_input)

    # Add AI response to the chat history
    st.session_state.messages.append({"role": "ai", "content": response})

# Task 5: Display the 'user' and 'AI response'
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("ai").write(message["content"])

