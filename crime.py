import streamlit as st
import pandas as pd

# Load data
df = pd.read_csv('chicago_crime_data.csv')
annual_trends = pd.read_csv('annual_trends.csv')
monthly_trends = pd.read_csv('monthly_trends.csv')
peak_hours = pd.read_csv('peak_hours.csv')
crime_types = pd.read_csv('crime_types.csv')
arrest_rates = pd.read_csv('arrest_rates.csv')
domestic_vs_non_domestic = pd.read_csv('domestic_vs_non_domestic.csv')

# Rename columns for compatibility with st.map
df.rename(columns={'Latitude': 'latitude', 'Longitude': 'longitude'}, inplace=True)

# Title and background
st.title('Chicago Crime Analysis Dashboard')
st.markdown("""
This dashboard provides insights into crime patterns in Chicago. 
Explore various aspects such as annual and monthly crime trends, peak crime hours, 
distribution of crime types, arrest rates, and a heatmap of crime hotspots.
""")

# Display data
st.subheader('Crime Data Sample')
st.write(df.head())

# Annual Crime Trends
st.subheader('Annual Crime Trends')
st.line_chart(annual_trends.set_index('Year'))

# Monthly Crime Trends
st.subheader('Monthly Crime Trends')
st.line_chart(monthly_trends.set_index('Month'))

# Peak Crime Hours
st.subheader('Crimes by Hour of the Day')
st.bar_chart(peak_hours.set_index('Hour'))

# Crime Types Distribution
st.subheader('Distribution of Crime Types')
st.bar_chart(crime_types.set_index('Crime Type'))

# Arrest Rates by Crime Type
st.subheader('Arrest Rates by Crime Type')
st.bar_chart(arrest_rates.set_index('Crime Type'))

# Domestic vs Non-Domestic Crimes
st.subheader('Domestic vs Non-Domestic Crimes')
st.bar_chart(domestic_vs_non_domestic.set_index('Domestic'))

# Display Heatmap
st.subheader('Crime Hotspots Heatmap')
st.map(df[['latitude', 'longitude']])


