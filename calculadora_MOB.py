
import math
#faremos nessa file a criação de uma calculadora implementando os conhecimentos que obtivemos no MOB

#Operações necessárias:
# adição, subtração(), multiplicação, potenciação(), exponencial (logarítmica), mod (resto)(), absoluto, trigonométricas

# faremos nessa file a criação de uma calculadora implementando os conhecimentos que obtivemos no MOB


# desafios citados:
# Read.Me , Histórico de operações, simulação de conflitos (ultimo)

historico_operacoes = []

def subtracao(*args):
    if len(args) < 2:
        raise ValueError("Subtração requer pelo menos dois argumentos.")
    resultado = args[0]
    for num in args[1:]:
        adicionar_ao_historico(f"{resultado} - {num}", {resultado - num})
        resultado -= num
    return resultado

def multiplicação(*args):
    if len(args) < 2:
        raise ValueError("Multiplicação requer pelo menos dois argumentos.")
    resultado = args[0]
    for num in args[1:]:
        adicionar_ao_historico(f"{resultado} * {num}", {resultado * num})
        resultado *= num
    return resultado

def soma(*args):
    if len(args) < 2:
        raise ValueError("Soma requer pelo menos dois argumentos.")
    resultado = args[0]
    for num in args[1:]:
        adicionar_ao_historico(f"{resultado} + {num}", {resultado + num})
        resultado += num
    return resultado

def logaritmo_natural(a):
    if a <= 0:
        raise ValueError("O logaritmo de números não positivos não está definido.")
    adicionar_ao_historico(f"logaritmo natural({a})", {math.log(a, math.e)})
    return math.log(a, math.e)
    
def absoluto(a):
    resultado = abs(a)
    adicionar_ao_historico(f"absoluto({a})", {resultado})
    return resultado
  
def divisao(*args):
    if len(args) < 2:
        raise ValueError("Divisão requer pelo menos dois argumentos.")
    resultado = args[0]
    for num in args[1:]:
        if num == 0:
            raise ZeroDivisionError("Divisão por zero não é permitida.")
        adicionar_ao_historico(f"{resultado} / {num}", {resultado / num})
        resultado /= num
    return resultado

def potencia(base, expoente):
    resultado = math.pow(base, expoente)
    adicionar_ao_historico(f"{base} ** {expoente}", {resultado})
    return resultado

def fatorial(n):
    if not isinstance(n, int) or n < 0:
        raise TypeError("Fatorial só aceita um número inteiro não negativo.")
    adicionar_ao_historico(f"fatorial({n})", {math.factorial(n)})
    return math.factorial(n)

def modulo(a, b):
    if b == 0:
        raise ZeroDivisionError("Módulo por zero não é permitido.")
    adicionar_ao_historico(f"{a} % {b}", {a % b})
    return a % b

def seno(a):
    adicionar_ao_historico(f"seno({a})", {math.sin(a)})
    return math.sin(a)

def cosseno(a):
    adicionar_ao_historico(f"cosseno({a})", {math.cos(a)})
    return math.cos(a)

def tangente(a):
    adicionar_ao_historico(f"tangente({a})", {math.tan(a)})
    return math.tan(a)
    
def logaritmo(base, n):
    if n <= 0:
        raise ValueError("O logaritmo de números não positivos não está definido.")
    adicionar_ao_historico(f"logaritmo({base}, {n})", {math.log(n, base)})
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
    '**': potencia,
    'abs': absoluto,
    '*': multiplicação,
    'ln': logaritmo_natural
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
    """
    Tenta criar uma entrada no histórico de operações e torna-la acessível.
    Se o histórico não estiver acessível, a função retorna que está vazia.
    """
    linha_historico = f"{operacao} = {resultado}"
    historico_operacoes.append(linha_historico)


#função principal da calculadora
def calculadora():
    print('As funções disponíveis são: +, -, *, /, **, log, abs, %, !, sen, cos, tg')
    print("Para encerrar, digite 'x' na operação.")
    print('Para ver o histórico, digite "H" no menu principal.')
    
    while True:
        try:
            operacao_input = input('\nSelecione a operação desejada: ').lower()

            # verifica se o usuário quer ver o histórico
            if operacao_input == "h":
                print("\n--- Histórico de Operações ---")
                if not historico_operacoes:
                    print("Nenhuma operação no histórico ainda.")
                else:
                    for operacao in historico_operacoes:
                        print(operacao)
                continue

            # verifica se o usuário quer sair
            if operacao_input == 'x':
                print('Encerrando a calculadora...')
                break
            
            # verifica se a operação é válida
            if operacao_input not in operacoes:
                raise ValueError("Operação inválida. Por favor, escolha uma das opções listadas.")
            
            valores_input = input('Digite os valores, separados por espaço: ')
            valores = converter_para_numeros(valores_input)

            # resgata a função correspondente à operação
            funcao = operacoes[operacao_input]
            
            # corrige a falta de algorismos para certas operações
            if operacao_input in ['**', 'log', '%', 'ln']:
                if len(valores) != 2:
                    raise ValueError(f"A operação '{operacao_input}' requer exatamente 2 valores.")
                resultado = funcao(*valores)
            elif operacao_input in ['!', 'sen', 'cos', 'tg', 'abs']:
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


