## integrate code with openAI API
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
import os
from constants import openai_key
import streamlit as st

os.environ["OPENAI_API_KEY"] = openai_key

st.title('Celebrity Search Results')
input_text = st.text_input("Search the topic u want")

#Promt templates

first_input_prompt = PromptTemplate(
    input_variables= ['name'],
    template = "Tell me about celebrity  {name}"
)

llm = OpenAI(temperature=0.8)
chain = LLMChain(llm=llm,prompt=first_input_prompt,verbose=True)
#open llms

if input_text:
    st.write(chain.run(input_text))

