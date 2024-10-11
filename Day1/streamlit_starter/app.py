import streamlit as st
from transformers import pipeline

# Load the sentiment analysis model
@st.cache_resource  # This decorator caches the function's return value
def load_model():
    # Use the Transformers pipeline for sentiment analysis
    # This automatically downloads and loads a pre-trained model
    return pipeline("sentiment-analysis")

# Streamlit app
def main():
    st.title("Streamlit Sentiment Analysis")
    st.write("Enter some text, and we'll analyze its sentiment!")

    # Load the model using the cached function
    # This ensures the model is loaded only once and reused
    sentiment_analyzer = load_model()

    # Create a text input area for user input
    user_input = st.text_area("Enter your text here:")

    # Create a button to trigger the analysis
    if st.button("Analyze Sentiment"):
        if user_input:
            # Use the Transformers pipeline to perform sentiment analysis
            # The pipeline handles tokenization and inference
            result = sentiment_analyzer(user_input)[0]
            
            # Extract the sentiment label and confidence score
            sentiment = result["label"]
            confidence = result["score"]
            
            # Display the results
            st.write(f"Sentiment: {sentiment}")
            st.write(f"Confidence: {confidence:.2f}")
            
            # Create a color-coded box based on the sentiment
            color = "green" if sentiment == "POSITIVE" else "red"
            st.markdown(f'<div style="background-color:{color};padding:10px;border-radius:5px;">{sentiment}</div>', unsafe_allow_html=True)
        else:
            st.write("Please enter some text to analyze.")

if __name__ == "__main__":
    main()
