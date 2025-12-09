import streamlit as st
import pandas as pd

st.title("**BEST ANIMES**")
st.header("Welcome to the **Anime Verse**")
st.subheader("This is a website to showcase different Animes with plot twists")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")
st.write("\n")

#with st.container():
#    st.subheader("Kia")
#    st.image("artifacts\images\Kia.webp")
#    st.subheader("Koniegsegg")
#    st.image("artifacts\images\koniegsegg.webp")
#    st.subheader("Lamborgini")
#    st.image("artifacts\images\lambor.webp")

col1, col2, col3 = st.columns([2, 2, 2],gap="medium",vertical_alignment='center',border=True)
col1.subheader("Lookism")
col1.image("artifacts\Lookism.jpg")
col2.subheader("Naruto")
col2.image("artifacts\\Naruto.jpg")
col3.subheader("One_Piece")
col3.image("artifacts\One_Piece.jpg")  
st.selectbox("Pick one", ["None","Lookism", "Naruto","One_Piece"],placeholder="None")




price = st.slider("Enter Your Budget", min_value=10000, max_value=60000,step=1000,value=55000)
st.write(f"Your Selected Budget is :- {price}")
st.text_input("Enter Your name")
st.text_input("Enter your COntact no")
st.text_input("Enter the Anime you want to Inquiry")
st.text_input(" Your Feedback is Important")
if st.button("Submit"):
    st.switch_page('pages/form_feedback.py')

 