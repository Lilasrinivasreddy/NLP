


import numpy as np
import pickle
import pandas as pd
#from flasgger import Swagger
import streamlit as st 

from PIL import Image

#app=Flask(__name__)
#Swagger(app)

pickle_in = open("classifier.pkl","rb")
classifier=pickle.load(pickle_in)

#@app.route('/')
def welcome():
    return "Welcome All"

#@app.route('/predict',methods=["Get"])
def predict_note_authentication(variance,skewness,curtosis,entropy):
   
  prediction=classifier.predict([[variance,skewness,curtosis,entropy]])
  print(prediction)
  return prediction


#@app.route('/')
def main():
    st.title("Bank Note Authenticator")
    html_temp = """
    <div style="background-color:tomato;padding:10px">
    <h2 style="color:white;text-align:center;">Streamlit Bank Note Authenticator ML App </h2>
    </div>
    """

    st.markdown(html_temp,unsafe_allow_html=True)
    variance = st.text_input("Variance","Ex:8")
    skewness = st.text_input("skewness","Ex:8")
    curtosis = st.text_input("curtosis","Ex:8")
    entropy = st.text_input("entropy","Ex:8")
    result=""
    if st.button("Predict"):
        result=predict_note_authentication(variance,skewness,curtosis,entropy)
    st.success('The output is  {}'.format(result))
    if st.button("About Creator"):
        st.text("Anil L")
        st.text("BE Graduated")
        st.text("Built Streamlit")

if __name__=='__main__':
    main()
    
    
    