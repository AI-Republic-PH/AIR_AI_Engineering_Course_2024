import streamlit as st

st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="👋",
)

st.write("# Welcome to Day 1 of our AI Engineering Bootcamp! 👋")

st.sidebar.success("Select a page above.")

st.markdown(
    """
    
    ### Pages
    - 📊 Sentiment Analysis with Transformers
    - 📊 Sentiment Analysis with SpaCy Textblob
    """
)