from fastapi import FastAPI
import funcao
import requests

app = FastAPI(title="Gerenciador de produtos")

@app.get("/")
def home():
    return { "mensagem": "Bem-vindo ao gerenciador de produtos"}

@app.post("/produtos")
def adicionar_produto(nome: str, categoria: str, preco: float, quantidade: int):
    funcao.adicionar_produto(nome, categoria, preco, quantidade)
    return {"mensagem": "Produto cadastrado com sucesso!"}


@app.get("/produtos")
def listar_produto():
    produtos = funcao.listar_produto()
    listar = []
    for linha in produtos:
        listar.append(
            {
                "id": linha[0],
                "nome": linha[1],
                "categoria": linha[2],
                "preco": linha[3],
                "quantidade": linha[4],
            }
        )
    return {"produtos": listar}

@app.delete("/produtos/{id}")
def deletar_produtos(id: int):
    produtos = funcao.buscar_produtos(id)
    if produtos:
        funcao.deletar_produtos(id)
        return {"mensagem": "Produto excluido com sucesso!"}
    else:
        return{"erro": "Produto não encontrado"}
    
    
    
@app.put("/produtos/id")
def atualizar_produtos( id: int ,quantidade: int):
    produtos_existente = funcao.buscar_produtos(id)

    if produtos_existente:
        funcao.atualizar_produtos(id, quantidade)
        return{"mensagem": "Produtos atualizados com sucessso!"}
    else:
        return{"erro": "Podutos não encontrado"}