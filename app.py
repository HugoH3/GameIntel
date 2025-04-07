import pandas as pd
import plotly.express as px
import streamlit as st

df = pd.read_csv('data/vg_sales.csv')
df = df.drop(['img'], axis=1)
df['release_date'] = pd.to_datetime(df['release_date']) # Muda o 'release_date' de string para um obj datetime
df['year'] = df['release_date'].dt.year # Cria uma coluna apenas com os anos
df = df.dropna(subset=['total_sales']) # Remove jogos sem info sobre vendas

def set_time_interval(initial, final):
    time_filter = (df['release_date'].dt.year >= initial) & (df['release_date'].dt.year <= final)
    return df[time_filter]
def set_publisher(publisher):
    if publisher is None:
        return df
    publisher_filter = (df['publisher'] == publisher)
    return df[publisher_filter]

def set_region(region):
    if region == 'JP':
        df['total_sales'] = df['jp_sales']
    elif region == 'NA':
        df['total_sales'] = df['na_sales']
    elif region == 'PAL':
        df['total_sales'] = df['pal_sales']


#! Layout do Dashboard

st.set_page_config(
    page_title='GameIntel',
    page_icon="🎮",
    layout="wide"
)
st.sidebar.header('Filters')
st.title('GameIntel: VG Sales Dashboard')

publisher = st.sidebar.selectbox(
    label="Publisher",
    index=None,
    options=df['publisher'].unique().tolist(),
    placeholder="Select a publisher"
)
region = st.sidebar.selectbox(
    label="Region",
    index=None,
    options=['JP', 'NA', 'PAL'],
    placeholder="Filter region"
)
# Pega a regiao escolhida e atribui as vendas dela ao 'total_value' para criar as metricas filtradas
set_region(region)
 #! Remove jogos não lançados na região
df = df.dropna(subset=['total_sales'])

df = set_publisher(publisher)
if publisher is not None:
    st.subheader(f"Showing data for: {publisher}")
else:
    st.subheader(f"Overview")
checkbox = st.sidebar.checkbox('Set interval')
if checkbox:
    years = st.sidebar.slider(
        label="Year",
        min_value=df['release_date'].min().year,
        max_value=df['release_date'].max().year,
        value=(1980, 2020)
    )
    df = set_time_interval(years[0], years[1])
else:
    year = st.sidebar.slider(
        label="Year",
        min_value=df['release_date'].min().year,
        max_value=df['release_date'].max().year,
        value=2011
    )
    df = set_time_interval(year, year)
    bar = px.bar(df, x='release_date', y='total_sales')


sales_per_year = df.groupby('year')['total_sales'].sum().reset_index()
bar = px.bar(df, x='console', y='total_sales', color='console')
pie = px.pie(df, values='total_sales', names='genre')
line = px.line(sales_per_year, x='year', y='total_sales')
c1 = st.container(border=True)
col1, col2 = st.columns(2, border=True)

with c1:
    if checkbox:
        st.subheader('Income over the years')
        st.plotly_chart(line)
    elif publisher is not None:
        st.subheader('Games sold this year')
        bar2 = px.bar(df, x='title', y='total_sales', color='developer')
        st.plotly_chart(bar2)
    else:
        st.subheader('Top 10 Best Sellers of the year')
        total_sales_by_game = df.groupby(['title', 'publisher'])['total_sales'].sum().reset_index()
        total_sales_by_game.sort_values(by=['total_sales'], ascending=False, inplace=True)
        bar2 = px.bar(total_sales_by_game.head(10), x='title', y='total_sales',color='publisher')
        st.plotly_chart(bar2)

    total_income = df['total_sales'].sum()
    if total_income > 999:
        st.metric(label="Total Income", value=f"${total_income:,.2f}B")
    else:
        st.metric(label="Total Income", value=f"${total_income:,.2f}Mi")


with col1:
    st.subheader('Sales by Genre')
    st.plotly_chart(pie)
with col2:
    st.subheader('Sales by Console')
    st.plotly_chart(bar)

with st.expander("View dataframe"):
    st.dataframe(df)


