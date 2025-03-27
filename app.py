import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/vg_sales.csv')
df = df.drop(['img'], axis = 1)
st.title('GameIntel Dashboard')

st.dataframe(df)