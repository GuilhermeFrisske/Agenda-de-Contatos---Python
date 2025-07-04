# Imports utilizados
import json
import os
import re
import csv

# Os contatos serão salvos no arquivo contatos.json
ARQUIVO = "contatos.json"

#Importação de csv(Command Separed Values )
def exportar_para_csv(contatos):
    with open("contatos.csv", "w", newline='', encoding="utf-8") as csvfile:
        campos = ["Nome", "Telefone", "Email"]
        writer = csv.DictWriter(csvfile, fieldnames=campos)

        writer.writeheader()
        for nome, dados in contatos.items():
            writer.writerow({"Nome": nome, "Telefone": dados["telefone"], "Email": dados["email"]})
    print("Contatos exportados para 'contatos.csv'.")

# Carrega os contatos do arquivo
def carregar_contatos():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

# Salva os contatos no arquivo
def salvar_contatos(contatos):
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(contatos, f, indent=4)

# Valida o telefone
def validar_telefone(telefone):
    padrao = r'^\(?\d{2}\)?\s?\d{4,5}-?\d{4}$'
    return re.match(padrao, telefone) is not None

# Valida o e-mail
def validar_email(email):
    padrao = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(padrao, email) is not None

# Adiciona um novo contato
def adicionar_contatos(contatos):
    nome = input("Nome: ").strip()
    sobrenome = input("Sobrenome: ").strip()
    nome_completo = f"{nome} {sobrenome}"

    if nome_completo in contatos:
        print("Contato já existe. Use a opção de atualização de contato.")
        return

    while True:
        telefone = input("Telefone: ").strip()
        if validar_telefone(telefone):
            break
        else:
            print("Telefone inválido. Tente novamente.")

    while True:
        email = input("Email: ").strip()
        if validar_email(email):
            break
        else:
            print("Email inválido. Tente novamente.")

    contatos[nome_completo] = {"telefone": telefone, "email": email}
    print("Contato adicionado com sucesso!")

# Lista todos os contatos
def lista_contatos(contatos):
    if not contatos:
        print("Nenhum contato encontrado.")
    else:
        print("\nLista de Contatos:")
        print("=" * 40)
        for nome_completo, dados in contatos.items():
            print(f"Nome     : {nome_completo}")
            print(f"Telefone : {dados['telefone']}")
            print(f"Email    : {dados['email']}")
            print("-" * 40)

# Atualiza um contato existente
def atualizar_contato(contatos):
    nome = input("Digite o nome completo do contato que deseja atualizar: ").strip()
    if nome in contatos:
        while True:
            telefone = input("Novo Telefone: ").strip()
            if validar_telefone(telefone):
                break
            else:
                print("Telefone inválido. Tente novamente.")

        while True:
            email = input("Novo Email: ").strip()
            if validar_email(email):
                break
            else:
                print("Email inválido. Tente novamente.")

        contatos[nome] = {"telefone": telefone, "email": email}
        print("Contato atualizado com sucesso!")
    else:
        print("Contato não encontrado.")

# Exclui um contato
def excluir_contato(contatos):
    nome = input("Digite o nome completo do contato que deseja excluir: ").strip()
    if nome in contatos:
        escolha = input("Tem certeza que deseja apagar o contato? (S/N): ").strip().upper()
        if escolha == "S":
            del contatos[nome]
            print("Contato excluído com sucesso.")
        elif escolha == "N":
            print("Contato não foi apagado.")
        else:
            print("Opção inválida. Contato não foi excluído.")
    else:
        print("Contato não encontrado.")

# Busca contatos por nome (ou parte do nome)
def busca_contato_usuário(contatos):
    busca = input("Escreva o nome do usuário que deseja buscar: ").strip().lower()
    encontrados = {nome: dados for nome, dados in contatos.items() if busca in nome.lower()}

    if encontrados:
        print("\nContatos encontrados:")
        for nome, dados in encontrados.items():
            print(f"\nNome     : {nome}")
            print(f"Telefone : {dados['telefone']}")
            print(f"Email    : {dados['email']}")
    else:
        print("Nenhum contato encontrado com esse nome.")

# Menu principal
def menu():
    contatos = carregar_contatos()
    while True:
        print("\n" + "=" * 20 + " Bem-Vindo ao Menu " + "=" * 20)
        print("1 - Adicionar Contato")
        print("2 - Listar Contatos")
        print("3 - Atualizar Contato")
        print("4 - Excluir Contato")
        print("5 - Buscar Contato")
        print("6 - Importar para CSV")
        print("7 - Sair e Salvar")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            adicionar_contatos(contatos)
        elif opcao == "2":
            lista_contatos(contatos)
        elif opcao == "3":
            atualizar_contato(contatos)
        elif opcao == "4":
            excluir_contato(contatos)
        elif opcao == "5":
            busca_contato_usuário(contatos)
        elif opcao == "6":
            exportar_para_csv(contatos)
        elif opcao == "7":
            salvar_contatos(contatos)
            print("Encerrando o programa... Contatos salvos.")
            exit()
        else:
            print("Opção inválida. Tente novamente.")

# Executa o programa
menu()
