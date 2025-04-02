import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/vg_sales.csv')
df = df.drop(['img'], axis = 1)
df['release_date'] = pd.to_datetime(df['release_date'])
df['total_sales'].dropna()
def set_time_interval(initial, final):
    time_filter = (df['release_date'].dt.year >= initial) & (df['release_date'].dt.year <= final)
    return df[time_filter]

#! Layout do Dashboard
st.set_page_config(
    page_title = 'GameIntel',
    page_icon = "🎮",
    layout = "wide"
)
st.sidebar.header('Filtros')
st.title('Game Intel')

st.sidebar.multiselect(
    label = "Genre",
    options = df['genre'].unique().tolist(),
    placeholder = "Select one or more genres"
)
publisher = st.sidebar.multiselect(
    label = "Publisher",
    options = df['publisher'].unique().tolist(),
    placeholder = "Select one or more publishers"
)
if st.sidebar.checkbox('Time Interval'):
    years = st.sidebar.slider(
        label = "Year",
        min_value = df['release_date'].min().year,
        max_value = df['release_date'].max().year,
        value = (1980, 2020)
    )
    df = set_time_interval(years[0], years[1])
    fig = px.bar(df, x=df['release_date'].dt.year, y='total_sales')
    st.plotly_chart(fig)
else:
    year = st.sidebar.slider(
        label = "Year",
        min_value=df['release_date'].min().year,
        max_value=df['release_date'].max().year,
        value=(1980)
    )
    df = set_time_interval(year, year)
    fig = px.pie(df, names = 'console',values='total_sales')
    st.plotly_chart(fig)

