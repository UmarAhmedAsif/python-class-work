import streamlit as st

# Job search form
st.title("Job Portal")
search_query = st.text_input("Enter job title or keywords:")
location = st.text_input("Enter location:")
submit_button = st.button("Search")

# Job listings
if submit_button:
    st.subheader("Search Results")
    # Perform job search based on search_query and location
    # Display job listings
    
# Resume upload
st.subheader("Upload Resume")
resume_upload = st.file_uploader("Choose a file")

if resume_upload is not None:
    # Process the uploaded resume
    st.write("Resume uploaded )
