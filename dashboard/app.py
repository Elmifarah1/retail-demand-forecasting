import streamlit as st
import pandas as pd

st.set_page_config(page_title="Retail Demand Forecasting Dashboard", layout="wide")
st.title("Retail Demand Forecasting Dashboard")

@st.cache_data
def load_data():
    return pd.read_csv('../data/processed/train_features.csv', parse_dates=['date'])

df = load_data()
st.write("Data shape:", df.shape)
st.dataframe(df.head())