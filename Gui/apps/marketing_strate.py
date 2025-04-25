import streamlit as st
from PIL import Image
import matplotlib.pyplot as plt

def marketing_strate():
    # App Title
    st.title("Marketing Strategies for Customer Segments")

    # Introduction to the app
    st.write("""
    This app helps you explore appropriate marketing strategies for different customer segments. These segments are classified based on their shopping behavior, frequency, and spending value.
    """)

    # Add an illustrative image
    image = Image.open("images/marketing_strategy.png")  # Change path if needed
    st.image(image, caption="Marketing Strategies for Customer Segments", use_container_width=True)

    # Content for strategies for each group
    strategies = {
        "💎 Group 0 - Loyal": {
            "traits": "Prioritize retention with exclusive offers, personalized shopping experience. Leverage frequent buying behavior on Tuesdays and Fridays to drive sales. Apply loyalty programs and upsell suitable products based on spending history.",
            "desc": "Loyal customers, frequent buyers, recently returned, high value.",
            "strategy": """
            - Provide special offers and exclusive discounts.
            - Create loyalty programs and reward points.
            - Offer upsell and cross-sell products based on purchase history.
            - Focus on reaching out on Tuesdays and Fridays to optimize shopping habits.
            """
        },
        "🌟 Group 1 - Regular": {
            "traits": "Increase frequency and order value with product combos, attractive offers, and seasonal promotions. Suggest personalized products and focus outreach on mid and end of the week to optimize shopping behavior.",
            "desc": "Regular customers, buy less, have not returned in a while, low value.",
            "strategy": """
            - Create attractive product combos with special offers.
            - Apply seasonal promotions and special events.
            - Send emails and promotional notifications mid-week and weekends to increase shopping frequency.
            - Leverage upsell strategies for this group to increase order value.
            """
        },
        "⚠️ Group 2 - At-risk": {
            "traits": "Reactivate with special offers for the next purchase. Remind them of past good experiences, introduce new products or personalized promotions. Leverage buying habits on Tuesdays and Fridays to bring them back.",
            "desc": "Once valuable customers (high spend and frequent) but have not returned for a while (likely to churn).",
            "strategy": """
            - Send promotional messages or special offers for their next purchase.
            - Remind customers of their past positive experiences and introduce new products.
            - Focus on reactivating customers on Tuesdays and Fridays.
            - Personalize the message to attract their return.
            """
        },
        "🚫 Group 3 - No Potential": {
            "traits": "Optimize costs by limiting direct outreach. Use low-cost marketing channels such as automated emails, passive remarketing. Can be ignored if resources are limited.",
            "desc": "Churned customers, minimal purchases, low spending.",
            "strategy": """
            - Maintain passive remarketing strategies through emails or social media channels.
            - Reduce marketing costs for this group by limiting direct outreach.
            - Do not prioritize resources for this group if resources are limited.
            """
        }
    }

    # Display marketing strategies for each group
    for group, details in strategies.items():
        st.subheader(group)
        st.write(f"**Description**: {details['desc']}")
        st.write(f"**Marketing Strategy**: {details['strategy']}")

        # Plot a simple chart illustrating the strategy (e.g., evaluating the priority level for each strategy)
        fig, ax = plt.subplots(figsize=(5, 3))
        ax.barh([group], [1], color="skyblue")  # Simple bar chart to illustrate
        ax.set_xlabel('Priority Level')
        ax.set_title(f'Marketing Strategy for {group}')
        st.pyplot(fig)

    # Conclusion
    st.write("""
    ### Conclusion
    Marketing strategies are crucial for optimizing sales performance. Each customer group requires a distinct approach based on their characteristics and behavior. Implementing these strategies will help businesses maximize profits and maintain long-lasting relationships with customers.
    """)
