import streamlit as st

st.title("Check Your Heart Condition")
name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
mobile=st.text_input("Enter your mobile number")
pulse=st.number_input("Enter your pule per minute")

st.markdown("Your Report is here:")

if(pulse<60):
    st.write("Your Pulse Rate is :",pulse)
    st.write("Your heart is very weak, please consult your nearest doctor")
elif(pulse>100):
    st.write("Your Pulse Rate is :",pulse)
    st.write("Your heart is very fast, please consult your nearest doctor")
    
else:
    st.write("Your Pulse Rate is :",pulse)
    st.write("Your heart is very normal")    
    

        
