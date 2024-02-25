import streamlit as st
import pandas as pd

# Sample job data
job_data = pd.DataFrame({
    'Job Title': ['Data Scientist', 'Software Engineer', 'Product Manager'],
    'Company': ['ABC Inc.', 'XYZ Corp.', '123 Industries'],
    'Location': ['New York', 'San Francisco', 'Seattle'],
    'Salary': ['$100,000', '$120,000', '$110,000']
})

# Sidebar filters
location = st.sidebar.selectbox('Location', ['All'] + job_data['Location'].unique().tolist())
salary_range = st.sidebar.slider('Salary Range', 50000, 150000, (50000, 150000))

# Filter job data
filtered_jobs = job_data[(job_data['Location'] == location) & 
                         (job_data['Salary'].apply(lambda x: int(x.replace('$', '').replace(',', ''))) >= salary_range[0]) &
                         (job_data['Salary'].apply(lambda x: int(x.replace('$', '').replace(',', ''))) <= salary_range[1])]

# Display filtered job listings
st.write('## Job Listings')
st.write(filtered_jobs)
