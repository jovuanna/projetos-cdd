def intro(jogo):
    print('---------------------------')
    print('-'*6, jogo,'-'*6)
    print('---------------------------')


import random

palavras = 'Julian'.upper()
intro("Jogo da forca")
'''sorteio = random.choices(palavras) #sorteia um elemento da lista'''
acertos = 0
erros = 0

while acertos != len(palavras) or erros != 6:
    letra = input("Digite uma letra: ").upper()
    if letra in palavras:
        print("Você acertou!")
    else:
        print("Você errou!")
'''print(f"A palavra era: {palavras}")'''
