
import streamlit as st

# Configure the webpage
st.set_page_config(page_title="AISE Deployment Demo")

# Application heading
st.title("AI-Enabled Software Engineering")

st.header("Cloud Deployment Demonstration")

st.write(
    "This application is running as a cloud deployment demo."
)

# Take input from the user
name = st.text_input("Enter your name")

# Submit button
if st.button("Submit"):
    if name.strip():
        st.success(
            f"Hello, {name}! Your application is working."
        )
    else:
        st.warning("Please enter your name.")

# Deployment information
st.divider()

st.subheader("Deployment Check")

st.write(
    "If you can see this page and use the button, "
    "the application is running."
)
