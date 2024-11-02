import streamlit as st
from PIL import Image
import pandas as pd
import plotly.express as px
from annotated_text import annotated_text
from streamlit_option_menu import option_menu
with st.sidebar:
    selected = option_menu(
    menu_title=" ",
    options=["HOME","ABOUT ME","PROJECTS","EDUCATION","WHAT I KNOW!"]
)
if selected=="HOME":
    annotated_text(("D"," "))
    st.header("Hi!!!")
    st.title("***I'm Dharshini***")
    image=Image.open("file:///C:/Users/dhars/Downloads/girl.webp")
    st.image(image,caption="Dharshini")
    st.write("https://www.linkedin.com/in/dharshini-878415316")
    image=Image.open("file:///C:/Users/dhars/Downloads/icon3.webp")
    _image=image.resize((70,50))
    st.image(_image,caption=" ")
    image=Image.open("file:///C:/Users/dhars/Downloads/icon1.webp")
    _image=image.resize((50,25))
    st.image(_image,caption=" ")
    image=Image.open("file:///C:/Users/dhars/Downloads/logo.jpg")
    _image=image.resize((50,25))
    st.image(_image,caption=" ")
st.sidebar.header("OPTIONS")
text=st.sidebar.text_area("PASTE THE TEXT HERE")
btn=st.sidebar.button("click here to apply")
if btn:
    st.write(text)   
if selected=="ABOUT ME":
    st.header("ABOUT ME!!")
    st.header("***I AM AN CREATIVE STUDENT DEVELOPER & DESIGNER***")
    st.subheader( "***With 1 years of learning experience in KGISL institution. I'm  passionate about working in data science and machine learning.I'm eager to explore opportunities in software developments and I'd love to contribute to projects involving game development***")
    
if selected=="PROJECTS":
    st.header("***MY CREATIONS</>***")
    btn=st.button(" NOTABLE PROJECTS!!")
    if btn:
        st.subheader("***PORTFOLIO***"," ")
        st.subheader("***GUESSING GAME***")
        st.subheader("***PERSONAL DIARY***")
        st.write("***Are some of my works in addition some web application***")
if selected=="EDUCATION":
    st.subheader("***EDUCATION</>***")
    _dict={" ACADEMIC DETAILS":["10TH STANDARD[STATE BOARD SCHOOL]","12TH STANDARD[STATE BOARD SCHOOL]"],
    "SCORE":['93.2% ','95.5%']}
    st.dataframe(_dict)
if selected=="WHAT I KNOW!":
    st.title("WHAT I KNOW !!!!")
    _dict={"what i know!!":["PYTHON","STREAMLIT","HTML","C++"],
    "PERCENT":[80,50,60,40]}
    fig = px.pie(_dict,names="what i know!!",values="PERCENT",title="  ")
    st.plotly_chart(fig)
    st.header("MY PORTFOLIO IS")
    opt=st.radio(label=" ",options=[" ","GOOD","BAD"])
    if opt=="GOOD":
        st.write("THANKS FOR YOUR APPRECIATION!!")
    elif opt=="BAD":
        st.write("I WILL DO BETTER NEXT TIME!! THANKS FOR YOUR ENCOURAGMENT")
    else:
        pass