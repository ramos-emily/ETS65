# 20.	Implemente um jogo de tabuleiro em que cada peça (peões, torres, etc.) seja representada por uma classe, com regras específicas de movimento e captura. No caso do xadrez, adicione a regra de roque, en passant, promoção de peões e xeque-mate.

# super() chama o método __init__ da classe Peca e passa o valor de cor para ele, garantindo que o peão tenha o atributo cor inicializado corretamente.

class Peca():
    def __init__(self, cor):
        self.cor = cor

class Peao(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
        direcao = 1 if self.cor == 'branca' else -1

        #pra frente
        if tabuleiro.posicao_vazia(posicao[0] + direcao, posicao[1]):
            movimentos.append((posicao[0] + direcao, posicao[1]))

        #pra diagonal
        for i in [-1, 1]:
            if 0 <= posicao[1] + i < 8 and tabuleiro.posicao_ocupada(posicao[0] + direcao, posicao[1] + i):
                movimentos.append((posicao[0] + direcao, posicao[1] + i))
        
        return movimentos

class Cavalo(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
        movimentos_possiveis = [
            (posicao[0] + 2, posicao[1] + 1), (posicao[0] + 2, posicao[1] - 1),
            (posicao[0] - 2, posicao[1] + 1), (posicao[0] - 2, posicao[1] - 1),
            (posicao[0] + 1, posicao[1] + 2), (posicao[0] + 1, posicao[1] - 2),
            (posicao[0] - 1, posicao[1] + 2), (posicao[0] - 1, posicao[1] - 2),
        ]
        
        for movimento in movimentos_possiveis:
            if 0 <= movimento[0] < 8 and 0 <= movimento[1] < 8:
                if not tabuleiro.posicao_ocupada(movimento[0], movimento[1]):
                    movimentos.append(movimento)

        return movimentos

class Torre(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
    
        for i in range(1, 8):
            # Horizontal
            if tabuleiro.posicao_vazia(posicao[0], posicao[1] + i):
                movimentos.append((posicao[0], posicao[1] + i))
            if tabuleiro.posicao_vazia(posicao[0], posicao[1] - i):
                movimentos.append((posicao[0], posicao[1] - i))
            # Vertical
            if tabuleiro.posicao_vazia(posicao[0] + i, posicao[1]):
                movimentos.append((posicao[0] + i, posicao[1]))
            if tabuleiro.posicao_vazia(posicao[0] - i, posicao[1]):
                movimentos.append((posicao[0] - i, posicao[1]))
        
        return movimentos

class Bispo(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
        for i in range(1, 8):
            # Diagonais
            if tabuleiro.posicao_vazia(posicao[0] + i, posicao[1] + i):
                movimentos.append((posicao[0] + i, posicao[1] + i))
            if tabuleiro.posicao_vazia(posicao[0] - i, posicao[1] + i):
                movimentos.append((posicao[0] - i, posicao[1] + i))
            if tabuleiro.posicao_vazia(posicao[0] + i, posicao[1] - i):
                movimentos.append((posicao[0] + i, posicao[1] - i))
            if tabuleiro.posicao_vazia(posicao[0] - i, posicao[1] - i):
                movimentos.append((posicao[0] - i, posicao[1] - i))

        return movimentos

class Rainha(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
        torre = Torre(self.cor)
        bispo = Bispo(self.cor)

        movimentos += torre.movimentos_validos(posicao, tabuleiro)
        movimentos += bispo.movimentos_validos(posicao, tabuleiro)

        return movimentos

class Rei(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
        movimentos_possiveis = [
            (posicao[0] + 1, posicao[1]), (posicao[0] - 1, posicao[1]),
            (posicao[0], posicao[1] + 1), (posicao[0], posicao[1] - 1),
            (posicao[0] + 1, posicao[1] + 1), (posicao[0] - 1, posicao[1] - 1),
            (posicao[0] + 1, posicao[1] - 1), (posicao[0] - 1, posicao[1] + 1)
        ]

        for movimento in movimentos_possiveis:
            if 0 <= movimento[0] < 8 and 0 <= movimento[1] < 8:
                if not tabuleiro.posicao_ocupada(movimento[0], movimento[1]):
                    movimentos.append(movimento)

        return movimentos

class Tabuleiro:
    def __init__(self):
        self.tabuleiro = [[None] * 8 for _ in range(8)]

    def colocar_peca(self, peca, linha, coluna):
        self.tabuleiro[linha][coluna] = peca

    def posicao_vazia(self, linha, coluna):
        return self.tabuleiro[linha][coluna] is None

    def posicao_ocupada(self, linha, coluna):
        return self.tabuleiro[linha][coluna] is not None

    def movimento_valido(self, peca, posicao_atual, nova_posicao):
        movimentos_validos = peca.movimentos_validos(posicao_atual, self)
        return nova_posicao in movimentos_validos

    def exibir_tabuleiro(self):
        for linha in self.tabuleiro:
            for peca in linha:
                if peca is None:
                    print(" . ", end=" ")
                else:
                    print(f" {peca.__class__.__name__[0]} ", end=" ")
            print()

tabuleiro = Tabuleiro()
tabuleiro.colocar_peca(Rei('branca'), 0, 4)
tabuleiro.colocar_peca(Torre('preta'), 7, 0)
tabuleiro.exibir_tabuleiro()
