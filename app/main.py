import streamlit as st

st.set_page_config(page_title="Fruit Identifier", page_icon=":apple:")

st.title('Fruit Identifier :apple: :banana:')

st.sidebar.title("Test")

# upload da imagem para predicao
uploaded_image = st.file_uploader("Upload a CSV")

git_url = "https://github.com/louilolo/fruit-identifier/tree/main#fruit-identifier-apple-banana"
st.link_button("GitHub Repository", git_url)
# st.link_button("Go to gallery", url)