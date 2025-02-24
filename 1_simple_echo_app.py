import streamlit as st

st.title("Simple Chat App")

# Task 1: Write some text on the browser
st.write("Welcome to the Simple Chat App!")
st.markdown("You can ask questions and get responses here.")

# Task 2: Design ChatGPT-like UI to get user input
if "messages" not in st.session_state:
    st.session_state.messages = []

user_input = st.chat_input("Type your message here...")

if user_input:
    # Add user message to the chat history
    st.session_state.messages.append({"role": "user", "content": user_input})
    # Here you would typically call your chatbot API to get a response
    # For demonstration, we'll just echo the user's message
    response = f"Echo: {user_input}"
    st.session_state.messages.append({"role": "ai", "content": response})

# Task 3: Display the 'user' and 'response-to-question'
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    else:
        st.chat_message("ai").write(message["content"])
