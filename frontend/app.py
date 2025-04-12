import streamlit as st 
from utils import *

st.title("Todo List App")
st.subheader("Actual Task List")

tasks = get_tasks()
if tasks:
    for task in tasks:
        st.write(f"- {task[1]}")
