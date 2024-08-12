import streamlit as st
from PIL import Image


img=Image.open("heart.jpg")
st.image(img)
st.header("Check Your :red[Heart] Condition")
name=st.text_input("Enter your name")
age=st.number_input("Enter your age")
mobile=st.text_input("Enter your mobile number")
pulse=st.number_input("Enter your pule per minute")
button1=st.button("Report")

if button1:
    st.subheader("Your :red[Report] is here:")
    st.write("Your Pulse Rate is :",pulse)
    if(pulse<60):       
        st.write("Your heart is :red[very weak,] please consult your nearest doctor")
    elif(pulse>100):        
        st.write("SYour heart is :red[very fast,] please consult your nearest doctor]")    
    else:        
        st.write("Your heart is very normal")    
    
