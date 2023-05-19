def intro(jogo):
    print('---------------------------')
    print(' '*6, jogo, ' '*6)
    print('---------------------------')
'''with open('palavras.txt') as arquivo:
    linhas = arquivo.read()
    print(linhas)
    lista_de_palavras = linhas.split('\n')'''
import random

forca = '''
_____
    |
    -'''
vazio = '''
'''

cabeca = '''
    O
'''
tronco = '''
    O
    |
'''
b_direito = '''
    O
   /|
'''
b_esquerdo = '''
    O
   /|\\
'''
p_direita = '''
    O
   /|\\
   / \\
'''
p_esquerda = '''
    O
   /|\\
   / \\
'''
intro("Jogo da forca")

acertos = 0
erros = 0

letras_acertadas = ''
letras_erradas = ''

lista = ['julian', 'robert', 'jullia', 'gaiman', 'giseli', 'thiago', 'vanete', 'heitor', 'python', 'shadow']
palavras = [lista.upper()
            for lista in lista]

sorteio = random.choice(palavras) #sorteia um elemento da lista (choice: sorteia um elemento da lista, choices: sorteia vários)

while acertos != len(sorteio) and erros != 5:
    letra = input("Digite uma letra: ").upper() # o upper serve pra deixar a letra em caixa alta independente de como o usuário digitar
    if letra in sorteio:
        print("Você acertou!")
        letras_acertadas += letra # mantém as a letras certas adicionadas no laço de repetição anterior
        acertos += 1
    else:
        print("Você errou!")
        letras_erradas += letra
        erros += 1
    msg = ''
    for letra in sorteio:
        if letra in letras_acertadas:
            msg += letra + ' '  # mostra a letra no lugar + um espaco
        else:
            msg += '_'  # mostra que não tem nenhuma letra certa ainda naquela posição
    chances = [vazio, cabeca, tronco, b_direito, b_esquerdo, p_direita, p_esquerda]
    print(forca + chances[erros])
    print(msg)
    print(f'Você já acertou: ' + letras_acertadas)  # junta as letras acertadas

print(f"A palavra era: {sorteio}")
