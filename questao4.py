# QUESTÃO 4 #

# Função para contar a frequência de números inseridos pelo usuário
def frequenciaDeNumeros():
    
    numerosContados = {}
    
    # Loop para solicitar os números ao usuário
    while True:
        numero = input("Digite um inteiro: ")
        if (numero == 'f'): # Finalizar o programa
            print('\nFim...\n')
            break
        
        elif (numero.isdigit()): # Verifica se a entrada é um número inteiro
            numero = int(numero)
            if numero in numerosContados: # Verifica se o número já está no dicionário
                numerosContados[numero] = numerosContados[numero] + 1 # 
            else:
                numerosContados[numero] = 1 # Caso não esteja vai ser adiconado ao diconario com o valor = 1

    for numero in numerosContados: # Printar na tela
        if (numerosContados[numero] == 1):
            print(f'O número {numero} apareceu 1 vez')
        else:
            print(f'O número {numero} apareceu {numerosContados[numero]} vezes')
    print('\n')  

frequenciaDeNumeros()