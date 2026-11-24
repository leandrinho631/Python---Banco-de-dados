import psycopg2

def criar_conexao():
    try:
        con = psycopg2.connect(
            host = "localhost",
            port = "5432",
            database = "Mercadinho de Rua",
            user = "postgres",
            password = "leo1"
        )
        #print("Conexão feita")
        return con
    except Exception as e:
        print(f"O erro foi {e}")


