import streamlit as st 
from langchain import PromptTemplate, LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
import google.generativeai as genai

# Import the local environment
from dotenv import load_dotenv # for api key storing
import os
load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE-API-KEY"))


# Design the Page ... streamlit run app.py
header = {'authorization':st.secrets["GOOGLE-API-KEY"],
          "content-type":"application/json"}
st.title("Movie Recommender Systems")
user_input = st.text_input("Enter the Movie Title,genre or keyword")

# creating a prompt Template
demo_template = ''' Give me movie recommendations for the following genre {prompt}'''
template = PromptTemplate(
    input_variables = ['prompt'],
    template = demo_template)


# Google Gemini Model
llm = ChatGoogleGenerativeAI(model="gemini-pro",api_key=os.getenv("GOOGLE-API-KEY"))


if user_input:
    prompt = template.format(user_input=user_input)
    recommendations = llm.predict(text=prompt)
    st.write(f"Recommendations: for you :\n {recommendations}")
else:
    st.write(' ')
