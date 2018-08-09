#Hangman v2.0
#Programador: Will
#__________________________________________________________
white = '\033[;30;m'
red = '\033[;31;m'
green = '\033[;32;m'
yellow = '\033[;33;m'
blue = '\033[;34;m'
purple = '\033[;35;m'
glue = '\033[;36;m'
gray = '\033[;37;m'
alphanum = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'


# Recebe uma palavra/frase e retorna uma lista com os caracteres escondidos por underscore.
def hide(word):
    h_word = list(word)
    for l in range(0, len(h_word)):
        if word[l] in alphanum:
            h_word[l] = '_'
        else:
            h_word[l] = word[l]
    return h_word


def play_s(word):
    word = str(word).upper()
    h_word = hide(word)
    h_alphanum = []
    tries = 5
    while True:
        # Mostra o menu in game. Uma lista com todas as letras que foram tentadas, o número de tentativas e a palavra
        # oculta.
        print('\n' + " ".join(h_alphanum))
        print(f'Tentativas restantes: {tries}\n')
        print(' '.join(h_word))
        # Verifica se ainda existem tentativas, senão encerra o loop.
        if tries == 0:
            print(f'Você perdeu! A palavra/frase secreta é {word}')
            # Aguarda o jogador pressionar ENTER.
            input()
            break
        if h_word == list(word):
            print('Acertô mizerávi!')
            # Aguarda o jogador pressionar ENTER.
            input()
            break
        # Captura apenas o primeiro caractere
        l = str(input('\nLetra: ')).upper()[0]
        # Verifica se a letra já foi digitada consultando a lista de letras.
        if l in h_alphanum:
            print(f'Você já tentou o caractere {l}!')
            input()
            continue
        else:
            h_alphanum.append(l)
        # Atualiza a palavra oculta caso exista a letra na palavra/frase.
        if l in word:
            for i in range(0, len(word)):
                if word[i] == l:
                    h_word[i] = l
        else:
            tries -= 1


def play_a(words):
    h_words = []
    for i in range(0, len(words)):
        words[i] = words[i].upper()
        h_words.append(hide(words[i].upper()))
    # Armazena a última palavra/frase em uma variável, essa é a dica.
    tip = words[-1].upper()
    # Retira a dica da lista de palavras ocultas e da lista de palavras.
    h_words.pop()
    words.pop()
    h_alphanum = []
    tries = 5
    while True:
        print('\n' + '=' * 40)
        print(" ".join(h_alphanum))
        print(f'Tentativas restantes: {tries}\n')
        for w in h_words:
            print(' '.join(w))
        print(f'\nDica: {tip}')
        # Verifica se ainda existem tentativas, senão encerra o loop.
        if tries == 0:
            print('Você perdeu! As palavras/frases secretas são')
            for w in words:
                print(w)
            # Aguarda o jogador pressionar ENTER.
            input()
            break
        win = True
        # Verifica se as palavras estão diferentes, se sim, invalida a vitória.
        for i in range(0, len(words)):
            if h_words[i] != list(words[i]):
                win = False
        if win:
            print('Acertô mizerávi!')
            # Aguarda o jogador pressionar ENTER.
            input()
            break
        # Captura apenas o primeiro caractere
        l = str(input('\nLetra: ')).upper()[0]
        # Verifica se a letra já foi digitada consultando a lista de letras.
        if l in h_alphanum:
            print(f'Você já tentou a letra {l}!')
            input()
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


def versus():
    while True:
        print('1 Simples\n2 Avançado\n3 Voltar')
        op = str(input())[0]
        if op == '1':
            play_s(str(input('Digite a palavra/frase secreta: ')))
            break
        elif op == '2':
            words = []
            for i in range(0, 3):
                if i != 2:
                    w = str(input(f'Digite a {i+1}ª palavra/frase: '))
                    words.append(w)
                else:
                    words.append(str(input('Qual é a dica? ')))
            play_s(words)
            break
        elif op == '3':
            break


def mainloop():
    while True:
        print(f'=' * 40)
        print(f'{glue}{"JOGO DA FORCA V3.0":*^40}{white}')
        print(f'=' * 40)
        print(f'{purple}1 Novo Jogo Solo\n{blue}2 Novo Jogo Versus\n{red}3 Sair{white}')
        op = str(input())[0]
        if op == '1':
            print('Jogo Solo em desenvolvimento...')
        elif op == '2':
            versus()
        elif op == '3':
            break
        else:
            print('Opção inválida.')


mainloop()
