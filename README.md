# RUBY---AI-Chatbot
A Q&A chatbot built with Google Gemini and Streamlit.

## Contents
- 1_QnA_Bot.py: Q&A chatbot using Gemini and Streamlit

## Setup
1. Clone the repo and open the folder
2. Install dependencies:
   pip install -r requirements.txt
3. Copy .env.example to .env and add your own GOOGLE_API_KEY

## Run
streamlit run 1_QnA_Bot.py

The app opens in your browser at http://localhost:8501

## Roadmap
- [ ] Streaming responses
- [ ] Conversation memory
- [ ] Rebuild with LangChain
- [ ] Switch model providers with one line

## What I learned
- Knowledge cutoff: models can't answer about events after their
  training data
- How to call the Gemini API from Python and handle the response
- Building a chat UI with Streamlit
