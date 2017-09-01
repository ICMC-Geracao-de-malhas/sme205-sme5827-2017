'''
ALUNO: DAVI LOTFI LAVOR NAVARRO DA ROCHA
NºUSP: 9012632

Trabalho 01 de Geração de Malhas

Entrada: Arquivo com uma lista simples de pontos em sentido anti-horário.

    Assim como no arquivo naca012.txt dado, o arquivo de entrada precisa ser formatado da seguinte forma:

    -- Coordenada X + Espaço + Coordenada Y --

    >> x1 y1
    >> x2 y2
    >> x3 y3
    >>  ...
    >> xk yk

Saída: Pontos dos bordos de um dominio regular onde um dos lados corresponde a curva de entrada.

    A saída do arquivo irá conter os bordos de um dominio regular e será formatado da seguinte maneira>

    >> Nº de Pontos
    >> Coordenadas do bordo superior (top)
    >> Nº de Pontos
    >> Coordenadas do bordo inferior (bottom)
    >> Nº de Pontos
    >> Coordenadas do bordo esquerdo (left)
    >> Nº de Pontos
    >> Coordenadas do bordo direito (right)

'''

import numpy as np

'''
    Começo do programa. Deve-se inserir o nome do arquivo 'txt' com os pontos como especificados nos comentarios acima.
'''

entrada = open('naca120.txt', 'r')
saida = open('bordos.txt', 'w')

'''
    x será a lista que irá conter as coordenadas do arquivo de entrada. Cada elemento da lista é um ponto (x,y). Logo, o numero
    de pontos será dado pela função len(x) abaixo.
'''

x = entrada.readlines()
n_de_pontos = len(x)

'''
    Aqui iniciamos as variaveis que serão ultilizadas no programa. 
    >> xt e yt = coordenadas do bordo superior
    >> xb e yb = coordenadas do bordo inferior
    >> xr e yr = coordenadas do bordo esquerdo
    >> xl e yl = coordenadas do bordo direito
'''
xt = 1.5*np.ones(n_de_pontos, dtype=float)
yt = np.zeros(n_de_pontos, dtype=float)

xb = np.ones(n_de_pontos, dtype=float)
yb = np.ones(n_de_pontos, dtype=float)

for i in range(n_de_pontos):
    xb[i] = float(x[i].split(" ")[0])
    yb[i] = float(x[i].split(" ")[1])

xr = np.linspace(1, 1.5, n_de_pontos)
yr = np.zeros(n_de_pontos)

''' 
    Aqui os pontos xr,yr são iguais a xl,yl, pois no arquivo ep1 que continha o exercicio, eles correspondem aos segmentos
    AB e CD, que fisicamente ocupam o mesmo espaço.,
'''

xl = xr
yl = yr

''' 
    No arquivo ep1 tinhamos um dominio retangular com coordenadas -1.0 < X < 1.5 e -0.6 < Y < 0.6. 
    O perimetro desse dominio é a soma de seus lados, ou seja 2.5 + 1.2 + 2.5 + 1.2 = 7.4 
    Dessa forma, defini a distância entres os pontos da seguinte forma (Perimetro)/(nº de pontos)
'''

dist_point = 7.4/(n_de_pontos)



'''
    Os comandos ''while'' abaixo percorrem o dominio retangular em sentido anti horário. 
    Cada (coordenada k + 1) = (coordenada k + dist+points)
    Setamos o ponto inicial do dominio B: (1.5,0.0) e acrescentamos dist_point a coordenada Y, até Y <= 0.6
    Para cada ponto 'k' encontrado dentro desse intervalo, salvamos sua informação em yt[k]
    Se encontrarmos o ponto Y > 0.6, o "while" muda, e percorre a extensão X, subtraindo dist_point, até X > -1.
    Dessa forma, temos uma distribuição parcialmente uniforme por todo o dominio.
       
'''
i = 1
while yt[i] < 0.6:

    yt[i + 1] = yt[i] + dist_point
    i = i + 1

i = i - 1
while xt[i] > -1:
    yt[i + 1] = yt[i]
    xt[i + 1] = xt[i] - dist_point
    i = i + 1

i = i - 1
while yt[i] > -0.6:
    yt[i + 1] = yt[i] - dist_point
    xt[i + 1] = xt[i]
    i = i + 1

i = i - 1
while xt[i] < 1.5:

    yt[i + 1] = yt[i]
    xt[i + 1] = xt[i] + dist_point
    i = i + 1

aux4 = i

i = i -1

while yt[i] < 0.0:
    yt[i + 1] = yt[i] + dist_point
    xt[i + 1] = 1.5
    i = i +1

xt[aux4 - 1] = 1.5


''' Imprime no arquivo o nº de pontos do bordo SUPERIOR e as coordenadas dos mesmos'''

saida.write('{}' .format(n_de_pontos))
for i in range (n_de_pontos):
    saida.write('\n{:.5f} {:.5f}' .format(xt[i], yt[i]))

''' Imprime no arquivo o nº de pontos do bordo INFERIOR e as coordenadas dos mesmos'''

saida.write('\n{}' .format(n_de_pontos))
for i in range(n_de_pontos):
    saida.write('\n')
    saida.write('{}'.format(xb[i]))
    saida.write(' ')
    saida.write('{}'.format(yb[i]))

''' Imprime no arquivo o nº de pontos do bordo ESQUERDO e as coordenadas dos mesmos'''

saida.write('\n{}' .format(n_de_pontos))
for i in range (n_de_pontos):
    saida.write('\n{:.5f} {:.5f}' .format(xl[i], yl[i]))

''' Imprime no arquivo o nº de pontos do bordo DIREITO e as coordenadas dos mesmos'''

saida.write('\n{}' .format(n_de_pontos))
for i in range (n_de_pontos):
    saida.write('\n{:.5f} {:.5f}' .format(xr[i], yr[i]))

saida.close()
entrada.close()