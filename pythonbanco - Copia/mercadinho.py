lista_produto = []
lista_cliente = []
lista_funcionario = []



def menu():
    print("1 - Cadastrar Cliente")
    print("2 - Lista de Clientes")
    print("3 - Registrar Produto")
    print("4 - Listar Produtos")
    print("5 - Cadastrar Funcionario")
    print("6 - Lista de Funcionario")




def cadastrar_cliente():
    nome_cliente = input("Digite seu nome de cliente: ")
    telefone = input("Digite seu número telefone: ")

    cliente = {
        nome_cliente: telefone
    }

    lista_cliente.append(cliente)





def cadastrar_funcionario():
    nome_fun = input("digite seu nome de funcionario: ")
    cargo = input("Digite  nome do cargo: ")

    funcionario = {
        nome_fun : cargo
    }

    lista_funcionario.append(funcionario)




def criando_login():
    login = ""
    senha = ""

    print("Bem vindo crie um login!")

    criando_login = input("Digite seu login: ")
    criando_senha = input("Digite sua senha: ")

    print("Login criado com sucesso!")
    print("Digite novamente para acessar o menu.")

    while login != criando_login or senha != criando_senha:
        login = input("Digite seu login: ")
        senha = input("Digite sua senha: ")
        
        
def registrar_produto():
    print("REGISTRADOR DE PRODUTOS:")
    print("O produto deve conter mais de 3 caracteres")
    nome_produto = input("Digite o nome do Produto")

    while len(nome_produto) <= 3:
        print("O produto deve conter mais de 3 caracteres")
        nome_produto = input("Digite o nome do Produto: ")

    preco_produto = float(input("Digite o preço do produto: "))

    produto = {
        nome_produto : preco_produto
    }

    lista_produto.append(produto)


criando_login()
registrar_produto()
cadastrar_cliente()
print(lista_cliente)
cadastrar_funcionario()
print(lista_funcionario)
print(lista_produto)
