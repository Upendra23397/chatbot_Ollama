# Mood-Based AI Chatbot (LangChain + Ollama + Streamlit)

A simple chatbot with selectable personalities (Angry / Funny / Sad), built with
**LangChain**, running a **local LLM via Ollama**, with a **Streamlit** web UI.

---

## What it does

- The user picks a "mode" for the AI: Angry, Funny, or Sad.
- That mode is turned into a `SystemMessage` that shapes the AI's tone and personality.
- The user chats with the model in a normal chat interface.
- The full conversation history is kept and sent back to the model on every turn,
  so it has context of what was said before.

---

## Tech Stack

| Piece | Purpose |
|---|---|
| **Ollama** | Runs the LLM (`llama3.2`) locally on your machine — no API key, no internet, no cost per call |
| **LangChain (`langchain_ollama`, `langchain_core`)** | Provides a consistent interface (`ChatOllama`) to talk to the model, and standard message types (`SystemMessage`, `HumanMessage`, `AIMessage`) to structure the conversation |
| **Streamlit** | Turns the Python script into a web UI with almost no extra code — `st.chat_input`, `st.chat_message`, `st.radio`, `st.session_state` |

---

## How to run it

1. Install and start [Ollama](https://ollama.com), then pull the model:
   ```
   ollama pull llama3.2
   ```
2. Install Python dependencies:
   ```
   pip install streamlit langchain-ollama langchain-core
   ```
3. Run the app:
   ```
   streamlit run app_ollama.py
   ```

---

## Code walkthrough (for explaining in an interview)

### 1. The model
```python
model = ChatOllama(model="llama3.2", temperature=0.9)
```
`ChatOllama` is LangChain's wrapper around a locally running Ollama server.
`temperature=0.9` makes responses more random/creative rather than deterministic
(0 = always most likely answer, 1 = more varied/surprising answers).

### 2. The mode / persona
```python
mode = "You are an angry AI agent. You respond aggressively and impatiently."
```
This becomes a `SystemMessage` — a special message type that isn't shown to the
user but tells the model *how* to behave for the entire conversation. It's the
standard way to give an LLM a persona or instructions in LangChain (and most
chat APIs in general).

### 3. Message history & memory
```python
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=mode)]
```
LLMs are stateless — each API/model call has no memory of previous calls by
itself. To fake "memory," you resend the **entire conversation** (system + all
past human/AI turns) every time. `st.session_state` is Streamlit's way of
persisting Python variables across reruns (since Streamlit re-executes the
whole script top-to-bottom on every interaction) — so the message list survives
between chat turns instead of resetting.

### 4. The chat loop
```python
response = model.invoke(st.session_state.messages)
st.session_state.messages.append(AIMessage(content=response.content))
```
`model.invoke(...)` sends the whole message list to the model and gets one
response back. That response is wrapped in an `AIMessage` and appended to the
history so the *next* call includes it as context.

### 5. Streamlit UI pieces
- `st.radio(...)` — lets the user pick a mode (renders as radio buttons).
- `st.chat_input(...)` — a chat-style text box pinned to the bottom of the page.
- `st.chat_message("user")` / `st.chat_message("assistant")` — renders messages
  as chat bubbles, styled per role.
- `st.session_state` — Streamlit's key-value store that persists across reruns
  within a browser session (this is what plain Python variables can't do here,
  since the script re-runs from scratch on every user action).

---

## Likely interview questions & how to answer them

**Q: Why does the message history need to be resent every time?**
A: LLM APIs (and Ollama) are stateless — the model has no built-in memory
between calls. LangChain's message objects (`SystemMessage`, `HumanMessage`,
`AIMessage`) let you represent a full conversation as a list, which is resent
each turn so the model can see prior context.

**Q: What's the difference between `SystemMessage`, `HumanMessage`, and `AIMessage`?**
A: They represent the three roles in a chat conversation — `SystemMessage` sets
behavior/instructions (usually invisible to the end user), `HumanMessage` is
what the user typed, and `AIMessage` is what the model responded. Structuring
messages this way is a LangChain convention that maps to how most chat-based
LLM APIs (OpenAI, Anthropic, Ollama, etc.) expect input.

**Q: Why Ollama instead of an API like OpenAI/Anthropic?**
A: Ollama runs the model locally on your own hardware — no API key, no
per-token cost, and it works offline. Trade-off: you need enough local
compute (RAM/GPU) and local models are often smaller/less capable than the
largest hosted models.

**Q: Why does Streamlit need `st.session_state`?**
A: Streamlit reruns the entire script from top to bottom on every user
interaction (like a page refresh). Normal Python variables would reset every
time, so `st.session_state` is used to persist things — like chat history —
across those reruns for the same user session.

**Q: What would you change to make this production-ready?**
A: Some ideas to mention: add error handling around the Ollama call, add a way
to persist conversations to a database instead of only in-memory session
state, support multiple concurrent users properly, add streaming responses
token-by-token instead of waiting for the full reply, and add input
validation/rate limiting.

**Q: What is `temperature` doing?**
A: It controls the randomness of the model's output. Lower values (near 0)
make it more deterministic and repetitive; higher values (near 1) make it more
varied and creative, at some risk of less coherent answers.

---

## Possible extensions to mention if asked "what would you add next?"

- Streaming responses (token-by-token) instead of waiting for the full reply
- A "clear conversation" button
- Saving/loading past conversations
- Support for switching models or providers (e.g. also allow a hosted API model)
- Adding retrieval-augmented generation (RAG) so the bot can answer from your
  own documents
