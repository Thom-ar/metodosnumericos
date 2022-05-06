
from unittest import skip
import numpy as np
import pandas as pd

#Função x^3
arquivo_txt = np.genfromtxt("Dados.txt", dtype=float, usecols= 1, skip_header = 1, skip_footer = 1 )
arquivo_txtA = np.loadtxt("Dados.txt", dtype=float, usecols= 1, skiprows = 4)
arquivo_txtB = np.genfromtxt("Dados.txt", dtype=float, usecols= 1, skip_footer = 4) 


h = 1e-6
h1 = arquivo_txt - h
h2 = arquivo_txt + h
h2B = arquivo_txtB + h
#Diferença atrasada
atrasada = (arquivo_txtA**3 - (arquivo_txtA-h)**3)/h
print('Diferenca Atrasada:',atrasada)
#Diferença centrada
centrada = (h2**3 - h1**3)/(2*h)
print('Diferenca Centrada:',centrada)
#Diferença avançada
avancada = (h2B**3 -arquivo_txtB**3)/h 
print('Diferenca Avancada:',avancada)
f1 = str(atrasada)
f2 = str(centrada.transpose())
#f2 = str(centrada)
f3 = str(avancada)
with open("derivada.txt", 'w') as arquivo:
    arquivo.write('n ' + 'F(n)' + '\n')
    arquivo.write('Diferenca Avancada: 1 '+ f3 + '\n')
    arquivo.write('Diferenca Centrada: 2 3 4 ' + f2 + '\n')
    arquivo.write('Diferenca Atrasada: 5 '+ f1 + '\n')
    
    





    
