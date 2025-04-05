import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv('data/vg_sales.csv')
df = df.drop(['img'], axis=1)
df['release_date'] = pd.to_datetime(df['release_date'])
df = df.dropna(subset=['total_sales'])
df['year'] = df['release_date'].dt.year

def set_time_interval(initial, final):
    time_filter = (df['release_date'].dt.year >= initial) & (df['release_date'].dt.year <= final)
    return df[time_filter]
def set_publisher(publisher):
    if publisher is None:
        return df
    publisher_filter = (df['publisher'] == publisher)
    return df[publisher_filter]
def set_developer(developer):
    if developer is None:
        return df
    developer_filter = (df['developer'] == developer)
    return df[developer_filter]
def set_region(region):
    if region is None:
        return df
    region_filter = (df['region'] == region)

#! Layout do Dashboard
st.set_page_config(
    page_title='GameIntel',
    page_icon="🎮",
    layout="wide"
)
st.sidebar.header('Filtros')
st.title('Game Intel')

publisher = st.sidebar.selectbox(
    label="Publisher",
    index=None,
    options=df['publisher'].unique().tolist(),
    placeholder="Select a publisher"
)
df = set_publisher(publisher)

developer = st.sidebar.selectbox(
    label = "Developer",
    index = None,
    options = df['developer'].unique().tolist(),
    placeholder = "Select a developer"
)

df = set_developer(developer)

if st.sidebar.checkbox('Set interval'):
    years = st.sidebar.slider(
        label="Year",
        min_value=df['release_date'].min().year,
        max_value=df['release_date'].max().year,
        value=(1980, 2020)
    )
    df = set_time_interval(years[0], years[1])
    df = df.sort_values(by='release_date')
    fig = px.bar(df, x='console', y='total_sales')
    st.plotly_chart(fig)
else:
    year = st.sidebar.slider(
        label="Year",
        min_value=df['release_date'].min().year,
        max_value=df['release_date'].max().year,
        value=1980
    )
    df = set_time_interval(year, year)
    fig = px.bar(df, x='console', y='total_sales')
    st.plotly_chart(fig)

st.dataframe(df)