


tabuleiro = [str(i) for i in range(1, 10)]


COMBINACOES_VENCEDORAS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),  # linhas
    (0, 3, 6), (1, 4, 7), (2, 5, 8),  # colunas
    (0, 4, 8), (2, 4, 6),             # diagonais
]


def mostrar_tabuleiro():
    """Imprime o tabuleiro atual na tela."""
    print()
    print(f" {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---+---+---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---+---+---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} ")
    print()


def jogada_valida(posicao):
    """Verifica se a posição escolhida está livre e dentro do intervalo."""
    if posicao < 0 or posicao > 8:
        return False
    return tabuleiro[posicao] not in ("X", "O")


def verificar_vencedor(simbolo):
    """Confere se o símbolo (X ou O) completou alguma combinação vencedora."""
    for combinacao in COMBINACOES_VENCEDORAS:
        a, b, c = combinacao
        if tabuleiro[a] == tabuleiro[b] == tabuleiro[c] == simbolo:
            return True
    return False


def tabuleiro_cheio():
    """Verifica se não há mais espaços livres (empate)."""
    return all(casa in ("X", "O") for casa in tabuleiro)


def pedir_posicao(jogador):
    """Pede ao jogador uma posição válida e retorna o índice (0 a 8)."""
    while True:
        entrada = input(f"Jogador {jogador}, escolha uma posição (1-9): ")
        if not entrada.isdigit():
            print("Digite um número entre 1 e 9.")
            continue
        posicao = int(entrada) - 1  # ajusta para índice da lista (0 a 8)
        if jogada_valida(posicao):
            return posicao
        print("Posição inválida ou já ocupada. Tente novamente.")


def jogar():
    """Loop principal do jogo."""
    jogador_atual = "X"

    print("=== JOGO DA VELHA ===")
    mostrar_tabuleiro()

    while True:
        posicao = pedir_posicao(jogador_atual)
        tabuleiro[posicao] = jogador_atual
        mostrar_tabuleiro()

        if verificar_vencedor(jogador_atual):
            print(f"🎉 Jogador {jogador_atual} venceu!")
            break

        if tabuleiro_cheio():
            print("Empate! Ninguém venceu.")
            break

        
        jogador_atual = "O" if jogador_atual == "X" else "X"

    jogar_novamente = input("Jogar de novo? (s/n): ").strip().lower()
    if jogar_novamente == "s":
        
        for i in range(9):
            tabuleiro[i] = str(i + 1)
        jogar()
    else:
        print("Obrigado por jogar!")


if __name__ == "__main__":
    jogar()
