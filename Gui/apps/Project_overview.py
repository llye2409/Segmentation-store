import streamlit as st
from PIL import Image

def Project_overview():
    st.title("📊 Project Overview")

    st.markdown("""
    > This project is part of the **Graduation Project** for the program at the **Information Technology Center – University of Science, HCM City**.  
    The goal is to apply knowledge of **data analysis** and **machine learning** to solve real-world problems in the retail industry, specifically RFM.

    ---

    ### 🎯 **Project Overview**

    Store X is a retail store specializing in providing essential items such as **fresh food**, **beverages**, and **daily consumer products**.

    The project focuses on:
    - Increasing **revenue** by understanding customer behavior
    - Optimizing **personalized marketing strategies**
    - **Segmenting customers** for more effective service

    ---
    """)

    st.subheader("🧭 Project Process")

    image = Image.open("images/workflow.png")  # Replace with the actual path to your workflow image
    st.image(image, caption="Workflow - Customer Analysis and Segmentation Process", use_container_width=True)

    st.markdown("""
    ---
    #### 📝 Main Steps:
    1. **Data Collection & Cleaning**  
       - Handling duplicates, missing values, and standardizing formats

    2. **Consumer Behavior Analysis**  
       - Purchase frequency by product, revenue by month/week

    3. **Calculate RFM Scores**  
       - Recency (R), Frequency (F), Monetary (M)

    4. **Customer Segmentation**  
       - RFM Quartile Segmentation  
       - K-Means Clustering  
       - Hierarchical Clustering

    5. **Visualization & Interpretation**  
       - Treemaps, 3D charts, donut charts, dendrograms, scatter plots

    6. **Marketing Strategy Recommendations**  
       - Product suggestions, targeted approach for each customer group

    7. **Evaluation & Improvement**  
       - Measuring effectiveness & continuous optimization

    ---
    """)

    st.subheader("💡 Project Benefits")
    col1, col2 = st.columns(2)
    with col1:
        st.success("🎯 Target the right customer segments")
        st.success("📦 Optimize product assortment")
    with col2:
        st.info("🛍️ Personalize shopping experience")
        st.info("🤝 Build customer loyalty")

    st.markdown("---")
    st.caption("© 2025 - Student Project, Information Technology Center - University of Science, HCM City")
