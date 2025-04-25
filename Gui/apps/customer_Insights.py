import streamlit as st
import pandas as pd
from PIL import Image
import plotly.express as px

# Read data from CSV file (replace 'your_data.csv' with your actual file name)
df = pd.read_csv("data/rfm_data.csv")

def customer_insights():
    st.title("📊 Customer Insights")

    # Convert 'Date' column to datetime format
    df["Date"] = pd.to_datetime(df["Date"])

    # Analyze the most purchased product categories
    category_counts = df['Category'].value_counts().reset_index()
    category_counts.columns = ['Category', 'Count']

    # Analyze revenue by product
    product_revenue = df.groupby('productName')['Total_Revenue'].sum().reset_index()
    product_revenue = product_revenue.sort_values(by='Total_Revenue', ascending=False)

    # High revenue but low quantity products (e.g., Beef)
    high_revenue_low_qty = df.groupby('productName').agg(
        total_revenue=('Total_Revenue', 'sum'),
        total_items=('items', 'sum')
    ).reset_index()

    # Whole milk sales are high in quantity but low in revenue
    milk_sales = df[df['productName'].str.contains("whole milk", case=False, na=False)]

    # Customer spending levels
    spending_by_customer = df.groupby("Member_number")["Total_Revenue"].sum().reset_index()
    high_spending_customers = spending_by_customer[spending_by_customer["Total_Revenue"] > spending_by_customer["Total_Revenue"].quantile(0.75)]

    # Monthly and daily revenue trends
    df['Month'] = df['Date'].dt.month
    df['Weekday'] = df['Date'].dt.weekday

    # Monthly revenue
    monthly_revenue = df.groupby('Month')['Total_Revenue'].sum().reset_index()

    # Revenue by weekday
    weekday_revenue = df.groupby('Weekday')['Total_Revenue'].sum().reset_index()

    # Create charts in Streamlit

    # Product category distribution chart
    fig_category = px.bar(category_counts, x='Category', y='Count', title="Product Distribution by Category")
    st.plotly_chart(fig_category, use_container_width=True)

    # Product revenue chart
    fig_product_revenue = px.bar(product_revenue.head(10), x='productName', y='Total_Revenue', title="Revenue by Product")
    st.plotly_chart(fig_product_revenue, use_container_width=True)

    # High revenue but low quantity products chart
    fig_high_revenue_low_qty = px.scatter(high_revenue_low_qty, x='total_items', y='total_revenue', color='productName', 
                                          title="High Revenue but Low Quantity Products")
    st.plotly_chart(fig_high_revenue_low_qty, use_container_width=True)

    # Monthly revenue chart
    fig_monthly_revenue = px.line(monthly_revenue, x='Month', y='Total_Revenue', title="Revenue by Month")
    st.plotly_chart(fig_monthly_revenue, use_container_width=True)

    # Weekday revenue chart
    fig_weekday_revenue = px.line(weekday_revenue, x='Weekday', y='Total_Revenue', title="Revenue by Weekday")
    st.plotly_chart(fig_weekday_revenue, use_container_width=True)

    # Customer spending analysis chart
    fig_spending = px.box(spending_by_customer, y="Total_Revenue", title="Customer Spending Levels")
    st.plotly_chart(fig_spending, use_container_width=True)

    # High spending customer group
    st.write("High spending customer group:")
    st.write(high_spending_customers)

    # Detailed analysis of Whole Milk product
    st.write("Whole Milk Product Analysis:")
    st.write(milk_sales[['productName', 'Total_Revenue', 'items']].head())

    # Calculate correlation between revenue and product quantity
    df['Revenue_per_item'] = df['Total_Revenue'] / df['items']
    correlation = df[['Total_Revenue', 'items']].corr()

    # Correlation chart between revenue and quantity
    fig_correlation = px.scatter(df, x='items', y='Total_Revenue', 
                                title="Correlation between Product Quantity and Revenue",
                                labels={"items": "Product Quantity", "Total_Revenue": "Revenue"})
    st.plotly_chart(fig_correlation, use_container_width=True)

    # Display the correlation matrix
    st.write("Correlation between Revenue and Product Quantity:", correlation)

    # Calculate the time between customer purchases
    df['Prev_Purchase_Date'] = df.groupby('Member_number')['Date'].shift(1)
    df['Days_Between_Purchases'] = (df['Date'] - df['Prev_Purchase_Date']).dt.days

    # Purchase cycle time chart
    fig_purchase_cycle = px.histogram(df.dropna(subset=['Days_Between_Purchases']), 
                                      x='Days_Between_Purchases', 
                                      nbins=30, 
                                      title="Time Between Customer Purchases")
    st.plotly_chart(fig_purchase_cycle, use_container_width=True)

    # Add 'Hour' column to the DataFrame to track the hour of the day
    df['Hour'] = df['Date'].dt.hour

    # Revenue by hour of the day
    hourly_revenue = df.groupby('Hour')['Total_Revenue'].sum().reset_index()

    # Hourly revenue chart
    fig_hourly_revenue = px.line(hourly_revenue, 
                                x='Hour', 
                                y='Total_Revenue', 
                                title="Revenue by Hour of the Day")
    st.plotly_chart(fig_hourly_revenue, use_container_width=True)
