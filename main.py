## integrate code with openAI API
from langchain.llms import OpenAI
import os
from constants import openai_key
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

st.title('Langchain Demo With OPENAI API')
input_text = st.text_input("Search the topic u want")

#open llms
llm = OpenAI(temperature=0.8)

if input_text:
    st.write(llm(input_text))

