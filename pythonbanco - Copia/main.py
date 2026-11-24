
from services.client_services import inserir_usuario, login, list_client
from services.employess import inserir_employees
import pwinput


while True:
    print("1 - Cadastrar cliente \n 2 - Entrar cliente \n 3 - Cadastrar funcionário \n 4 Sair \n 5 - Listar clientes")
    opcao = int(input("Digite a opção: "))

    if opcao == 1:
        nome = input("Digite seu nome: ")
        telefone = input("Digite seu telefone: ")
        email = input("Digite seu email: ")
        password = pwinput.pwinput("Digite sua senha: ")
        inserir_usuario(nome, telefone, email, password)

    elif opcao == 2:
        email = input("Digite seu email: ")
        password = pwinput.pwinput("Digite sua senha: ")
        clinte_logged = login(email, password)
        if clinte_logged:
            print(clinte_logged)
        else:
            print("Email ou senha inválidos")
    
    elif opcao == 3:
        nome = input("Digite seu nome: ")
        cargo = input("Cargo em que atua na empresa: ")
        cpf = input("CPF: ")
        email = input("Digite seu email: ")
        senha = pwinput.pwinput("Digite sua senha: ")
        inserir_employees(nome, cargo, cpf, email, senha)
        
    elif opcao == 4:
        break

    elif opcao == 5:
        list_client()
    else:
        print("Digite uma opção válida")


