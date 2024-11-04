import streamlit as st

def game():
    st.header("***GUESSING GAME!!***")
    def rule():
        st.header("***RULES TO PLAY THE GAME!!***")
        st.subheader("1.GUESS THE NUMBER BETWEEN 1 T0 100")
        st.subheader("2.DON'T GUESS ABOVE 100 AND BELOW 1")
        st.subheader("3.IF YOUR GUESS IS CORRECT YOU WIN THE GAME AND WON CASH PRIZE UPTO $1000")
        st.subheader("4.IF YOUR GUESS IS WORNG YOU HAVE A CHANCE TO WIN THE GAME TRY UNTILL THE GAME IS END  ")
        return
    st.write(rule())
    return
def loss():
    st.write("YOUR GUESS IS WRONG!!")
    st.write("TRY LOWER NUMBER!!")
    game()
    return
def lower():
    st.write("YOUR GUESS IS WRONG!!")
    st.write("TRY HIGHER NUMBER!! ")
    game()

game()   
btn=st.button("***START***")
number = 66
attempts=0
if btn:
    guess = st.number_input("ENTER YOUR GUESS:",min_value=0,max_value=100)
    if guess < number:
        lower()
    elif guess > number:
        loss()
    elif  guess == number:
        st.write("CONGRATULATION! YOU WON THE GAME !!")
    else:
        st.write("INVALID NUMBER!!")
        
    


    
