def mostra_pista (pinos):
    for elemento in pinos:
         print (elemento, end='') 
    print()

pista = [ 
   'I', ' ', 'I', ' ', 'I', ' ', 'I', '\n', ' ', 'I', ' ', 'I', ' ', 'I', '\n', ' ', ' ', 'I', ' ', 'I', '\n', ' ', ' ', ' ', 'I', ' '
]

posicao_dos_pinos = {
    '1' : 24,
    '2' : 17,
    '3' : 19,
    '4' : 9,
    '5' : 11,
    '6' : 13,
    '7' : 0,
    '8' : 2,
    '9' : 4,
    '10' : 6,
}
 
mostra_pista(pista)

jogada = ['6', '3',]

for pino in jogada:
    posicao = posicao_dos_pinos[pino]
    pista[posicao] = ' '

mostra_pista(pista)
