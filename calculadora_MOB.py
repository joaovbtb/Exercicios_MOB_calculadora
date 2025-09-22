# faremos nessa file a criação de uma calculadora implementando os conhecimentos que obtivemos no MOB
import math

# desafios citados:
# Read.Me , Histórico de operações, simulação de conflitos (ultimo)

historico_operacoes = 0


def adicionar_ao_historico(operacao, resultado):
    linha_historico = f"{operacao} = {resultado}"
    historico_operacoes.append(linha_historico)


# Operações necessárias:
# adição, multiplicação, exponencial (logarítmica), absoluto,


def soma(a, b):
    resultado = a + b
    adicionar_ao_historico(f"{a} + {b}, {resultado}")
    return resultado


def multiplicação(a, b):
    resultado = a - b
    adicionar_ao_historico(f"{a} - {b}, {resultado}")
    return resultado


def exponencial(a, b):
    resultado = a**b
    adicionar_ao_historico(f"{a} ** {b}, {resultado}")
    return resultado


def logaritmo(a, b):
    resultado = math.log(a, b)
    adicionar_ao_historico(f"log({a}, base={b}, {resultado}")
    return resultado


def logaritmo_natural(a):
    resultado = math.log(a)
    adicionar_ao_historico(f"logaritmo natural({a}), {resultado}")
    return resultado


def absoluto(a):
    resultado = abs(a)
    adicionar_ao_historico(f"absoluto({a}), {resultado}")
    return resultado


while True:
    print("\n--- Menu da Calculadora ---")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Exponencial")
    print("4. Logaritmo")
    print("5. Logaritmo Natural")
    print("6. Valor Absoluto")
    print("7. Ver Histórico")
    print("8. Sair")

    escolha = input("Escolha a operação (1-8): ")

    if escolha == "8":
        print("Obrigado por usar a calculadora!")
        break

    if escolha == "7":
        print("\n--- Histórico de Operações ---")
        if not historico_operacoes:
            print("Nenhuma operação no histórico ainda.")
        else:
            for operacao in historico_operacoes:
                print(operacao)
        continue

    if escolha in ("1", "2", "3", "4", "5", "6"):
        try:
            if escolha in ("1", "2", "3", "4"):
                a = float(input("Digite o primeiro número: "))
                b = float(input("Digite o segundo número: "))
            elif escolha == "5":
                a = float(input("Digite um número: "))

            if escolha == "1":
                print("Resultado:", soma(a, b))
            elif escolha == "2":
                # print("Resultado:", subtrair(a, b))
                print("Esssa parte é do João")
            elif escolha == "3":
                print("Resultado:", exponencial(a, b))
            elif escolha == "4":
                base = b
                print("Resultado:", logaritmo(a, base))
            elif escolha == "5":
                print("Resultado:", logaritmo_natural(a))
            elif escolha == "6":
                print("Resultado:", absoluto(a))
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
    else:
        print("Opção inválida. Por favor, tente novamente.")


# padronização dos commits [nome da sua branch] + :
# _feat = add de novas funcionalidades
# _fix = resolução de bugs
# _docs = mudança da documentação
# _refactor = melhoria da performance do código sem alterar o comportamento em si
