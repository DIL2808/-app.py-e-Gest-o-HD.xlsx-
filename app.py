
import streamlit as st
import pandas as pd

# Carregar os dados da planilha
df = pd.read_excel("Gestão HD.xlsx", sheet_name="Planilha1", engine="openpyxl")

# Título do aplicativo
st.title("Gestão de Sessões de Hemodiálise")

# Seção de cadastro de nova sessão
st.header("Cadastrar Nova Sessão")

with st.form("form_sessao"):
    paciente = st.text_input("Nome do Paciente")
    tipo_acesso = st.selectbox("Tipo de Acesso Vascular", ["Fístula Arteriovenosa", "Cateter Venoso Central", "Prótese", "Outro"])
    hospital = st.text_input("Hospital")
    medico = st.text_input("Nome do Médico")
    tecnico = st.text_input("Nome do Técnico de Enfermagem")
    data_hd = st.date_input("Data da Sessão")
    tempo_hd = st.text_input("Tempo de HD")
    pa1 = st.text_input("PA 1º")
    pa2 = st.text_input("PA 2º")
    pa3 = st.text_input("PA 3º")
    pa4 = st.text_input("PA 4º")
    pa5 = st.text_input("PA 5º")
    submitted = st.form_submit_button("Salvar Sessão")

    if submitted:
        st.success("Sessão registrada com sucesso!")

# Seção de histórico de sessões
st.header("Histórico de Sessões")

# Filtros
filtro_paciente = st.text_input("Filtrar por paciente")
filtro_acesso = st.selectbox("Filtrar por tipo de acesso", ["Todos", "Fístula Arteriovenosa", "Cateter Venoso Central", "Prótese", "Outro"])

# Aplicar filtros
df_filtrado = df.copy()
if filtro_paciente:
    df_filtrado = df_filtrado[df_filtrado["Nº"].astype(str).str.contains(filtro_paciente)]
if filtro_acesso != "Todos" and "Local" in df_filtrado.columns:
    df_filtrado = df_filtrado[df_filtrado["Local"].astype(str).str.contains(filtro_acesso, case=False)]

# Exibir tabela filtrada
st.dataframe(df_filtrado)
