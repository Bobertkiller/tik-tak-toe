def geraTabuleiro():
    M = []
    for i in range(3):
        linha = []
        for j in range(3):
            linha.append('.')
        M.append(linha)
    return M


def imprimeTabuleiro(M):
    for i in range(len(M)):
        for j in range(len(M[0])):
            print(M[i][j], end='   ')
        print('\n')


def jogar(tabuleiro, jogador, linha, coluna):
    if tabuleiro[linha][coluna] == '.':
        if (jogador % 2) == 0:
            tabuleiro[linha][coluna] = 'x'
            return tabuleiro, True
        else:
            tabuleiro[linha][coluna] = 'O'
            return tabuleiro, True
    else:
        print('O outro jogador ja marcou essa posição')
        return tabuleiro, False


def verificaGanhador(tabuleiro):
    verif_1 = 0
    verif_2 = 0

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] != '.':
                if tabuleiro[i][j] == 'x':
                    verif_1 += 1
                else:
                    verif_2 += 1
        if verif_1 == 3 or verif_2 == 3:
            print('Temos um vencedor')
            imprimeTabuleiro(tabuleiro)
            return tabuleiro, exit()
        else:
            verif_1, verif_2 = 0, 0

    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] != '.':
                if tabuleiro[j][i] == 'x':
                    verif_1 += 1
                else:
                    verif_2 += 1
        if verif_1 == 3 or verif_2 == 3:
            print('Temos um vencedor')
            imprimeTabuleiro(tabuleiro)
            return tabuleiro, exit()
        else:
            verif_1, verif_2 = 0, 0

    for i in range(3):
        if tabuleiro[i][i] != '.':
            if tabuleiro[i][i] == 'x':
                verif_1 += 1
            else:
                verif_2 += 1
    if verif_1 == 3 or verif_2 == 3:
        print('Temos um vencedor')
        imprimeTabuleiro(tabuleiro)
        return tabuleiro, exit()
    else:
        verif_1, verif_2 = 0, 0

    z = 2

    for i in range(3):
        if tabuleiro[i][z] != '.':
            if tabuleiro[i][z] == 'x':
                verif_1 += 1
            else:
                verif_2 += 1
    if verif_1 == 3 or verif_2 == 3:
        print('Temos um vencedor')
        imprimeTabuleiro(tabuleiro)
        return tabuleiro, exit()
    else:
        verif_1, verif_2 = 0, 0


def verificaVelha(tabuleiro):
    verif = 0
    for i in range(3):
        for j in range(3):
            if tabuleiro[i][j] == '.':
                verif += 1
    if verif == 0:
        print('Deu velha!')
        imprimeTabuleiro(tabuleiro)
        return  exit()


def main():
    velha, flag = False, False
    jogador = 2
    tabuleiro = geraTabuleiro()
    imprimeTabuleiro(tabuleiro)

    while velha == False and flag == False:
        if (jogador % 2) == 0:
            print('Vez do jogador 1')
            linha = int(input('Linha: '))-1
            coluna = int(input('Coluna: '))-1
            tabuleiro, flag = jogar(tabuleiro, jogador, linha, coluna)
            verificaGanhador(tabuleiro)
            verificaVelha(tabuleiro)
            imprimeTabuleiro(tabuleiro)
            if flag == True:
                jogador += 1
                flag = False

        else:
            print('Vez do jogador 2')
            linha = int(input('Linha: '))-1
            coluna = int(input('Coluna: '))-1
            tabuleiro, flag = jogar(tabuleiro, jogador, linha, coluna)
            verificaGanhador(tabuleiro)
            verificaVelha(tabuleiro)
            imprimeTabuleiro(tabuleiro)
            if flag == True:
                jogador += 1
                flag = False

main()
