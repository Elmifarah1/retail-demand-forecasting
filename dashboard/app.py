from pathlib import Path
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Retail Demand Forecasting Dashboard", layout="wide")
st.markdown("<h1 style='text-align:center;'>Retail Demand Forecasting Dashboard</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Built by Elmi Farah · Code Institute Capstone Project</p>", unsafe_allow_html=True)
st.write("")

@st.cache_data(show_spinner="Loading data…")
def load_data():
    data_path = Path(__file__).resolve().parent.parent / "data" / "processed" / "train_features_sample.csv.gz"
    
    if not data_path.exists():
        st.error(f"⚠️ Data file not found at:\n{data_path}")
        st.stop()
    
    return pd.read_csv(data_path, parse_dates=['date'], compression='gzip')

df = load_data()
st.write("Data shape:", df.shape)
st.dataframe(df.head())

st.sidebar.header("Filters")

store = st.sidebar.selectbox("Select Store", sorted(df['store_nbr'].unique()))
family = st.sidebar.selectbox("Select Family", sorted(df['family'].unique()))

filtered = df[(df['store_nbr'] == store) & (df['family'] == family)]

st.write(f"Selected: Store {store} | Family: {family}")
st.dataframe(filtered.head())

import matplotlib.pyplot as plt

st.subheader("Sales Over Time")

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(filtered['date'], filtered['sales'], color='steelblue')
ax.set_xlabel("Date")
ax.set_ylabel("Sales")
ax.set_title(f"Store {store} – {family}")
st.pyplot(fig)

st.subheader("Top 10 Product Families by Total Sales")

top_families = (
    df.groupby('family')['sales']
      .sum()
      .sort_values(ascending=False)
      .head(10)
)

st.bar_chart(top_families)

st.subheader("Monthly Sales Trend")

monthly = (
    df.assign(month=df['date'].dt.to_period('M').dt.to_timestamp())
      .groupby('month', as_index=False)['sales']
      .sum()
)

import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(monthly['month'], monthly['sales'], color='orange')
ax.set_xlabel("Month")
ax.set_ylabel("Total Sales")
st.pyplot(fig)

import seaborn as sns

st.subheader("Sales by Day of Week")

df['day_of_week'] = df['date'].dt.day_name()
order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

fig, ax = plt.subplots(figsize=(8, 4))
sns.boxplot(data=df, x='day_of_week', y='sales', order=order, ax=ax, palette='Blues')
ax.set_xlabel("Day of Week")
ax.set_ylabel("Sales")
st.pyplot(fig)

st.markdown("---")
st.subheader("Project Summary")
st.write("""
This interactive dashboard visualises sales trends across stores and product families to support retail demand forecasting.  
It helps identify peak seasons, top-performing product lines, and overall sales behaviour patterns.  
Insights from this analysis can support data-driven decision-making for stock planning and promotional strategies.
""")