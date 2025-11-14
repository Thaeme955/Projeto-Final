# pip install streamlit requests
import streamlit as st
import requests

# Rode o streamlit:
# python -m streamlit run app.py

API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="Produtos", layout="wide")
st.title("Gerenciador de Produtos")

menu = st.sidebar.radio("Menu",
    ["Catálogo de Produtos", "Cadastrar Produto", "Deletar Produto", "Atualizar Produto"]
)


if menu == "Catálogo de Produtos":
    st.subheader("Todos os Produtos")
    
    response = requests.get(f"{API_URL}/produtos")
    
    if response.status_code == 200:
        produtos = response.json().get("produtos", [])
        if produtos:
            st.dataframe(produtos)
        else:
            st.info("Nenhum produto cadastrado ainda!")
    else:
        st.error("Erro ao conectar com a API.")


elif menu == "Cadastrar Produto":
    st.subheader("➕ Adicionar Produto")
    
    nome = st.text_input("Nome do produto")
    categoria = st.text_input("Categoria")
    preco = st.number_input("Preço", min_value=0.0, step=0.5)
    quantidade = st.number_input("Quantidade", min_value=0, step=1)

    if st.button("Salvar produto"):
        dados = {
            "nome": nome,
            "categoria": categoria,
            "preco": preco,
            "quantidade": quantidade
        }
        response = requests.post(f"{API_URL}/produtos", params=dados)

        if response.status_code == 200:
            st.success("Produto adicionado com sucesso!")
        else:
            st.error("Erro ao adicionar produto.")


elif menu == "Deletar Produto":
    st.subheader("Excluir Produto")
    
    id_produto = st.number_input("ID do produto a excluir", min_value=1, step=1)

    if st.button("Excluir"):
        response = requests.delete(f"{API_URL}/produtos/{id_produto}")

        if response.status_code == 200:
            data = response.json()
            if "erro" not in data:
                st.success("Produto excluído com sucesso!")
            else:
                st.error("Erro: Produto não encontrado.")
        else:
            st.error("Erro ao tentar excluir o produto.")

            
elif menu == "Atualizar Produto":
    st.subheader("Atualizar Quantidade do Produto")

    id_produto = st.number_input("ID do produto", min_value=1, step=1)
    nova_quantidade = st.number_input("Nova quantidade", min_value=0, step=1)

    if st.button("Atualizar"):
        response = requests.put(
            f"{API_URL}/produtos/id?id={id}&quantidade={nova_quantidade}"
        )

        if response.status_code == 200:
            data = response.json()

            if "erro" in data:
                st.error(data["erro"])
            else:
                st.success("Produto atualizado com sucesso!")
        else:
            st.error("Erro ao tentar atualizar o produto.")
