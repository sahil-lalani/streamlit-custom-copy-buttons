import streamlit as st

text_to_copy = st.text_input("Hello, World!")

hosted_html_file = "https://silver-pavia-51.tiiny.site/"
iframe_url = f"{hosted_html_file}?copy={text_to_copy}"

if st.markdown(f'<iframe src="{iframe_url}"></iframe>', unsafe_allow_html=True):
    st.write("cool")
