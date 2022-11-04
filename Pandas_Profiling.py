from st_aggrid import AgGrid
import streamlit as st
import pandas as pd 
import pandas_profiling
from streamlit_pandas_profiling import st_profile_report
from pandas_profiling import ProfileReport
from  PIL import Image

st.set_page_config(layout='wide') #Choose wide mode as the default setting

#Add a logo (optional) in the sidebar
logo = Image.open('https://github.com/nvamsimohan/streamlit/blob/main/DDSA%20White1.jpg')
st.sidebar.image(logo,  width=120)

#Add the expander to provide some information about the app
with st.sidebar.expander("About the App"):
     st.write("""
        This data profiling App was built by Sharone Li using Streamlit and pandas_profiling package. You can use the app to quickly generate a comprehensive data profiling and EDA report without the need to write any python code. \n\nThe app has the minimum mode (recommended) and the complete code. The complete code includes more sophisticated analysis such as correlation analysis or interactions between variables which may requires expensive computations. )
     """)

#Add an app title. Use css to style the title
st.markdown(""" <style> .font {                                          
    font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;} 
    </style> """, unsafe_allow_html=True)
st.markdown('<p class="font">Import your data and generate a Pandas data profiling report easily...</p>', unsafe_allow_html=True)
