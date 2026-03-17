import streamlit as st
import pickle
import numpy as np
from PIL import Image


with open("model_knn.save", "rb") as file:
    model = pickle.load(file)

st.title(":yellow[SALARY PREDICTION]")
im=Image.open("bg.jpg")
st.image(im,width=800)

st.divider()


st.write("Using this, you can get estimations for the salaries of the company employees.")

Years=st.number_input("Enter the years at the company",value=1,step=1,min_value=0)
Jobrate=st.number_input("Enter the job rate",value=3.5,step=0.5,min_value=0.0)

x=[Years,Jobrate]


st.divider()

predict=st.button("Press the button for Salary Prediction")

st.divider()

if predict:
    st.balloons()
    
    x1=np.array([x])

    prediction=model.predict(x1)[0]

    st.write(f"Salary Prediction is {prediction:,.2f}")

else:
    "Please press the button to make the prediction"

