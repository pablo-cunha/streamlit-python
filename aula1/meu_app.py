import streamlit as st
import pandas as pd

# Configurando a página do streamlit
st.set_page_config(page_title="Meu Site Streamlit")

# Colocando elementos na página (Containers)
with st.container():
    # Subtítulo
    st.subheader("Meu primeiro site com o Streamlit")

    # Título
    st.title("Dashboard de Contratos")

    # Texto
    st.write("Informações sobre os contratos fechados ao longo de maio")

# Função para carregar dados
# Utilizando decorator
@st.cache_data
def carregar_dados():
    tabela = pd.read_csv("./dados/resultados.csv")
    return tabela

# Container de dados
with st.container():
    # Separador
    st.write("---")

    # Botão interativo
    qt_dias = st.selectbox("Selecione o período", ["7 dias", "15 dias", "30 dias"])
    num_dias = int(qt_dias.replace("dias", ""))

    # Criando dataframe e aplicando o período selecionado pelo botão interativo
    dados = carregar_dados()
    dados = dados[-num_dias:]

    # Gráfico de área
    st.area_chart(dados, x= "Data", y= "Contratos")