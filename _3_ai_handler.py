import streamlit as st
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.messages import HumanMessage, AIMessage

from _3_tools import tools, get_tool_desc

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash").bind_tools(tools)


def generate_message_response(message: str, history):
    "Entry point to generate AI response from user message"
    messages = list(history)
    messages.append(HumanMessage(content=message))

    chat_ai_res = llm.invoke(messages)

    try:
        messages.append(chat_ai_res)
        # Handling tool calls
        # Reference: https://python.langchain.com/docs/how_to/tool_results_pass_to_model/
        for tool_call in chat_ai_res.tool_calls:
            selected_tool = get_tool_desc()[
                tool_call["name"].lower()]
            print(f"tool_calling: {selected_tool}")
            
            tool_msg = selected_tool.invoke(tool_call)
            print(tool_msg)
            messages.append(tool_msg)

    except Exception as e:
        print(f"Error tool_calling: {e}")

    if chat_ai_res.tool_calls is None:
        return [chat_ai_res, messages]
    else:
        chat_ai_res = llm.invoke(messages)
        return [chat_ai_res, messages]
