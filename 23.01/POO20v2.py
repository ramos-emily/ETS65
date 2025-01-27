#aqui so tentei fazer uma versao com tkinter, mas nao funcionou

import tkinter as tk
from tkinter import messagebox

class Peca:
    def __init__(self, cor):
        self.cor = cor

class Peao(Peca):
    def __init__(self, cor):
        super().__init__(cor)

    def movimentos_validos(self, posicao, tabuleiro):
        movimentos = []
        direcao = 1 if self.cor == 'branca' else -1

        # Para frente
        if tabuleiro.posicao_vazia(posicao[0] + direcao, posicao[1]):
            movimentos.append((posicao[0] + direcao, posicao[1]))

        # Diagonal
        for i in [-1, 1]:
            if 0 <= posicao[1] + i < 8 and tabuleiro.posicao_ocupada(posicao[0] + direcao, posicao[1] + i):
                movimentos.append((posicao[0] + direcao, posicao[1] + i))
        
        return movimentos

class Tabuleiro:
    def __init__(self, root):
        self.root = root
        self.tabuleiro = [[None] * 8 for _ in range(8)]
        self.buttons = []
        self.setup_tabuleiro()

    def setup_tabuleiro(self):
        for linha in range(8):
            row_buttons = []
            for coluna in range(8):
                button = tk.Button(self.root, text="", width=4, height=2, command=lambda l=linha, c=coluna: self.selecionar_peca(l, c))
                button.grid(row=linha, column=coluna)
                row_buttons.append(button)
            self.buttons.append(row_buttons)

    def colocar_peca(self, peca, linha, coluna):
        self.tabuleiro[linha][coluna] = peca
        button = self.buttons[linha][coluna]
        button.config(text=self.get_peca_symbol(peca), state=tk.NORMAL)

    def get_peca_symbol(self, peca):
        if isinstance(peca, Peao):
            return "P" if peca.cor == "branca" else "p"
        return ""

    def posicao_vazia(self, linha, coluna):
        return self.tabuleiro[linha][coluna] is None

    def posicao_ocupada(self, linha, coluna):
        return self.tabuleiro[linha][coluna] is not None

    def selecionar_peca(self, linha, coluna):
        peca = self.tabuleiro[linha][coluna]
        if peca is not None:
            messagebox.showinfo("Seleção", f"Peça selecionada: {peca.cor} {peca.__class__.__name__}")
        else:
            messagebox.showinfo("Seleção", "Posição vazia!")

root = tk.Tk()
root.title("Jogo de Xadrez")

tabuleiro = Tabuleiro(root)


tabuleiro.colocar_peca(Peao('branca'), 1, 0)  
tabuleiro.colocar_peca(Peao('preta'), 6, 0)  
root.mainloop()
