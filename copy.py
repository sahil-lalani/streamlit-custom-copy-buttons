import streamlit as st

text_to_copy = st.text_input("Hello, World!")

hosted_html_file = "https://copy-button.streamlit.app/files/copy.html"
iframe_url = f"{hosted_html_file}?copy={text_to_copy}"

st.markdown(f'<iframe src="{iframe_url}"></iframe>', unsafe_allow_html=True)
