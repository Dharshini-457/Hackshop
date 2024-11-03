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
    btn=st.button("***RESTART!!***")
    if btn:
        game()
    return

game()   
btn=st.button("***START***")
number = 66
attempts=0
if btn:
    st.number_input("ENTER YOUR GUESS:",key="guess")
    if st.session_state.guess < number:
        loss()
        st.write("TRY A HIGHER NUMBER!!!")
    elif st.session_state.guess > number:
        loss()
        st.write("TRY A LOWER NUMBER!!")
    else:
        st.write(f"CONGRATULATION! YOU WON THE GAME WITH{attempts} attempts!!")
        breakpoint
    attempts+=1


    
