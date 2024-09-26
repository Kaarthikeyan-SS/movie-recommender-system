import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# Import the Local Environment
from dotenv import load_dotenv
import os
load_dotenv()
genai.configure(api_key =os.getenv('GOOGLE-API-KEY'))
# Design the Page ... streamlit run app.py
headers = {'authorization':st.secrets['GOOGLE-API-KEY'],"content-type":"application/json"}
st.title("Movie Recommender Systems")
user_input = st.text_input("Enter the Movie Title,genre or keyword")

# creating a prompt Template
demo_template = '''I want you to act as a Dietician and help me with {prompt}'''
template = PromptTemplate(
    input_variables = ['prompt'],
    template = demo_template)


# Google Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-pro",api_key='GOOGLE-API-KEY')


if user_input:
    prompt = template.format(user_input=user_input)
    recommendations = llm.predict(text=prompt)
    st.write(f"Recommendations: for you :\n {recommendations}")
else:
    st.write(' ')