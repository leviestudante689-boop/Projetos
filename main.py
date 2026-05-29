import inquilinos
import cobrancas

def menu():
    while True:
        print("----MENU PRINCIPAL----")
        print("1 cadastrar inquilino")
        print("2 gerar cobrança")
        print("6 sair")
        opcao = input("Digite a opção desejada: ")

        if opcao == "1":
            inquilinos.cadastrar_inquilino()
        elif opcao == "2":
            pass
        elif opcao == "6":
            print("Saindo do programa...")
            break
        else: 
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    menu()
    