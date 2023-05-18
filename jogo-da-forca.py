def intro(jogo):
    print('---------------------------')
    print(' '*6, jogo, ' '*6)
    print('---------------------------')


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


#print(forca+tronco)

acertos = 0
erros = 0

letras_acertadas = ''
letras_erradas = ''

# sorteio = random.choices(palavras) #sorteia um elemento da lista
palavras = 'Julian'.upper()



while acertos != len(palavras) and erros != 5:
    letra = input("Digite uma letra: ").upper() # o upper serve pra deixar a letra em caixa alta independente de como o usuário digitar
    if letra in palavras:
        print("Você acertou!")
        letras_acertadas += letra # mantém as a letras certas adicionadas no laço de repetição anterior
        acertos += 1
    else:
        print("Você errou!")
        letras_erradas += letra
        erros += 1
    msg = ''
    for letra in palavras:
        if letra in letras_acertadas:
            msg += letra + ' '  # mostra a letra no lugar + um espaco
        else:
            msg += '_'  # mostra que não tem nenhuma letra acertada ainda naquela posição
    chances = [vazio, cabeca, tronco, b_direito, b_esquerdo, p_direita, p_esquerda]
    print(forca + chances[erros])
    print(msg)
    print(f'Você já acertou: ' + letras_acertadas)  # junta as letras acertadas

'''print(f"A palavra era: {palavras}")'''
