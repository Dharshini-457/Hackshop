import streamlit as st
st.title("My Portfolio!!")

name = st.text_input("Enter your name:")
st.write(f"Hi!!{name}")
if name=="Dharshini":
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
            st.write("**personal diary")
else:
    st.write("Your are not dharshini")
    
