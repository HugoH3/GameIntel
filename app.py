import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/vg_sales.csv')
df = df.drop(['img'], axis = 1)
df['release_date'] = pd.to_datetime(df['release_date'])

st.set_page_config(
    page_title = 'GameIntel',
    page_icon = "🎮",
    layout = "wide"
)
genre = st.selectbox(
    label = "Genre",
    options = df['genre'].unique().tolist(),
    index = None,
    placeholder = "Select a Genre"
)
year  = st.selectbox(
    label = "Year of release",
    options = df['release_date'].dt.year.unique().tolist(),
    index = None,
    placeholder = "Select a Year of Release"
)
developer = st.selectbox(
    label = "Developer",
    options = df['developer'].unique().tolist(),
    index = None,
    placeholder = "Select a Developer"
)
st.title('Game Intel')
