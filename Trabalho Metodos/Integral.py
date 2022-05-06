import numpy as np 


arquivo_txt1 = np.genfromtxt("Dados.txt", dtype=float, usecols= 1, skip_footer = 4) 
arquivo_txt2 = np.genfromtxt("Dados.txt", dtype=float, usecols= 1, skip_header = 1, skip_footer = 3 )
arquivo_txt3 = np.genfromtxt("Dados.txt", dtype=float, usecols= 1, skip_header = 2, skip_footer = 2 )
arquivo_txt4 = np.genfromtxt("Dados.txt", dtype=float, usecols= 1, skip_header = 3, skip_footer = 1)
arquivo_txt5 = np.genfromtxt("Dados.txt", dtype=float, usecols= 1, skip_header = 4)

def integral(f, a, b, h=1e-6):
    N = int((b-a)/h)
    if N ==0:
        N=1
    l = np.linspace(a, b, num=N, endpoint=False)
    return np.sum(f(l)) * (b-a)/N 

def poly5(x): return x**3


integracao1 = str(integral(poly5, arquivo_txt1, 2))
integracao2 = str(integral(poly5, 1, arquivo_txt2))
integracao3 = str(integral(poly5, 1, arquivo_txt3))
integracao4 = str(integral(poly5, 1, arquivo_txt4))
integracao5 = str(integral(poly5, 1, arquivo_txt5))


with open("Integral.txt", 'w') as arquivo:
    arquivo.write('1 ' + integracao1 + '\n')
    arquivo.write('2 ' + integracao2 + '\n')
    arquivo.write('3 ' + integracao3 + '\n')
    arquivo.write('4 ' + integracao4 + '\n')
    arquivo.write('5 ' + integracao5 + '\n')