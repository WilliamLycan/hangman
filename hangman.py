from random import randint
from time import sleep

white = '\033[;30;m'
red = '\033[;31;m'
green = '\033[;32;m'
yellow = '\033[;33;m'
blue = '\033[;34;m'
purple = '\033[;35;m'
glue = '\033[;36;m'
gray = '\033[;37;m'
alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
# Forca com o boneco
hangman = list("__________\n|        |\n|         \n|          \n|          \n|\n|")


# Atualiza o boneco na forca (mudar para uma guilhotina se possível)
def update_hangman(tries):
    if tries == 5:
        return
    elif tries == 4:
        hangman[31] = 'O'
        hangman[42] = '|'
    elif tries == 3:
        hangman[41] = '/'
    elif tries == 2:
        hangman[43] = '\\'
    elif tries == 1:
        hangman[53] = '/'
    elif tries == 0:
        hangman[55] = '\\'


# Reseta o boneco para o estado original
def reset_hangman():
    hangman[31] = ' '
    hangman[42] = ' '
    hangman[41] = ' '
    hangman[43] = ' '
    hangman[53] = ' '
    hangman[55] = ' '


# Mostra uma animação de carregamento
def loading():
    for i in range(4, -1, -1):
        update_hangman(i)
    print('Carregando...')
    for l in hangman:
        if l == '\n':
            sleep(0.3)
            print(l, end='')
        else:
            print(l, end='')
    reset_hangman()


# Recebe uma palavra/frase e retorna uma lista com os caracteres escondidos por underscore.
def hide(word):
    h_word = list(word)
    for l in range(0, len(h_word)):
        if word[l] in alphanum:
            h_word[l] = '_'
        else:
            h_word[l] = word[l]
    return h_word


def play(words):
    loading()
    # Guarda a lista de palavras ocultas.
    h_words = []
    for i in range(0, len(words)):
        # Copia uma versão oculta para a lista.
        h_words.append(hide(words[i]))
    # Armazena a última palavra/frase em uma variável, essa é a dica.
    tip = words[-1].upper()
    # Retira a dica da lista de palavras ocultas e da lista de palavras.
    h_words.pop()
    words.pop()
    # Lista que vai guardar todos os caracteres digitados.
    h_alphanum = []
    tries = 5
    while True:
        update_hangman(tries)
        print('\n' + '=' * 40)
        print(" ".join(h_alphanum))
        print(f'Tentativas restantes: {tries}')
        print(''.join(hangman))
        for w in h_words:
            print('| ' + ' '.join(w))
        print(f'\nDica: {tip}')
        # Verifica se ainda existem tentativas, senão encerra o loop.
        if tries == 0:
            if len(words) > 1:
                print('Você perdeu! As palavras/frases secretas são')
            else:
                print('Você perdeu! A palavra/frase secreta é')
            for w in words:
                print(w)
            # Aguarda o jogador pressionar ENTER.
            input('OK')
            break
        win = True
        # Verifica se as palavras estão diferentes, se sim, invalida a vitória.
        for i in range(0, len(words)):
            if h_words[i] != list(words[i]):
                win = False
        if win:
            print('Acertô mizerávi!')
            # Aguarda o jogador pressionar ENTER.
            input('OK')
            break
        # Captura apenas o primeiro caractere
        l = str(input('\nLetra: ')).upper()
        if len(l) == 0:
            op = '0'
        # Verifica se a letra já foi digitada consultando a lista de letras.
        if l in h_alphanum:
            print(f'Você já tentou o caractere {l}!')
            input('OK')
            continue
        else:
            h_alphanum.append(l)
        # Atualiza a palavra oculta caso exista a letra na palavra/frase.
        h = False
        for x in range(0, len(words)):
            if l in words[x]:
                h = True
                for y in range(0, len(words[x])):
                    if l == words[x][y]:
                        h_words[x][y] = l
        if not h:
            tries -= 1
    reset_hangman()


def versus():
    while True:
        print('1 Simples\n2 Avançado\n3 Voltar')
        # Captura apenas o primeiro caractere.
        op = str(input())
        if len(op) == 0:
            op = '0'
        words = []
        if op == '1':
            word = str(input('Digite a palavra/frase secreta: ')).strip().upper()
            tip = str(input('Qual é a dica? : ')).strip().upper()
            words.append(word)
            words.append(tip)
            play(words)
            break
        elif op == '2':
            for i in range(0, 4):
                if i != 3:
                    w = str(input(f'Digite a {i+1}ª palavra/frase: ')).strip().upper()
                    words.append(w)
                else:
                    words.append(str(input('Qual é a dica? ')))
            play(words)
            break
        elif op == '3':
            break


def mainloop():
    while True:
        print(f'=' * 40)
        print(f'{glue}{"JOGO DA FORCA V3.0":*^40}{white}')
        print(f'=' * 40)
        print(f'{purple}1 Novo Jogo Solo\n{blue}2 Novo Jogo Versus\n{red}3 Sair{white}')
        op = str(input())
        # Evita o erro de indexação caso o jogador pressione ENTER sem digitar algo
        if len(op) == 0:
            op = '0'
        if op == '1':
            print('Jogo Solo em desenvolvimento...')
            input('OK')
        elif op == '2':
            versus()
        elif op == '3':
            break
        else:
            print('Opção inválida.')


mainloop()
