from conexao import conector 

def criar_tabela():
    conexao,cursor = conector()
    if conexao:
        try:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS produtos (
                id SERIAL PRIMARY KEY,
                nome TEXT NOT NULL,
                categoria TEXT NOT NULL,
                preco REAL NOT NULL,
                quantidade INTEGER
                )
                """)
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao criar a tabela {erro}")
        finally:
            cursor.close()
            conexao.commit()
#criar_tabela()

def adicionar_produto(nome, categoria, preco, quantidade):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "INSERT INTO produtos (nome, categoria, preco, quantidade) VALUES (%s, %s, %s, %s)",
                (nome, categoria, preco, quantidade)
                )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao adicionar o filme {erro}")
        finally:
            cursor.close()
            conexao.commit()

#adicionar_produto("contra filé", "carne vermelha", 50.00, 25)

def listar_produto():
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos ORDER BY id"
            )
            return cursor.fetchall()
        except Exception as erro:
            print(f"Erro ao listar os produtos: {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()

#listar_produto()
  
def atualizar_produtos(preco, id,):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "UPDATE produtos SET preco = %s WHERE id = %s",
                (preco, id)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Erro ao atualizar o produto: {erro}")
        finally:
            cursor.close()
            conexao.close()

#atualizar_produtos(40, 1)


def deletar_produtos(id):
    conexao,cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "DELETE FROM produtos WHERE id = %s",
                (id,)
            )
            conexao.commit()
        except Exception as erro:
            print(f"Produto removido: {erro}")
        finally:
            cursor.close()
            conexao.close()

#deletar_produtos(1)


def buscar_produtos(id):
    conexao, cursor = conector()
    if conexao:
        try:
            cursor.execute(
                "SELECT * FROM produtos WHERE id = %s",
                (id,)
            )
            return cursor.fetchone()
        except Exception as erro:
            print(f"Erro ao buscar produto: {erro}")
            return[]
        finally:
            cursor.close()
            conexao.close()

buscar_produtos(2)

                           
                           
                           
                           
            

           