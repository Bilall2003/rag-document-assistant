import streamlit as st
import numpy as np
import torch
from transformers import pipeline
import time


st.title("CHATBOT BETA")

st.text_area(label="Here",placeholder="Write a message...",label_visibility="collapsed") 
st.link_button("This is AI and can make mistakes. Please double-check responses.",url="https://mljourney.com/can-ai-make-mistakes-understanding-ai-errors-and-limitations/")
