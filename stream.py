import streamlit as st
import pandas as pd 
import numpy as np 

st.title("My first cloud app")

st.write("A simple dataframe:")

df=pd.DataFrame(np.random.randn(10,2),columns=['cols1','cols2'])
st.dataframe(df)