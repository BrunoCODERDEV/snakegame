# Configurações iniciais
import pygame as pyg
import random as ra

pyg.init()
pyg.display.set_caption("Snake Project Python")
largura, altura = 600, 400
pyg.display.set_mode((largura, altura))
relogio = pyg.time.Clock()



# cores RGB 
azul = (0, 0, 255)
verde =  (0, 255, 0)
preta = (0, 0, 0)
branca = (255, 255, 255)
vermelho = (255, 0, 0)

# parametro da cobrinha
tamanho_quadrado = 10
velocidade_quadrado = 16

def rodar_jogo():
 fim_jogo = False

 while not fim_jogo:
  pass
 
for evento in  pyg.event.get():
 if evento.type == pyg.QUIT:
  fim_jogo = True
  # criar um loop/infinito

# desenhar os objetos do jogo na tela
# pontuação
# cobrança
# comida

# criar a logica de terminar o jogo
# o que acontece:
# cobra bateu na parede
# cobra bateu na propria cobra

# pegar a interações do usuario
# fechou a tela
# apertou as teclas do teclado pra mover a cobra

 rodar_jogo()