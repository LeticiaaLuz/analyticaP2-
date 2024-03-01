# QUESTÃO 2 #

# Funcao para pegar a posicao inical e final no formato certo do input
def pegarPosicoes():
    while True: 
        
        posicoes = input('\nDigite a posicao inicial e final do cavalo: ')
        
        if posicoes == 'f': # Finalizar o programa
            print('\nFim...\n')
            return None
        
        elif len(posicoes) != 5 or posicoes[2] != ' ': # # Verifica se a entrada está no formato desejado
            print('\nInput inválido!\n')
        
        else:
            # Define listas de colunas e linhas do tabuleiro de xadrez
            colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
            linhas = ['1', '2', '3', '4', '5', '6', '7', '8']
        
            if (posicoes[0] not in colunas or posicoes[1] not in linhas or
                posicoes[3] not in colunas or posicoes[4] not in linhas): # Verifica se as posicoes estão com valores presentes nas listas acima
                print('\nInput inválido!\n')
        
            else:
                return posicoes

def movimentarCavalo():
    while True:
        posicoes = pegarPosicoes()

        if posicoes is None:
            return 0

        # Separa a string. Divindo ela em posicao inicial e final              
        posicoes = posicoes.split(sep=" ")
        posicaoInicial, posicaoFinal = posicoes

        # Pega as colunas e linhas das posições inicial e final
        colunaInicial = posicaoInicial[0]
        linhaInicial = int(posicaoInicial[1])
        
        colunaFinal = posicaoFinal[0]
        linhaFinal = int(posicaoFinal[1])

        colunas = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        colunaInicialIndice = colunas.index(colunaInicial)
        colunaFinalIndice = colunas.index(colunaFinal)
        
        # Condicoes para as posicoes serém válidas
        if (((abs(colunaFinalIndice - colunaInicialIndice) == 2) and (abs(linhaFinal - linhaInicial) == 1)) or\
                 ((abs(colunaFinalIndice - colunaInicialIndice) == 1) and (abs(linhaFinal - linhaInicial) == 2))):
            
            print('\nVÁLIDO\n')
        
        else:
            print('\nINVÁLIDO\n')
       

movimentarCavalo()

