def intro(jogo):
    print('---------------------------')
    print('-'*6, jogo,'-'*6)
    print('---------------------------')


intro("Jogo da forca")
'''sorteio = random.choices(palavras) #sorteia um elemento da lista'''
palavras = 'Julian'.upper()

acertos = 0
erros = 0

letras_acertadas = ''
letras_erradas = ''

while acertos != len(palavras) and erros != 5:
    msg = ''
    print(f'Você já acertou: ' + letras_acertadas)
    print(f'Você já errou: ' + letras_erradas)
    letra = input("Digite uma letra: ").upper()
    if letra in palavras:
        print("Você acertou!")
        letras_acertadas += letra
        acertos += 1
    else:
        print("Você errou!")
        letras_erradas += letra
        acertos += 1
    for letra in palavras:
        if letra in letras_acertadas:
            msg += letra

        else:
            msg += '_'
    print(msg)

'''print(f"A palavra era: {palavras}")'''
