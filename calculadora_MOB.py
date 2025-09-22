
import math
#faremos nessa file a criação de uma calculadora implementando os conhecimentos que obtivemos no MOB

#Operações necessárias:
# adição, subtração(), multiplicação, potenciação(), exponencial (logarítmica), mod (resto)(), absoluto, trigonométricas

# faremos nessa file a criação de uma calculadora implementando os conhecimentos que obtivemos no MOB


# desafios citados:
# Read.Me , Histórico de operações, simulação de conflitos (ultimo)


historico_operacoes = 0

#parte voltada para a definição das funções:
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

def subtracao(*args):
    if len(args) == 0:
        raise ValueError("Subtração requer pelo menos um argumento.")
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
    return resultado

def multiplicação(a, b):
    resultado = a * b
    adicionar_ao_historico(f"{a} * {b}, {resultado}")
    return resultado

def soma(a, b):
    resultado = a + b
    adicionar_ao_historico(f"{a} + {b}, {resultado}")
    return resultado

def exponencial(a, b):
    resultado = a**b
    adicionar_ao_historico(f"{a} ** {b}, {resultado}")
    return resultado

def logaritmo_natural(a):
    resultado = math.log(a)
    adicionar_ao_historico(f"logaritmo natural({a}), {resultado}")
    return resultado


def absoluto(a):
    resultado = abs(a)
    adicionar_ao_historico(f"absoluto({a}), {resultado}")
    return resultado
  
def divisao(a, b):
    if b == 0:
        raise ZeroDivisionError("Divisão por zero não é permitida.")
    return a / b

def potencia(base, expoente):
    return math.pow(base, expoente)

def fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("Fatorial só aceita um número inteiro não negativo.")
    return math.factorial(n)

def modulo(a, b):
    return a % b

def seno(a):
    return math.sin(a)

def cosseno(a):
    return math.cos(a)

def tangente(a):
    return math.tan(a)
    
def logaritmo(base, n):
    if n <= 0:
        raise ValueError("O logaritmo de números não positivos não está definido.")
    return math.log(n, base)

#dicionário para mapear as operações às funções

operacoes = {
    '-': subtracao,
    '/': divisao,
    'log': logaritmo,
    '!': fatorial,
    '%': modulo,
    '+' : soma,
    'sen': seno,
    'cos': cosseno,
    'tg': tangente,
    '**': potencia
}


#parte da conversão
def converter_para_numeros(string_valores):
    """
    Tenta converter uma string de valores separados por espaço em uma lista de números.
    Se a conversão falhar, levanta um ValueError.
    """
    numeros = []
    for valor in string_valores.split():
        try:
            numeros.append(float(valor))
        except ValueError:
            raise ValueError(f"Valor inválido: '{valor}'. Por favor, insira apenas números.")
    return numeros
  
  #adiciona ao histórico 
  def adicionar_ao_historico(operacao, resultado):
    linha_historico = f"{operacao} = {resultado}"
    historico_operacoes.append(linha_historico)

#função principal da calculadora

def calculadora():
    print('As funções disponíveis são: +, -, *, /, **, log, abs, %, !, sen, cos, tg')
    print("Para encerrar, digite 'x' na operação.")
    
    while True:
        try:
            operacao_input = input('\nSelecione a operação desejada: ').lower()
            if operacao_input == 'x':
                print('Encerrando a calculadora...')
                break
            
            if operacao_input not in operacoes:
                raise ValueError("Operação inválida. Por favor, escolha uma das opções listadas.")
            
            valores_input = input('Digite os valores, separados por espaço: ')
            valores = converter_para_numeros(valores_input)

            # resgata a função correspondente à operação
            funcao = operacoes[operacao_input]
            
            # corrige a falta de algorismos para certas operações
            if operacao_input in ['/', '**', 'log', '%']:
                if len(valores) != 2:
                    raise ValueError(f"A operação '{operacao_input}' requer exatamente 2 valores.")
                resultado = funcao(*valores)
            elif operacao_input in ['!', 'sen', 'cos', 'tg']:
                if len(valores) != 1:
                    raise ValueError(f"A operação '{operacao_input}' requer exatamente 1 valor.")
                else:
                    resultado = funcao(*valores)
            else:
                resultado = funcao(*valores)
            
            print(f'Resultado: {resultado}')
        
        except (ValueError, TypeError, ZeroDivisionError) as e:
            print(f"Erro: {e}")
        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


# --- Execução Principal ---
if __name__ == '__main__':
    calculadora()







# Operações necessárias:
# adição, multiplicação, exponencial (logarítmica), absoluto,


