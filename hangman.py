#Hangman v2.0
#Programador: Will
#__________________________________________________________

#Strings com os textos do menu principal
msg_title = "\nJogo da Forca v2.0\n"
msg_sp = "Jogar Sozinho"
msg_mp = "Jogar em dupla"
msg_edit = "Editar Palavras/Frases"
msg_options = "Opções"
msg_credits = "Créditos"
msg_exit = "Sair"
msg_help = "Ajuda"

msgs_mm = [msg_title,
           msg_sp,
           msg_mp,
           msg_edit,
           msg_options,
           msg_credits,
           msg_exit,
           msg_help]

#Strings com os textos de ajuda do menu principal
msg_sp_help = "(Palavras/frases registradas)"
msg_mp_help = "(Palavras/frases definidas por outro jogador)"
msg_edit_help = "(Adicionar ou remover palavras/frases)"
msg_options_help = "(Configurar opções do jogo)"
msg_credits_help = "(Mostrar nomes da equipe de desenvolvimento)"
msg_exit_help = "(Fechar o jogo)"
msg_help_help = "(Escolha novamente para desligar)"

msgs_mm_help = [' ',
                msg_sp_help,
                msg_mp_help,
                msg_edit_help,
                msg_options_help,
                msg_credits_help,
                msg_exit_help,
                msg_help_help]

#Strings com os textos do menu jogar sozinho
msg_sp_title = "\nJogar Sozinho\n"
msg_sp_s = "Simples"
msg_sp_a = "Avançado"
msg_back = "Voltar"

msgs_sp = [msg_sp_title,
           msg_sp_s,
           msg_sp_a,
           msg_back,
           msg_help]

#Strings com os textos de ajuda do menu jogar sozinho
msg_sp_s_help = "  (Uma palavra/frase)"
msg_sp_a_help = " (Três palavras/frases com dica)"
msg_back_help = "   (Voltar ao menu principal)"

msgs_sp_help = [' ',
                msg_sp_s_help,
                msg_sp_a_help,
                msg_back_help,
                "    " +  msg_help_help]

#Strings in game
msg_in_game_try = "Tentativas: "
msg_in_game_hint = "Dica: "
msg_in_game_enter = "Digite uma letra/número ou a palavra/frase inteira: "
msg_in_game_win = "Acertô mizerávi!"
msg_in_game_lose = "Você perdeu!"
msg_in_game_invalid = "Texto inválido"
msg_in_game_repeat = "Você já tentou essa letra!"

msgs_in_game = [msg_in_game_try,
                msg_in_game_hint,
                msg_in_game_enter,
                msg_in_game_win,
                msg_in_game_lose,
                msg_in_game_invalid,
                msg_in_game_repeat]

#Strings com os textos do menu jogo em dupla
msg_mp_title = "\nJogar em Dupla\n"
msg_mp_s = "Simples"
msg_mp_a = "Avançado"

msgs_mp = [msg_mp_title,
           msg_mp_s,
           msg_mp_a,
           msg_back,
           msg_help]

#Strings com os textos de ajuda do menu de jogo em dupla
msg_mp_s_help = "  (Uma palavra/frase definida por outro jogador)"
msg_mp_a_help = " (Três palavras/frases com dica definidas por outro jogador)"

msgs_mp_help = [' ',
                msg_mp_s_help,
                msg_mp_a_help,
                msg_back_help,
                "    " + msg_help_help]

#Strings com os textos do jogo em dupla simples
msg_mp_s_in_game_title = "\nJogar em dupla -> Simples\n"
msg_mp_s_in_game_enter_word = "Digite a palavra/frase (Não deixe  outro jogador ver!):"
msg_mp_s_in_game_enter_hint = "Digite a dica (Enter para deixar sem dica):"

msgs_mp_s_in_game = [msg_mp_s_in_game_title,
                     msg_mp_s_in_game_enter_word,
                     msg_mp_s_in_game_enter_hint]

#Strings com os textos do jogo em dupla avançado
msg_mp_a_in_game_title = "\nJogar em dupla -> Avançado\n"
msg_mp_a_in_game_enter_1_word = "Digite a primeira palavra/frase:"
msg_mp_a_in_game_enter_2_word = "Digite a segunda palavra/frase:"
msg_mp_a_in_game_enter_3_word = "Digite a terceira palavra/frase:"
msg_mp_a_in_game_enter_hint = "Digite a dica:"

msgs_mp_a_in_game = [msg_mp_a_in_game_title,
                     msg_mp_a_in_game_enter_1_word,
                     msg_mp_a_in_game_enter_2_word,
                     msg_mp_a_in_game_enter_3_word,
                     msg_mp_a_in_game_enter_hint]


#Strings com os textos do menu de edição
msg_edit_title = "\nEditar palavras/frases e dicas\n"
msg_edit_add_s = "Adicionar palavras/frases simples"
msg_edit_add_a = "Adicionar palavras/frases avançado"
msg_edit_remove_s = "Remover palavras/frases simples"
msg_edit_remove_a = "Remover palavras/frases avançado"

msgs_edit = [msg_edit_title,
             msg_edit_add_s,
             msg_edit_add_a,
             msg_edit_remove_s,
             msg_edit_remove_a,
             msg_back]

#Strings do menu adicionar simples
msg_edit_add_s_title = "\nAdicionar palavras/frases simples\n"
msg_edit_cancel = "(Digite # para cancelar)"
msg_edit_add_s_enter_word = "Digite a palavra/frase para adicionar:"
msg_edit_add_s_done = "Palavra/frase adicionada!"

msgs_edit_add_s = [msg_edit_add_s_title,
                   msg_edit_cancel,
                   msg_edit_add_s_enter_word,
                   msg_edit_add_s_done]

#Strings do menu adicionar avançado
msg_edit_add_a_title = "\nAdicionar palavras/frases avançado\n"
msg_edit_add_a_enter_1_word = "Digite a primeira palavra/frase para adicionar:"
msg_edit_add_a_enter_2_word = "Digite a segunda palavra/frase para adicionar:"
msg_edit_add_a_enter_3_word = "Digite a terceira palavra/frase para adicionar:"
msg_edit_add_a_enter_hint = "Digite a dica para adicionar:"
msg_edit_add_a_done = "Palavras/frases e dica adicionadas!"

msgs_edit_add_a = [msg_edit_add_a_title,
                   msg_edit_cancel,
                   msg_edit_add_a_enter_1_word,
                   msg_edit_add_a_enter_2_word,
                   msg_edit_add_a_enter_3_word,
                   msg_edit_add_a_enter_hint,
                   msg_edit_add_a_done]

#Strings do menu remover simples
msg_edit_remove_s_title = "\nRemover palavras/frases simples\n"
msg_edit_remove_s_enter_n = "Digite o número da palavra/frase para remover:"
msg_edit_remove_s_done = "Palavra/frase removida!"

msgs_edit_remove_s = [msg_edit_remove_s_title,
                      msg_edit_cancel,
                      msg_edit_remove_s_enter_n,
                      msg_edit_remove_s_done]

#Strings do menu remover avançado
msg_edit_remove_a_title = "\nRemover palavras/frases avançado\n"
msg_edit_remove_a_enter_n = "Digite o número do grupo para remover:"
msg_edit_remove_a_done = "Grupo de palavras/frases removido!"

msgs_edit_remove_a = [msg_edit_remove_a_title,
                      msg_edit_cancel,
                      msg_edit_remove_a_enter_n,
                      msg_edit_remove_a_done]

#Strings do menu opções
msg_options_title = "\nOpções\n"
msg_options_op1 = "Mudar idioma: "
msg_options_lang = "Português"

msgs_options = [msg_options_title,
                msg_options_op1,
                msg_back]

#Mensagens dos créditos
msg_credits_title = "\nCréditos\n"
msg_credits = ""
msg_credits_press_anything = "\nDigite qualquer coisa para voltar"

msgs_credits = [msg_credits_title,
                msg_credits,
                msg_credits_press_anything]

#__________________________________________________________

#Esta seção do código deixa as mensagens de ajuda alinhadas

#Lista com os comprimentos de cada string
msgs_len_list = []

#Coloca o tamanho das mensagens em uma lista
for x in msgs_mm:
    msgs_len_list.append(len(x))

#Variável que guarda o numero de caracteres da maior string
bml = max(msgs_len_list)

#Função que adiciona o espaço de acordo com o tamanho da mensagem
def add_space(msgs, msgs_help, bml):
    index = 0
    for x in msgs_help:
        msgs_help[index] = (' ' * (bml - len(msgs[index])) + ' ' + msgs_help[index])
        index += 1
    return list(msgs_help)

msgs_mm_help = add_space(msgs_mm, msgs_mm_help, bml)
del msgs_len_list
del bml

#_________________________________________________________

#Função que recebe duas listas com strings e imprime o conteúdo
def print_menu_help(menu, menu_help, bool_help):
    index = 0
    for x in menu:
        if bool_help:
            if index == 0:
                print(menu[index] + menu_help[index])
            else:
                print(str(index) + ' ' + menu[index] + menu_help[index])
        else:
            if index == 0:
                print(menu[index])
            else:
                print(str(index) + ' ' + menu[index])
        index += 1
        
def print_menu(menu):
    index = 0
    for x in menu:
        if index == 0:
            print(menu[index])
        else:
            print(str(index) + ' ' + menu[index])
        index += 1

#Tabela com os caracteres alfanuméricos
alphanum = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

#Tabela que vai ser preenchida com os caracteres já tentados
hidden_alphanum = []

#Forca com o boneco
hangman = list("__________\n|        |\n|         \n|          \n|          \n|\n|")

#Tabela com os caracteres especiais, eles não serão escondidos
special_chars = "\"\'!@#$%¢¨¬&*()-_+=[]{}ªº<>,.;:/\\?°"

#Recebe uma lista e retorna outra string com os caracteres substituídos
#por underscore, exceto os que estão na tabela de caracteres especiais
def hide(word):
    hidden_word = list(word)

    index = 0
    
    for x in hidden_word:
        if not hidden_word[index] in special_chars:
            hidden_word[index] = '_'
        if word[index] == ' ':
            hidden_word[index] = ' '
        index += 1

    return hidden_word

#Atualiza a tabela de caracteres
def update_alphanum(l):
    if len(l) > 1:
        return
    else:
        index = 0
        for x in alphanum:
            if l == x:
                if not l in hidden_alphanum:
                    hidden_alphanum.append(alphanum[index])
            index += 1

#Atualiza o boneco na forca (mudar para uma guilhotina se possível)
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

#Reseta o boneco para o estado original
def reset_hangman():
    hangman[31] = ' '
    hangman[42] = ' '
    hangman[41] = ' '
    hangman[43] = ' '
    hangman[53] = ' '
    hangman[55] = ' '

#Recebe uma palavra e começa o jogo
def play_s(words):
    win = False
    lose = False
    tries = 5
    word = words[0]
    hint = words[1]
    hidden_word = hide(word)
    
    while True:
        update_hangman(tries)        
        print('\n' + " ".join(hidden_alphanum))
        print('\n' + msgs_in_game[0] + str(tries))
        print(msgs_in_game[1] + hint)
        print("".join(hangman))
        print('|' + ' '.join(hidden_word))

        if hidden_word == list(word) and not lose:
            hidden_word = list(word)
            print(msgs_in_game[3])
            if not win:
                win = True
                continue
        
        if tries == 0 and not win:
            hidden_word = list(word)
            print(msgs_in_game[4])
            if not lose:
                lose = True
                continue

        if win or lose:
            break

        print('\n' + msgs_in_game[2] + '\n')
        
        l = (input('\n')).upper()
        
        if len(l) == 1:
            if l in hidden_alphanum:
                print('\n' + msgs_in_game[6] +'\n')
                continue
        
            update_alphanum(l)
            index = 0
            if l in word:
                for x in word:
                    if l == word[index]:
                        hidden_word[index] = word[index]
                    index += 1
            else:
                tries -= 1
        elif len(l) == len(word):
            if l == word:
                hidden_word = list(word)
            else:
                tries -= 1
        else:
            print('\n' + msgs_in_game[5] + '\n')

    hidden_alphanum.clear()
    reset_hangman()
    input('\n')

#def play_a(words):


def sp_s():
    print("Você selecionou o jogo solo simples")

def sp_a():
    print("Você selecionou o jogo solo avançado")
    
def mp_s():
    print(msgs_mp_s_in_game[0] + '\n')
    print(msgs_mp_s_in_game[1])
    words = []
    words.append((input('\n')).upper())
    print('\n' + msgs_mp_s_in_game[2])
    words.append((input('\n')).upper())
    play_s(words)
        
def mp_a():
    print("Você selecionou o jogo em dupla avançado")

def sp():
    bool_help =  False
    
    while True:
        print_menu_help(msgs_sp, msgs_sp_help, bool_help)
    
        option = input('\n')

        if option == '1':
            print("Você selecionou o jogo solo simples.")
        elif option == '2':
            print("Você selecionou o jogo solo avançado.")
        elif option == '3':
            break
        elif option ==  '4':
            bool_help = not bool_help
            
def mp():
    bool_help =  False

    while True:
        print_menu_help(msgs_mp, msgs_mp_help, bool_help)
    
        option = input('\n')

        if option == '1':
            mp_s()
            break
        elif option == '2':
            mp_a()
            break
        elif option == '3':
            break
        elif option ==  '4':
            bool_help = not bool_help

def edit():
    done = False
    
    while not done:
        print_menu(msgs_edit)

        option = input('\n')

        if option == '1':
            print("Adicionar palavras simples")
        elif option == '2':
            print("Adicionar palavras avançado")
        elif option == '3':
            print("Remover palavras simples")
        elif option == '4':
            print("Remover palavras avançado")
        elif option == '5':
            done = not done

def options():
    while True:
        print(msgs_options[0])
        print(msgs_options[1] + ' ' + msgs_options[2])

        option = input('\n')

        if option == '1':
            print("Você mudou o idioma.")
        elif option == '2':
            break

def credits():
    print(msgs_credits[0])
    print(msgs_credits[1])
    print(msgs_credits[2])

    input('\n')

#Loop principal do jogo
bool_help = False
done =  False

while True:
    print_menu_help(msgs_mm, msgs_mm_help, bool_help)
    option = input('\n')
    
    if option == '1':
        sp()
    elif option == '2':
        mp()
    elif option == '3':
        edit()
    elif option == '4':
        options()
    elif option == '5':
        credits()
    elif option == '6':
        print("\nSaindo...\n")
        break
    elif option == '7':
        bool_help = not bool_help
