from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
import streamlit as st

llm = ChatGoogleGenerativeAI(model="gemini-3.5-flash-lite")

out = StrOutputParser()

st.title("RUBY: AI Chatbot")
st.markdown("QnA Bot created using Google Gemini and Streamlit")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]

    st.chat_message(role).markdown(content)

query = st.chat_input("Ask anything? ")
if query:
    st.session_state.messages.append({"role": "user", "content": query})
    st.chat_message("user").markdown(query)
    res = llm.invoke(query)
    answer = out.invoke(res)
    st.chat_message("ai").markdown(answer)
    st.session_state.messages.append({"role": "ai", "content": answer})