# QUESTÃO 3 #


# Funcao para pegar o valor no formato certo do input
def pegarValor():
    while True:

        valor = input('\nDigite o valor para ser decomposto: ')

        if ('.' in valor): # Verifica se o valor contém um ponto decimal
            inteiro, parteDecimal = valor.split(sep='.') # Divide a string em parte inteira e decimal
            
            if ((len(parteDecimal)==2) and (inteiro.isdigit()) and (parteDecimal.isdigit())): # Verifica se são dígitos e se a parte decimal tem 2 casas
                return valor
            
            else:
                print('\nInput inválido!\n')

        else:
            print('\nInput inválido!\n')

# Função para calcular o troco em notas e moedas
def calcularTroco():
    valor = pegarValor()
    valor = float(valor)

    # Listas de valores das notas e moedas
    notas = [100, 50, 20, 10, 5, 2]
    moedas = [1, 0.5, 0.25, 0.1, 0.05, 0.01]
    
    # Parte das notas
    print("\nNOTAS:")
    for elemento in notas:
        # Calcula a quantidade de notas necessárias
        quantidadeNotas = int(valor // elemento)
        valor = valor - quantidadeNotas*elemento
        nota = float(elemento)
        print(f'{quantidadeNotas} nota(s) de R$ {nota:.2f}')
        


    # Parte das moedas
    print("\nMOEDAS:")
    for elemento in moedas:
        if elemento == 0.01:
            # Para as moedas de 1 centavo, n foi utilizado o resto para evitar erros
            quantidadeMoedas = int(valor / elemento)
            valor = valor - quantidadeMoedas*elemento
            valor = round(valor, 2)
            moeda = float(elemento)
            print(f'{quantidadeMoedas} moeda(s) de R$ {moeda:.2f}')
        else:
            # Calcula a quantidade de moedas necessárias para os demais
            quantidadeMoedas = int(valor // elemento)
            valor = valor - quantidadeMoedas*elemento
            valor = round(valor, 2)
            moeda = float(elemento)
            print(f'{quantidadeMoedas} moeda(s) de R$ {moeda:.2f}')


        
    
    print('\n')
    return 0

calcularTroco()