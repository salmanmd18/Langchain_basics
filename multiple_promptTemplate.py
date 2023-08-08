## integrate code with openAI API
from langchain.llms import OpenAI
from langchain import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import SimpleSequentialChain,SequentialChain

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
chain = LLMChain(llm=llm,prompt=first_input_prompt,verbose=True,output_key='person')
#open llms
second_input_prompt = PromptTemplate(
    input_variables= ['person'],
    template = "when was {person} born"
)


chain2 = LLMChain(llm=llm,prompt=second_input_prompt,verbose=True,output_key='dob')

third_input_prompt = PromptTemplate(
    input_variables= ['dob'],
    template = "Mention 5 major events happened round {dob} in the world"
)

chain3 = LLMChain(llm=llm,prompt=third_input_prompt,verbose=True,output_key='description')



# SimpleSequentialChain gives only the last information
#parent_chain = SimpleSequentialChain(chains=[chain,chain2],verbose=True)
# SequentialChain gives the entire information
parent_chain = SequentialChain(chains=[chain,chain2,chain3],input_variables = ['name'],output_variables=['person','dob','description'],verbose=True)

if input_text:
    # st.write(parent_chain.run(input_text))
    st.write(parent_chain({'name': input_text}))

