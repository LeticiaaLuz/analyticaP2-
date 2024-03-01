# QUESTÃO 1 #

# Funcao para pegar o horario no formato certo do input
def pegarHorario():
    while True:
        horario = input('\nInforme o horario no formato(hh:mm) -> ')
        if (horario == 'f'): # Finalizar o programa
            print('\nFim...\n')
            return None
        
        elif (len(horario) != 5) or (horario[2] != ':'): # Verifica se as estradas estão no formato de horas
            print('\nInput inválido!\n')
            
        
        elif (horario[0:2].isdigit() and horario[3:5].isdigit()):
            horas = int(horario[0:2])
            minutos = int(horario[3:5])
            
            if ((0 <= horas <= 23) and (0 <= minutos <= 59)):
                return horas, minutos
            else: # Verifica se o horário está no formato 24hrs
                print('\nInput inválido!\n')
                
        else:
            print('\nInput inválido!\n')
            
    


# FORMA 1 DE RESOLUÇÃO:
# formula utilizada; angulo = (|11*minutos - 60*horas|)/2

# Funcao que vai calcular o angulo           
def calcularMenorAnguloFormula():
    while True:
        horario = pegarHorario()
        if horario is None:
            return 0
        else:
            horas, minutos = horario

        if (horas > 12): # Passa as horas para o intervalo de 0-12
            horas = horas - 12
        
        angulo = abs(11*minutos/2 - 30*horas)
        

        if (angulo > 180): # Pega o menor angulo
            angulo = 360 - angulo
            
        print(f'\nO menor ângulo é de {angulo}°\n')


# SEGUNDA FORMA DE RESLUÇÃO DA QUESTÃO 1:
# angulo = (o quanto o ponteiro das horas andou) - (o quanto o ponteiro dos minutos andou) 
        
#def calcularMenorAngulo():
#    while True:

#        horario = pegarHorario()
#        if horario is None:
#            return 0
#        else:
#            horas, minutos = horario
        
#        if (horas > 12):
#            horas = horas - 12

#        angulo = abs((horas*30) - (minutos*6))
        

#        if (angulo > 180):
#            angulo = 360 - angulo
   
#        print(f'\nO menor ângulo é de {angulo}°\n')


calcularMenorAnguloFormula()


