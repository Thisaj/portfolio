import streamlit as st
import pandas

# st.set_page_config(layout="wide")

col1, col2 = st.columns(2)

with col1:
    st.image("images/me.jpg", width=300)

with col2:
    st.title("Alireza Jalali")
    content= """
        Hi, I am Alireza Jalali! I am a Python programmer, 
        student teacher, and a few trader.
        I am 20 years old. and here we go... 
        
    
    """
    st.info(content)

content2 = """
Below you can find some of apps i have built in python. feel free to contact me!
"""
st.info(content2)

col3, col4 = st.columns(2)

df = pandas.read_csv("data.csv", sep=";")
with col3:
    for index, row in df[:10].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")

with col4:
    for index, row in df[10:].iterrows():
        st.header(row["title"])
        st.write(row["description"])
        st.image("images/"+row["image"])
        st.write(f"[source code]({row['url']})")