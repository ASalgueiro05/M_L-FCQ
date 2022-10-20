import streamlit as st
from img_classification import teachable_machine_classification
import keras
from PIL import Image, ImageOps
import numpy as np

st.title("Aplicación de reconocimiento de Indian Food")

uploaded_file = st.file_uploader("Carga una imagen ...", type=["jpg","jpeg"])
if uploaded_file is not None:
  image = Image.open(uploaded_file)
  st.sidebar.image(image)
  label = teachable_machine_classification(image, 'keras_model.h5') 
  if label== 0:
    st.write("Tortillas de Harina :)")
  if label== 1:
    st.write("Empanadas")

genre = st.radio("Que prefieres?",("Empanadas","Tortillas de harina","Sopa de pollo"))
st.balloons()
