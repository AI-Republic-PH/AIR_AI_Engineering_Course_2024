import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="Sentiment Analysis", page_icon="📊")

st.markdown("# 📊 TransformersSentiment Analysis")
st.sidebar.header("Sentiment Analysis")

# Load the sentiment analysis model
@st.cache_resource
def load_model():
    return pipeline("sentiment-analysis")

# Streamlit app
def main():
    st.write("Enter some text, and we'll analyze its sentiment!")

    # Load the model
    sentiment_analyzer = load_model()

    # User input
    user_input = st.text_area("Enter your text here:")

    if st.button("Analyze Sentiment"):
        if user_input:
            # Perform sentiment analysis
            result = sentiment_analyzer(user_input)[0]
            
            # Display result
            sentiment = result["label"]
            confidence = result["score"]
            
            st.write(f"Sentiment: {sentiment}")
            st.write(f"Confidence: {confidence:.2f}")
            
            # Simple color-coded box
            color = "green" if sentiment == "POSITIVE" else "red"
            st.markdown(f'<div style="background-color:{color};padding:10px;border-radius:5px;">{sentiment}</div>', unsafe_allow_html=True)
        else:
            st.write("Please enter some text to analyze.")

if __name__ == "__main__":
    main()