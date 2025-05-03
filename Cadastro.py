import streamlit as st
import pandas as pd
from datetime import date

def formatar_cpf(cpf):
    return f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}" if len(cpf) == 11 else cpf

def gravar_dados(nome, cpf, dt_nasc, genero, tipo):
    if nome and cpf.isdigit() and len(cpf) == 11 and genero and dt_nasc <= date.today():
        cpf_formatado = formatar_cpf(cpf)
        with open("clientes.csv", "a", encoding="utf-8") as file:
            file.write(f"{nome},{cpf_formatado},{dt_nasc},{genero},{tipo}\n")
        st.session_state["sucesso"] = True
    else:
        st.session_state["sucesso"] = False

st.set_page_config(
    page_title="Cadastro de clientes",
    page_icon="📚"
)

st.title("Cadastro de clientes")
st.divider()

nome = st.text_input("Digite o nome do cliente", key="nome_cliente")

cpf = st.text_input("Digite seu CPF", placeholder="Ex: 12345678900", max_chars=14)

dt_nasc = st.date_input(
    "Data de nascimento",
    format="DD/MM/YYYY",
    min_value=date(1900, 1, 1),
    max_value=date.today()
)

genero = st.radio("Escolha seu gênero", ["Masculino", "Feminino", "Prefiro não informar"])

tipo = st.selectbox("Tipo do cliente", ["Pessoa Jurídica", "Pessoa Física"])

btn_cadastrar = st.button("Cadastrar", on_click=gravar_dados,
                          args=[nome, cpf, dt_nasc, genero, tipo])

if btn_cadastrar:
    if st.session_state["sucesso"]:
        st.success("Cliente cadastrado com sucesso!", icon="✅")
    else:
        st.error("Houve algum problema no cadastro! Verifique os campos.", icon="❌")
