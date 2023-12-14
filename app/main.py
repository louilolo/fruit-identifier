import streamlit as st
from ultralytics import YOLO
import cv2 as cv
from PIL import Image

st.set_page_config(page_title= "Fruit Identifier", page_icon= ":apple:")
logo = "paysandu.jpg"
logo_image = Image.open(logo)
resized_logo = logo_image.resize((700, 200)) # largura, altura
st.image(resized_logo)  
st.markdown(
            """
            <div style='background-color: #272731; padding: 10px; border-radius: 5px;'> <!-- setando cor da div e estilizando ela (bordas, cores...) -->
                <h3> Apresentação do trabalho: </h3> <!-- declaração de subtitulo (h3) -->
                <p>O fruit identifier foi pensado durante a disciplina de Projetos de Engenharia 2, na Universidade Federal do Pará (UFPA). No período letivo 2023.4 a ideia foi
                abordar a inteligência artifical e as suas aplicações.</p> <!-- declaração de parágrafo -->
                <p>Partindo disso, a equipe formada por Caio Santos, Desirée Xavier, Dhomini Bezerra, Giulia Sena e Ingrid Ramos decidiu seguir a linha de visão computacional
                para trazer ao ambiente acadêmico uma contribuição e aplicar os conhecimentos adquiridos na disciplina, criando um modelo de reconhecimento de frutas frescas ou passadas.</p>
                <h3> Modo de utilização da ferramenta: </h3> 
                <p>Para você conseguir utilizar a ferramenta é preciso fazer upload de uma imagem de banana ou maçã, pois foram essas as frutas escolhidas para basear o modelo.</p>
                <p>É importante que a imagem de upload esteja nos formatos indicados pela plataforma.</p>
                <p>As classificações são: Fresh Banana -> banana fresca ; Rotten Banana -> Banana estragada ; Fresh apple -> Maçã fresca ; Rotten Apple -> Maçã estragada</p>
            </div>
            """,
            unsafe_allow_html=True
        ) #basicamente esse trecho faz a criação de uma div que comporta subtitulos e paragrafos discorrendo sobre o trabalho



st.title('Verifique a qualidade da sua fruta: :apple::banana:') #definição de título e icons da página
img1 = st.file_uploader("Faça upload da imagem da fruta que deseja checar: ", type=('jpg', 'jpeg', 'png') ) # Upload da imagem + formatos


col1, col2 = st.columns(2) # Criação de duas colunas para exibição das imagens

with col1:
    if img1 is not None: #exibição das imagens sem bounding boxes
        st.image(img1,
                caption="Imagem enviada",
                use_column_width=True) 
with col2:
    if img1 is not None: # Verifica se a imagem foi carregada antes de exibi-la
        uploaded_image = Image.open(img1) 
        model =  YOLO('C:\\Users\\caiot\\Downloads\\best.pt') # Carregando o modelo
        results = model.predict(source = uploaded_image, conf = 0.6) # definindo a imagem de upload para predição e precisão mínima para fazê-la 
        boxes = results[0].boxes
        res_plotted = results[0].plot()[:, :, ::-1]
        st.image(res_plotted,
                caption="Detecção realizada",
                use_column_width=True)
        with st.expander("Resultados da detecção"): # Expansão para mostrar os resultados da detecção em formato de caixas
            for box in boxes:
                st.write(box.xywh)
github_url = "https://github.com/louilolo/fruit-identifier/tree/main#fruit-identifier-apple-banana" # cria uma variavel c link para o trabalho no github
st.link_button("GitHub Repository", github_url) # botao que leva para o github da equipe
