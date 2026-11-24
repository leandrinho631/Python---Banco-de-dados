from config.conect import criar_conexao

def inserir_employees(nome: str, cargo: str, cpf: str, email: str, password: str):
    try:
        con = criar_conexao()
        cursor = con.cursor()
        sql = "INSERT INTO funcionarios(nome, cargo, cpf, email, password) VALUES (%s,%s,%s,%s,%s)"
        cursor.execute(sql, (nome, cargo, cpf, email, password))
        con.commit()
        print("Funcionário cadastrado no sistema")
        
    except Exception as e:
        print(e)

    finally:
        cursor.close()
        con.close()
