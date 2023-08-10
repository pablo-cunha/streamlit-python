import streamlit as st

# Configurações da página
st.set_page_config(
    page_title="Jogadores",
    page_icon="🏃‍♂️",
    layout="wide"
)
# Session state
dados = st.session_state["data"]

# Definindo clubes, usando 'value_counts().index' para evitar repetições
clubes = dados["Club"].value_counts().index

# Criando elemento selectbox (controlador) e armazenando o clube selecionado na
# Variável 'clube'
clube = st.sidebar.selectbox("Clube", clubes)

# Definindo lista de jogadores e evitando repetições possíveis
dados_jogadores = dados[dados["Club"] == clube]
jogadores = dados_jogadores["Name"].value_counts().index

# Elemento selectbox (controlador) e armazenando jogador na variável 'jogador'
jogador = st.sidebar.selectbox("Jogador", jogadores)

# Armazenando estatísticas do jogador selecionado
jogador_status = dados[dados["Name"] == jogador].iloc[0]

# Exibindo no dashboard principal os dados do jogador selecionado
# Foto
st.image(jogador_status["Photo"])

# Nome (usando 'f' e chaves para passar uma variável como parâmetro)
st.title(f"{jogador_status['Name']}")

# Clube
st.markdown(f"**Clube:** {jogador_status['Club']}")

# Posição
st.markdown(f"**Posição:** {jogador_status['Position']}")

# Usando disposição entre colunas
col1, col2, col3, col4 = st.columns(4)
col1.markdown(f"**Idade:** {jogador_status['Age']}")
col2.markdown(f"**Altura:** {jogador_status['Height(cm.)'] / 100}")
col3.markdown(f"**Peso:** {jogador_status['Weight(lbs.)'] * 0.453:.2f}")

# Segunda parte dos dados (barra de overall e valores)
st.divider()
st.subheader(f"Overall {jogador_status['Overall']}")
st.progress(int(jogador_status['Overall']))

# Valores
# Elemento metric é melhor para exibir métricas
# ':,' formata como milhar
col1, col2, col3 = st.columns(3)
col1.metric(label="Valor de mercado", value=f"£{jogador_status['Value(£)']:,}")
col2.metric(label="Remuneração Semanal", value=f"£{jogador_status['Wage(£)']:,}")
col3.metric(label="Valor de rescisão", value=f"£{jogador_status['Release Clause(£)']:,}")