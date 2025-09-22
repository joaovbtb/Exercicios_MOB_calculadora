import math
#faremos nessa file a criação de uma calculadora implementando os conhecimentos que obtivemos no MOB

#Operações necessárias:
# adição, subtração(), multiplicação, potenciação(), exponencial (logarítmica), mod (resto)(), absoluto, trigonométricas

#desafios citados:
#Read.Me , Histórico de operações, tratamento de erros, testes unitários, simulação de conflitos (ultimo)

#parte voltada para a definição das funções:

def subtracao(*args):
    if len(args) == 0:
        raise ValueError("Subtração requer pelo menos um argumento.")
    resultado = args[0]
    for num in args[1:]:
        resultado -= num
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
            # Tenta converter para float para maior precisão, mas se for inteiro, ele funcionará bem.
            numeros.append(float(valor))
        except ValueError:
            raise ValueError(f"Valor inválido: '{valor}'. Por favor, insira apenas números.")
    return numeros

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

            # Executa a operação com base no que foi digitado.
            funcao = operacoes[operacao_input]
            
            # Algumas funções precisam de um número específico de argumentos.
            if operacao_input in ['/', '**', 'log', '%']:
                if len(valores) != 2:
                    raise ValueError(f"A operação '{operacao_input}' requer exatamente 2 valores.")
                resultado = funcao(*valores)
            elif operacao_input in ['!', 'sen', 'cos', 'tg', 'abs']:
                if len(valores) != 1:
                    raise ValueError(f"A operação '{operacao_input}' requer exatamente 1 valor.")
                # Converte para int para fatorial
                if operacao_input == '!':
                    resultado = fatorial(int(valores[0]))
                else:
                    resultado = funcao(*valores)
            else:
                resultado = funcao(*valores)
            
            print(f'Resultado: {resultado}')
        
        except (ValueError, TypeError, ZeroDivisionError) as e:
            # Captura os erros e mostra uma mensagem amigável para o usuário.
            print(f"Erro: {e}")
        except Exception as e:
            # Captura qualquer outro erro inesperado.
            print(f"Ocorreu um erro inesperado: {e}")


# --- Execução Principal ---
if __name__ == '__main__':
    calculadora()

#padronização dos commits [nome da sua branch] + :
#_feat = add de novas funcionalidades
#_fix = resolução de bugs
#_docs = mudança da documentação
#_refactor = melhoria da performance do código sem alterar o comportamento em si 







#Relatório pessoal de melhorias:
#1 - fazer as funções virarem desempacotamentos de argumentos
#2 - mudar o ultimo print() da função calculadora() em algo mais entendível talvez
#3 - pensar na possibilidade de mudar os números de int para float (pensar como abordar isso em factorial)
#4 - bolar uma forma de utilizar os Falses que vão ocorrendo para criar um sistema de segurança