"""Capivara! By Hideaki Fukami
Um jogo de dedução lógica em que você deve adivinhar um número recebendo algumas dicas."""

import random

NUM_DIGITS = 3
MAX_GUESSES = 10

def main():
    print(f'''Capivara, um jogo de dedução lógica.
By Hideaki Fukami

Eu estou pensando em um número de {NUM_DIGITS} dígitos onde os números não se repetem.
Tente adivinhar em que número estou pensando. Aqui estão algumas regras:

Quando eu digo:         Isso significa:

Quati                   Um dígito está correto e no lugar correto.
Tatu                    Um dígito está correto mas no lugar errado.
Capivara                Nenhum dígito está correto.

Por exemplo, se o número secreto for 248 e você chutar 843, as dicas serão Quati Tatu.''')

    while True:
        secretNum = getSecretNum()
        print('\nEu escolhi um número.')
        print(f'Voce tem {MAX_GUESSES} chances para acertar.')

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print(f'Tentativa #{numGuesses}: ')
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break
            if numGuesses > MAX_GUESSES:
                print('Suas tentativas acabaram!')
                print(f'A resposta era {secretNum}.')
        
        print('Você gostaria de jogar novamente? (Sim ou Não)')
        if not input('> ').lower().startswith('s'):
            break
    print('Obrigado por jogar!')

def getSecretNum():
    numbers = list(range(0, 10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(NUM_DIGITS):
        secretNum += str(numbers[i])
    return secretNum

def getClues(guess, secretNum):
    if guess == secretNum:
        return 'Você acertou!'

    clues = []

    for i in range(len(guess)):
        if guess[i] == secretNum[i]:
            clues.append('Quati')
        elif guess[i] in secretNum:
            clues.append('Tatu')
    if len(clues) == 0:
        return 'Capivara'
    else:
        clues.sort()
        return ' '.join(clues)

if __name__ == '__main__':
    main()