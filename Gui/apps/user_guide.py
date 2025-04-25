import streamlit as st

def user_guide():
    # Title
    st.title("User Guide for RFM Clustering App")

    # Introduction
    st.write("""
    Welcome to the **RFM Clustering App**! This app provides a set of tools to perform RFM (Recency, Frequency, and Monetary) analysis on customer data. It helps you segment customers based on their behavior, analyze the data, build models, and strategize marketing campaigns.
    
    Below is a guide to each section of the app and how to use them effectively.
    """)

    # Sections of the app
    st.header("Main Sections")
    st.write("""
    1. **Segmentation App**:
        - This is where you can upload your customer data, perform RFM segmentation, and visualize the results.
        - Users can choose features like Recency, Frequency, and Monetary to generate customer segments.

    2. **Project Overview**:
        - Provides an overview of the project, including goals, methodology, and high-level insights.

    3. **Dataset**:
        - This section allows you to upload and view your dataset. You can inspect the data, check for missing values, and perform some preliminary data preprocessing.

    4. **Customer Insights**:
        - Here you can explore and analyze customer insights. This section provides key visualizations and metrics that help understand customer behavior based on RFM.

    5. **Modeling**:
        - You can use various machine learning algorithms to build models on the segmented customer data. This helps predict customer behavior and classify customers into different groups.

    6. **Marketing Strategy**:
        - Based on the customer segmentation and insights, you will receive tailored marketing strategies to target each customer group efficiently.

    7. **User Guide**:
        - You are currently here! This guide explains how to navigate and use the app.

    """)

    # Navigation Tips
    st.header("Navigation Tips")
    st.write("""
    - Use the **sidebar** to navigate between different sections of the app.
    - Each section has specific instructions on how to interact with the content.
    - If you are unsure about anything, refer to this **User Guide** for clarification.
    - Make sure to check the **project overview** before starting any data analysis to understand the context and objectives of the project.

    """)

    # Troubleshooting Section
    st.header("Troubleshooting")
    st.write("""
    - **Issue**: The app doesn't load my dataset.
    - **Solution**: Ensure that the dataset is in the correct format (e.g., CSV, Excel). If the issue persists, check the file for any inconsistencies or missing values.
    
    - **Issue**: I can't see the customer segments after performing segmentation.
    - **Solution**: Verify that the dataset contains valid RFM features (Recency, Frequency, Monetary) and that the data is properly preprocessed. Ensure that you are using appropriate segmentation criteria.
    
    - **Issue**: I don't understand the Marketing Strategy suggestions.
    - **Solution**: The app generates strategies based on customer segments. Review the "Customer Insights" and "Segmentation App" sections for a better understanding of the customer groups before applying the marketing strategy.
    """)

    # Conclusion
    st.write("""
    If you have any further questions or need assistance, feel free to reach out to our support team. We hope this app helps you gain valuable insights into customer behavior and optimize your marketing efforts.

    Thank you for using the **RFM Clustering App**! 🎯
    """)

# To use this function, just call `user_guide()` when the "User Guide" option is selected in the sidebar.
