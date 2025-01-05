import streamlit as st
import pandas as pd
import sqlite3

# Title
st.title("Personal Expense Tracker")

# User selects the month
month_map = {
    "January": "01", "February": "02", "March": "03", "April": "04",
    "May": "05", "June": "06", "July": "07", "August": "08",
    "September": "09", "October": "10", "November": "11", "December": "12"
}

selected_month = st.selectbox("Select a month:", list(month_map.keys()))
table_name = month_map[selected_month]

# Connect to database and fetch data
conn = sqlite3.connect('expenses.db')
query = f'SELECT * FROM "{table_name}"'
data = pd.read_sql_query(query, conn)
conn.close()

# Display data
st.dataframe(data)

# Example visualization
st.bar_chart(data.groupby('category')['amount_paid'].sum())
