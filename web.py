import streamlit as st

st.write("""My first app""")
Image = st.file_uploader("Pick a file")
if Image is not None:
    st.write(Image)