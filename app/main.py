import streamlit as st
from ultralytics import YOLO
import cv2 as cv
from PIL import Image

st.set_page_config(page_title="Fruit Identifier", page_icon=":apple:") #definição de titulo e icon 
#cria uma sidebar que está relacionada ao menu de escolha (isso foi alterado arbitrariamente so para eu conhecer os comandos do streamlit)
st.sidebar.title('Menu')
paginaSelecionada = st.sidebar.selectbox('Selecione a fruta que deseja testar a qualidade',['Maçã', 'Banana']) 

# condicional para ver qual fruta o usuario escolheu e a partir dai exibir os textos corretos
if paginaSelecionada == 'Maçã': 
    st.title('Check the quality of your apple :apple:')
    # Upload da imagem + formatos
    img1 = st.file_uploader("Insira o arquivo desejado: ", type=('jpg', 'jpeg', 'png') )
    # Verifica se a imagem foi carregada antes de exibi-la
    if img1 is not None:
        st.title(img1.type)
        #exibição das imagens sem bounding boxes
        st.image(img1)
        uploaded_image = Image.open(img1)
        # Carregando o modelo
        model =  YOLO('C:\Repositorios\\fruit-identifier\\app\\best.pt') 
        results = model.predict(source = uploaded_image, save = True)
        github_url = "https://github.com/louilolo/fruit-identifier/tree/main#fruit-identifier-apple-banana"
        st.link_button("GitHub Repository", github_url)
        # esse trecho desenharia os retângulos na imagem (ainda nao entendi muito bem, teriamos que percorrer todo o arquivo gerado pelo modelo para fazer isso?)
        # cv.rectangle(img 1 ()...()...()...())
elif paginaSelecionada == 'Banana':
     st.title('Check the quality of your banana :banana:')
     #para bananas repetir o mesmo codigo de cima ou usar tudo numa pagina so, tanto faz...
github_url = "https://github.com/louilolo/fruit-identifier/tree/main#fruit-identifier-apple-banana"
st.link_button("GitHub Repository", github_url)
