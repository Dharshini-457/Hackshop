import streamlit as st
from PIL import Image
ist.markdown("<style>body{background-color:#333;}</style>",unsafe_allow_html=True)
mage=Image.open("file:///C:/Users/dhars/Downloads/KRS_7411.webp")
st.image(image,caption='Murugar',)
st.title("My Portfolio!!")

name = st.text_input("Enter your name:")
st.write(f"Hi!!{name}")
if name == "Dharshini":
    st.title("Your prortfolio is")
    btn = st.button("view education!!")
    if btn:
        st.header("My education")
        dict={"Institution name:":['abc school','kg college'],
        "year:":[2024,2028],
        "marks":[524,9.5]}
        st.dataframe(dict)
    btn = st.button(" view project")
    if btn:
        st.title("My projects")
       
        project=["*Personal Diary","*Todo Game"]
        st.dataframe(project)
