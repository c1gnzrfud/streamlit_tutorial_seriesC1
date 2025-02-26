#Import the required Libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

import plotly.express as px

st.set_page_config(layout="wide")

# Functions for each of the pages
def home(uploaded_file):
    if uploaded_file:
        st.header('Begin exploring the data using the menu on the left')
    else:
        st.header('To begin please upload a file')

def data_summary():
    st.header('Statistics of Dataframe')
    st.write(df.describe())

def data_header():
    st.header('Header of Dataframe')
    st.write(df.head())

def displayplot():
    st.header('Plot of Data')
    
    fig, ax = plt.subplots(1,1)
    ax.scatter(x=df['Depth'], y=df['Magnitude'])
    ax.set_xlabel('Depth')
    ax.set_ylabel('Magnitude')
    
    st.pyplot(fig)

def interactive_plot():
    col1, col2 = st.columns(2)
    
    x_axis_val = col1.selectbox('Select the X-axis', options=df.columns)
    y_axis_val = col2.selectbox('Select the Y-axis', options=df.columns)

    plot = px.scatter(df, x=x_axis_val, y=y_axis_val)
    st.plotly_chart(plot, use_container_width=True)

def panos1():
    import streamlit as st
    import pandas as pd


    @st.cache
    def get_data():
        return pd.read_csv('https://datahub.io/core/gdp/r/gdp.csv')


    '# World GDP'

    df = get_data()

    min_year = int(df['Year'].min())
    max_year = int(df['Year'].max())

    countries = df['Country Name'].unique()

    '## By country'
    country = st.selectbox('Country', countries)
    df[df['Country Name'] == country]


    '## By year'
    year = st.slider('Year', min_year, max_year)
    df[df['Year'] == year]
    
    
    
    
# Add a title and intro text
st.title('Earthquake Data Explorer')
st.text('This is a web app to allow exploration of Earthquake Data')

# Sidebar setup
st.sidebar.title('Sidebar')
#
upload_file = ('https://github.com/c1gnzrfud/streamlit_tutorial_seriesC1/raw/main/data/kaggle_significant_earthquakes_database.csv')
######upload_file = st.sidebar.file_uploader('Upload a file containing earthquake data')

#Sidebar navigation
st.sidebar.title('Navigation')
options = st.sidebar.radio('Select what you want to display:', ['Home', 'Data Summary', 'Data Header', 'Scatter Plot', 'Fancy Plots','Panos Data'])

# Check if file has been uploaded
if upload_file is not None:
    df = pd.read_csv(upload_file)

# Navigation options
if options == 'Home':
    home(upload_file)
elif options == 'Data Summary':
    data_summary()
elif options == 'Data Header':
    data_header()
elif options == 'Scatter Plot':
    displayplot()
elif options == 'Fancy Plots':
    interactive_plot()
elif options == 'Panos Data':
    panos1()
    
