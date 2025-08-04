import streamlit as st
import pandas as pd
from plots.plot_utils import plot_total_units, plot_monthly_revenue, plot_category_pie

st.set_page_config(page_title="RetailMetrics Stream", layout="wide")

st.title("📈 RetailMetrics Stream – Sales Insights Dashboard")

option = st.sidebar.radio("🧭 Choose what to explore:", [
    "📦 View Product Unit Sales",
    "📉 Track Monthly Revenue Trend",
    "🧩 See Revenue by Product",
    "🔍 Explore Dataset"
])

# Load and preprocess data
df = pd.read_csv("data/sales_data.csv")
df['Date'] = pd.to_datetime(df['Date'], dayfirst=True, errors='coerce')
df = df.dropna(subset=['Date'])

# Rename columns
df.rename(columns={
    'Q-P1': 'Units_A', 'Q-P2': 'Units_B', 'Q-P3': 'Units_C', 'Q-P4': 'Units_D',
    'S-P1': 'Revenue_A', 'S-P2': 'Revenue_B', 'S-P3': 'Revenue_C', 'S-P4': 'Revenue_D'
}, inplace=True)

# Add derived columns
df['Total_Revenue'] = df[['Revenue_A', 'Revenue_B', 'Revenue_C', 'Revenue_D']].sum(axis=1)
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month

if option == "📦 View Product Unit Sales":
    st.subheader("📦 Total Units Sold by Product")
    units = {
        "Product A": df['Units_A'].sum(),
        "Product B": df['Units_B'].sum(),
        "Product C": df['Units_C'].sum(),
        "Product D": df['Units_D'].sum()
    }
    fig = plot_total_units(units)
    st.pyplot(fig)

elif option == "📉 Track Monthly Revenue Trend":
    st.subheader("📉 Revenue Trend Across Months & Years")
    fig = plot_monthly_revenue(df)
    st.pyplot(fig)

elif option == "🧩 See Revenue by Product":
    st.subheader("🧩 Revenue Contribution by Product")
    revenue = {
        "Product A": df['Revenue_A'].sum(),
        "Product B": df['Revenue_B'].sum(),
        "Product C": df['Revenue_C'].sum(),
        "Product D": df['Revenue_D'].sum()
    }
    fig = plot_category_pie(revenue)
    st.pyplot(fig)

elif option == "🔍 Explore Dataset":
    st.subheader("🔍 Dataset Overview")
    st.dataframe(df)
    st.write("📈 Summary Stats")
    st.write(df.describe())
