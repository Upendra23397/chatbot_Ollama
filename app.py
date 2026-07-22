import streamlit as st
from langchain_ollama import ChatOllama
from langchain_core.messages import AIMessage, HumanMessage, SystemMessage

st.title("Choose your AI mode")

mode_choice = st.radio(
    "Select a mode",
    options=[1, 2, 3],
    format_func=lambda x: {1: "Angry mode", 2: "Funny mode", 3: "Sad mode"}[x],
)

if mode_choice == 1:
    mode = "You are an angry AI agent. You respond aggressively and impatiently."
elif mode_choice == 2:
    mode = "You are a very funny AI agent. You respond with humor and jokes."
elif mode_choice == 3:
    mode = "You are a very sad AI agent. You respond in a depressed and emotional tone."
else:
    mode = "You are a helpful AI assistant."

model = ChatOllama(
    model="llama3.2",
    temperature=0.9
)

if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]

st.write("------ Welcome! ------")

for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        st.chat_message("user").write(msg.content)
    elif isinstance(msg, AIMessage):
        st.chat_message("assistant").write(msg.content)

prompt = st.chat_input("You:")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    st.chat_message("user").write(prompt)

    response = model.invoke(st.session_state.messages)

    st.session_state.messages.append(AIMessage(content=response.content))
    st.chat_message("assistant").write(response.content)