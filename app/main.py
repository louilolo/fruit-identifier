import streamlit as st
from ultralytics import YOLO
import cv2 as cv
from PIL import Image

st.set_page_config(page_title="Fruit Identifier", page_icon=":apple::banana:") #definição de titulo e icon 
#cria uma sidebar que está relacionada ao menu de escolha (isso foi alterado arbitrariamente so para eu conhecer os comandos do streamlit)

# condicional para ver qual fruta o usuario escolheu e a partir dai exibir os textos corretos

st.title('Check the quality of your apple or banana :apple::banana:')
# Upload da imagem + formatos
img1 = st.file_uploader("Insira o arquivo desejado: ", type=('jpg', 'jpeg', 'png') )
# Verifica se a imagem foi carregada antes de exibi-la
col1, col2 = st.columns(2)

with col1:
    if img1 is not None:
        #exibição das imagens sem bounding boxes
        st.image(img1,
                caption="Uploaded Image",
                use_column_width=True)
with col2:
    if img1 is not None:
        uploaded_image = Image.open(img1)
        # Carregando o modelo
        model =  YOLO('C:\Repositórios\\fruit-identifier\\app\\best.pt') 
        results = model.predict(source = uploaded_image, conf = 0.5)
        boxes = results[0].boxes
        res_plotted = results[0].plot()[:, :, ::-1]
        st.image(res_plotted,
                caption="Detected Image",
                use_column_width=True)
        with st.expander("Detection Results"):
            for box in boxes:
                st.write(box.xywh)
        # esse trecho desenharia os retângulos na imagem (ainda nao entendi muito bem, teriamos que percorrer todo o arquivo gerado pelo modelo para fazer isso?)
        # cv.rectangle(img 1 ()...()...()...())
github_url = "https://github.com/louilolo/fruit-identifier/tree/main#fruit-identifier-apple-banana"
st.link_button("GitHub Repository", github_url)
