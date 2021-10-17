import streamlit as st
import pickle
import string

import base64

main_bg = "first.jpg"
main_bg_ext = "jpg"

side_bg = "second.jpg"
side_bg_ext = "jpg"
st.markdown(
    f"""
    <style>
    .reportview-container {{
        background: url(data:image/{main_bg_ext};base64,{base64.b64encode(open(main_bg, "rb").read()).decode()})
    }}
   .sidebar .sidebar-content {{
        background: url(data:image/{side_bg_ext};base64,{base64.b64encode(open(side_bg, "rb").read()).decode()})
    }}
    </style>
    """,
    unsafe_allow_html=True
)

tfidf = pickle.load(open('vectorizer.pkl','rb'))
model = pickle.load(open('model.pkl','rb'))



st.title("Stock Price Sentimental Analysis Classifier")




input_sms = st.text_area("Enter the News Headline")

if st.button('Predict'):

    # 1. preprocess
    transformed_sms = input_sms
    # 2. vectorize
    vector_input = tfidf.transform([transformed_sms])
    # 3. predict
    result = model.predict(vector_input)[0]
    # 4. Display
    if result == 1:
        st.header("Stock will go high")
    else:
        st.header("Stock will not go high")

