import streamlit as st
def binary(arr,target):
    low=0
    high=len(arr)-1
    while low<=high:
        mid=(low+high)//2
        if arr[mid]==target:
            st.write(mid)
        elif arr[mid]<target:
            low=mid+1
        else:
            high=mid-1
        return 0

def game():
    st.title("GUESSING GAME!!")
    num_to_guess=st.sidebar.slider("NUMBER TO GUESS",min_value=1,max_value=100,value=50)
    arr=list(range(1,101))
    st.write("GUESS A NUMBER BETWEEN 1-100")
    user_guess=st.number_input("YOUR GUESS.....",min_value=1,max_value=100)
    result=binary(arr,user_guess)
    if st.button("CHECK"):
        if result!=0:
            st.success(f"IT IS RIGHT!! The number was{num_to_guess}")
            st.balloons()
        else:
            st.error(f"IT IS WRONG!! The number was {num_to_guess}")
            game()

def rule():
    st.write("WELCOME TO OUR GAME !!")
    st.write(" Before we start the game the ruele of the game is must be followed ")
    st.write("Guess a number between 1 to 100")
    st.write("If the game fails restart the game and play again!!")
    if st.button("START!!"):
        game()
rule()

        