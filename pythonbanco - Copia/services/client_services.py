from config.conect import criar_conexao

def inserir_usuario(nome: str, telefone: str, email: str, password: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()

        sql = "INSERT INTO cliente(nome, telefone, email, password) VALUES (%s, %s, %s, %s)"
        cursor.execute(sql, (nome, telefone, email, password))
        con.commit()
        print("Cliente cadastrado com sucesso!")

    except Exception as e:
        print(e)

    finally:
        cursor.close()
        con.close()


def login(email: str, password: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM cliente WHERE email=%s and password=%s"
        cursor.execute(sql, (email, password))
        user = cursor.fetchone()
        return user
    
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        con.close()


def list_client():
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "SELECT * FROM cliente"
        cursor.execute(sql)
        clientes = cursor.fetchall()
        
        for cliente in clientes:
            print(cliente[3])

    except Exception as e:
        print(e)
    finally:
        con.close()
        cursor.close()