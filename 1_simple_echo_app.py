import streamlit as st

st.title("Simple app")

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
	
	ans = f"Hi you said {prompt}"

	with st.chat_message("assistant"):
		st.markdown(ans)
		messages.append({"role": "assistant", "content": ans})