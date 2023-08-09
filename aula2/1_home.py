import streamlit as st
import pandas as pd
import datetime

# Usando session state para que as outras páginas também tenham acesso ao dataframe
if "data" not in st.session_state:
    # Criando dataframe e filtrando jogadores com contrato ativo
    # E com contratos com valores maiores que zero
    dados = pd.read_csv("./dados/CLEAN_FIFA23_official_data.csv", index_col=0)
    dados = dados[dados["Contract Valid Until"] >= datetime.today().year]
    dados = dados[dados["Value(£)"] > 0]
    dados = dados.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = dados

# Usando '#' como notação markdown para título
st.write("# FIFA OFFICIAL DATASET!")

st.markdown(
    """
    O conjunto de dados
    de jogadores de futebol de 2017 a 2023 fornece informações
    abrangentes sobre jogadores de futebol profissionais.
    O conjunto de dados contém uma ampla gama de atributos, incluindo dados
    do jogador, características físicas, estatísticas de jogo, detalhes dos clubes.

    Com mais de 17.000 registros, este conjunto de dados oferece um recurso valioso para
    analistas de futebol, pesquisadores e entusiastas interessados em explorar vários
    aspectos do mundo do futebol, pois permite estudar atributos de jogadores, métricas de desempenho,
    avaliação do mercado, análise de clubes, posicionamento de jogadores e desenvolvimento
    do jogador ao longo do tempo.
    """)