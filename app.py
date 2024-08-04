import streamlit as st
import pandas as pd
from models.recommendation_system import Applicant_Job, Job_Applicant
from models.model_lda import perform_lda
from models.model_tsne import perform_tsne

# Streamlit app title
st.title('Job and Applicant Recommendation System')

# Load data
@st.cache
def load_data():
    return pd.read_csv(data/r"C:\Users\ANTOH\my_streamlit_app\data\Experience (1).csv")
           pd.read_csv(data/r"C:\Users\ANTOH\my_streamlit_app\data\Combined_Jobs_Final.csv")
data = load_data()

# Sidebar for navigation
st.sidebar.title('Navigation')
selection = st.sidebar.radio("Choose an option", ["Applicant Job Recommendations", "Job Recommendations for Applicant", "LDA Visualization", "t-SNE Visualization"])

if selection == "Applicant Job Recommendations":
    st.subheader("Get Job Recommendations for a Job")
    job_id = st.number_input("Enter Job ID", min_value=1)
    if st.button("Get Recommendations"):
        recommendations = Applicant_Job(job_id)
        st.write(recommendations)

elif selection == "Job Recommendations for Applicant":
    st.subheader("Get Job Recommendations for an Applicant")
    applicant_id = st.number_input("Enter Applicant ID", min_value=1)
    if st.button("Get Recommendations"):
        recommendations = Job_Applicant(applicant_id)
        st.write(recommendations)

elif selection == "LDA Visualization":
    st.subheader("LDA Visualization")
    lda_result = perform_lda(data)
    st.write(lda_result)  # Adjust according to how you want to display the results

elif selection == "t-SNE Visualization":
    st.subheader("t-SNE Visualization")
    tsne_result = perform_tsne(data)
    st.write(tsne_result)  # Adjust according to how you want to display the results

