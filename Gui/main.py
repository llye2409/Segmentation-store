import streamlit as st
from streamlit_option_menu import option_menu
import apps.Seg_app as Seg_app
import apps.Project_overview
import apps.customer_Insights
import apps.modeling
import apps.dataset
import apps.marketing_strate
import apps.user_guide

# st.set_page_config(page_title="🎯 RFM Clustering App", layout="centered", page_icon="📊")
from lib.mylib import *


# Apply css
inject_custom_css()
import apps.Seg_app as Seg_app

with st.sidebar:
    selected = option_menu(
        menu_title="Main Menu",
        options=["Segmentation App", "Project Overview", "Dataset", "Customer Insights", "Modeling", "Marketing Strategy", "User Guide"],
        icons=['house', 'box-seam', 'graph-up', 'hdd-stack', 'envelope'],
        menu_icon="list", 
    )

    
    st.markdown("""
<hr>
<div style='font-size: 14px; color: gray; text-align:center'>
    <b>Version:</b> 1.0.0
</div>
""", unsafe_allow_html=True)



if selected == "Segmentation App":
    Seg_app.seg_app()
elif selected == "Project Overview":
    apps.Project_overview.Project_overview()
elif selected == "Dataset":
    apps.dataset.dataset()
elif selected == "Customer Insights":
    apps.customer_Insights.customer_insights()
    st.write("Nội dung trang Customer Insights")
elif selected == "Modeling":
    apps.modeling.modeling()
elif selected == "Marketing Strategy":
    apps.marketing_strate.marketing_strate()
elif selected == "User Guide":
    apps.user_guide.user_guide()



