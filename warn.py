import streamlit as st 
st.title("Three young's Job Portal 👔") 
# animation
st.balloons()
balloonsEnd_theme=st.snow()
st.subheader("We Provide Great Opportunities To Those Who Deserve!")
search_query = st.text_input("Enter job title or keywords:")
location = st.text_input("Enter location:") 
submit_button = st.button("Search 🧐") 
if submit_button: st.subheader("Search Results 🔁")
if search_query.lower() == "manager": st.write(" post remaining for Manager position.")
elif search_query.lower() == "designer": st.write("Designer position is available.")
elif search_query.lower() == "accountant": st.write("Vacancy for Accountant position is full.") 
elif search_query.lower() == "general manager": st.write("Vacancy for general manager position is full.")
elif search_query.lower() == "assistant accountant": st.write("Vacancy for Accountant position available")
else: st.write("No information available for the entered job title.") 
if_button=('st.subheader')
# Resume upload
st.subheader("Upload Resume")
resume_upload = st.file_uploader("Choose a file")
if resume_upload is not None:
 print ("opps!! upload resume")
submit_resume_button = st.button("Upload Resume 📄")
if submit_resume_button:
    if resume_upload is not None:
        st.write("Great! Your resume has been uploaded successfully.")
    else:
        st.write("Oops! Please choose a file to upload your resume.")
import streamlit as st

def main():
    st.button("Contact Us")
    
    st.write("Please fill out the form below to get in touch with us.")
    
    name = st.text_input("Name")
    email = st.text_input("Email")
    message = st.text_area("Message", height=2)
    
    if st.button("Submit"):
        # You can add your own logic here to handle the submission
        if name and email and message:
            st.success("Thank you for reaching out! We will get back to you soon.")
        else:
            st.error("Please fill out all the fields before submitting.")

if __name__ == "__main__":
    main()
