import streamlit as st
st.title("Mi aplicación")
st.sidebar.header("Esta aplicación es solo un demo")
st.sidebar.image("https://i.ytimg.com/vi/xEzimIGQjIg/sddefault.jpg")
boton = st.balloon("globos")
if boton:
  st.balloon()
