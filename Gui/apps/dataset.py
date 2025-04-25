import streamlit as st
from pathlib import Path


def dataset():
    st.title("📂 Dataset Overview")

    st.markdown("""
    This project uses real transaction data from a retail store during the period **2014 - 2015**. 
    The goal is to analyze customer behavior and segmentation based on this data.

    #### ✅ **Data Structure**
    The data is divided into 3 main tables:

    1. **Transactions.csv**  
        - `Member_number`: Customer ID  
        - `Date`: Transaction date  
        - `itemDescription`: Product name  
        - `Category`: Product category  
        - `price`: Product price  

    2. **Customer.csv**  
        - `Member_number`: Customer ID  
        - `birth_year`: Birth year  
        - `gender`: Gender (if available)

    3. **Product.csv**  
        - `productId`: Product ID  
        - `productName`: Product name  
        - `Category`: Product category  

    #### 🧮 **Calculated Metrics**
    - **Total Revenue**: Total transaction amount per purchase  
    - **Frequency**: Number of purchases per customer  
    - **Recency**: Days since the last purchase  
    - **Monetary**: Total spending  

    #### 🧾 **Data Sample Images**
    """)
    

    # Create Profiling Report
    html_file = Path("images/df_products_report.html").read_text()

    # Embed the HTML report in Streamlit
    st.components.v1.html(html_file, height=1000)

    st.info("📌 Note: The data has been cleaned, missing values handled, and normalized before analysis.")
