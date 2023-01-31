import os
import sys
from time import sleep
from datetime import datetime

class Pessoa:
    def __init__(self, nome, cpf, vacina, data, lote):
        self.nome = nome
        self.cpf = cpf
        self.vacina = vacina
        self.data = data
        self.lote = lote

    def __str__(self):
        return f'\t- Nome: {self.nome}\n\t- CPF: {self.cpf}\n\t- Vacina: {self.vacina}\n\t- Data: {self.data}\n\t- Lote: {self.lote}'

pacientes = []

# --------------------------------------------------------------------------------------------------------------------------------

def cadastrar():
    os.system('cls')
    print("------------------------------------------------------------")
    print("                    Cadastro de Paciente                    ")
    print("------------------------------------------------------------\n")
    while True:
        # Informar o lote da vacina e se o usuario informou um letras 
        while True:
            nome = input("Informe o nome do paciente: ")
            if nome.isalpha():
                nome = str(nome)
                break
            else:
                print("\nNome inválido, informe apenas letras")

        # Validação do cpf
        while True:
            cpf = input("Informe o seu CPF no formato 'xxx.xxx.xxx-xx' sem '.' e '-': ")
            if cpf.isdigit() and len(set(cpf)) > 1:
                break
            else:
                print("\nPor favor, insira um CPF válido")

        # Vacina alicada (pode conter numeros e letras)
        vacina = str(input("Informe qual foi vacina aplicada: "))
        vacina = vacina.split()
        vacina = " ".join(vacina)

        # Data atual do cadastro do cliente
        data = datetime.now().strftime("%d/%m/%Y")
        print("Data atual:", data)
        sleep(0.2)

        # Informar o lote da vacina e se o usuario informou um numero interiro 
        lote = input("Informe o lote da vacina: ")
        if not (lote.isdigit() and int(lote) > 0):
            print("\nValor inválido! Por favor, tente novamente:")
            continue

        # Salvar dados
        pacientes.append(Pessoa(nome, cpf, vacina, data, lote))
        print("*** Usuário cadastrado ***\n")

        opcao = input("Você deseja continuar cadastrando (s/n)? ").upper()

        while opcao not in 'SN':
            print('\033[31mOPÇÃO INVÁLIDA! Digite apenas "S" ou "N"!\033[m')
            opcao = input("Você deseja continuar cadastrando (s/n)? ").upper()
            print()

        if opcao == 'S':
            os.system('cls')
            continue

        elif opcao == 'N':
            print(f'\033[31mEncerrando o Programa ...!\033[m')
            sleep(0.3)
            os.system('cls')
            menu()

# --------------------------------------------------------------------------------------------------------------------------------

def lista():
    os.system('cls')
    contador = 0
    print("------------------------------------------------------------")
    print("                     Lista de Pacientes                     ")
    print("------------------------------------------------------------\n")

    for paciente in pacientes:
        contador = contador + 1
        print(f'💉 - O paciente {paciente.nome} está cadastrado e possui as seguintes informações:')
        print(paciente)
        print('------------------------------------------------------------')

    voltar_menu()

# --------------------------------------------------------------------------------------------------------------------------------

def consultar():
    os.system('cls')
    print("------------------------------------------------------------")
    print("                     Consultar Paciente                     ")
    print("------------------------------------------------------------\n")
    contador = 0
    nome_pesquisa = input("Informe o nome do paciente que deseja pesquisar: ")

    pacientes_encontrados = [paciente for paciente in pacientes if nome_pesquisa.lower() in paciente.nome.lower()]

    if not pacientes_encontrados:
        print(f"\n\033[31mNenhum paciente com o nome '{nome_pesquisa}' foi encontrado.\033[m")
    else:
        for paciente in pacientes_encontrados:
            contador = contador + 1
            print(f'💉 - O paciente {paciente.nome} está cadastrado e possui as seguintes informações:')
            print(paciente)
            print('------------------------------------------------------------')
    
    opcao = input("Você deseja consultar outro paciente (s/n)? ").upper()

    while opcao not in 'SN':
        print('\033[31mOPÇÃO INVÁLIDA! Digite apenas "S" ou "N"!\033[m')
        opcao = input("Você deseja consultar outro paciente (s/n)? ").upper()
        print()
    
    if opcao == 'S':
        os.system('cls')
        consultar()
    
    elif opcao == 'N':
        print(f'\033[31mEncerrando o Programa ...!\033[m')
        sleep(0.3)
        os.system('cls')
        menu()

# --------------------------------------------------------------------------------------------------------------------------------

def excluir():
    os.system('cls')
    print("------------------------------------------------------------")
    print("                        Excluir Paciente                     ")
    print("------------------------------------------------------------\n")
    cpf = input("Informe o CPF do paciente que deseja excluir: ")
    achou = False
    for paciente in pacientes:
        if paciente.cpf == cpf:
            pacientes.remove(paciente)
            print(f'\033[32mPaciente com CPF "{cpf}" foi excluído com sucesso!\033[m')
            achou = True
            break
    if not achou:
        print(f'\033[31mNão existe paciente com CPF "{cpf}" no sistema!\033[m')

    opcao = input("Você deseja excluir outro paciente (s/n)? ").upper()

    while opcao not in 'SN':
        print('\033[31mOPÇÃO INVÁLIDA! Digite apenas "S" ou "N"!\033[m')
        opcao = input("Você deseja excluir outro paciente (s/n)? ").upper()
        print()
    
    if opcao == 'S':
        os.system('cls')
        consultar()
    
    elif opcao == 'N':
        print(f'\033[31mEncerrando o Programa ...!\033[m')
        sleep(0.3)
        os.system('cls')
        menu()

# --------------------------------------------------------------------------------------------------------------------------------

def sair():
    os.system('cls')
    print("------------------------------------------------------------")
    print("                         Saindo ...                         ")
    print("------------------------------------------------------------\n")
    print("\033[31mO sistema foi encerrado ... \033[m")
    quit()

# --------------------------------------------------------------------------------------------------------------------------------

def voltar_menu():
    opcao = str(input('Digite ("S") para voltar ao menu inicial? ').upper())
    
    while opcao not in 'S':
        print()
        opcao = input('\033[31mOPÇÃO INVÁLIDA!\033[m - Digite apenas "S" para voltar ao menu inicial! ').upper()
        print()

    if opcao == 'S':
        os.system('cls')
        menu()

# --------------------------------------------------------------------------------------------------------------------------------

options = {
    '1': cadastrar,
    '2': lista,
    '3': consultar,
    '4': excluir,
    '5': sair
}

# --------------------------------------------------------------------------------------------------------------------------------

def menu():
    while True:
        print("-------------------------------------")
        print("  Menu de aplicacão de vacinas:")
        print("      1 - Cadastrar Vacina")
        print("      2 - Listar Aplicacões")
        print("      3 - Consultar por Paciente")
        print("      4 - Excluir Paciente")
        print("      5 - Sair")
        print("-------------------------------------")

        opcao = input("Escolha uma opção: ")

        if opcao not in options:
            os.system('cls')
            print("\n\033[31mOPÇÃO INVÁLIDA!\033[m, escolha novamente.")
            continue

        options[opcao]()

# --------------------------------------------------------------------------------------------------------------------------------

menu()
