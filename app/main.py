import streamlit as st
from ultralytics import YOLO
import cv2 as cv

st.set_page_config(page_title="Fruit Identifier", page_icon=":apple:")

st.title('Fruit Identifier :apple: :banana:')

st.sidebar.title("Test")

# upload da imagem para predicao
image = st.file_uploader("Upload a CSV")

# Carregar o modelo e fazer a predicao
model = YOLO("/content/runs/detect/train5/weights/best.pt")
results = model.predict(source=image)

# Desenhar o retangulo gerado na predicao do modelo
cv.rectangle(img,(384,0),(510,128),(0,255,0),3)

# Exibir imagem com bounding box da predição
st.image(img)

github_url = "https://github.com/louilolo/fruit-identifier/tree/main#fruit-identifier-apple-banana"
st.link_button("GitHub Repository", github_url)
