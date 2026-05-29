# inquilinos.py
from banco_dados import lista_inquilinos

def cadastrar_inquilino():
    print("\n--- CADASTRO DE INQUILINO ---")
    nome = input("Nome completo: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")
    cpf = input("CPF (opcional): ")
    obs = input("Observações: ")

    novo_inquilino = {
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "cpf": cpf,
        "observacoes": obs
    }
    lista_inquilinos.append(novo_inquilino)
    print(f"Inquilino {nome} cadastrado com sucesso!")