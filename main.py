# coding: utf-8
# Nome: João Marcos Lima Mederios
# Matrícula: 117110317
# Atividade: Damas

import pygame
from pygame.locals import *
from sys import exit
import os

pygame.init()

tela = pygame.display.set_mode((1024, 768), 0, 32)
seta_baixo = pygame.image.load('assets' + os.sep + 'baixo.png')
peca_preta = pygame.image.load('assets' + os.sep + 'peca_preta.png')
peca_vermelha = pygame.image.load('assets' + os.sep + 'peca_vermelha.png')
dama_preta = pygame.image.load('assets' + os.sep + 'tabuleiro.png')
dama_vermelha = pygame.image.load('assets' + os.sep + 'tabuleiro.png')
plano_de_fundo = pygame.image.load('assets' + os.sep + 'tabuleiro.png')
tabuleiro = [[0, 2, 0, 2, 0, 2, 0, 2],
			[2, 0, 2, 0, 2, 0, 2, 0],
			[0, 2, 0, 2, 0, 2, 0, 2],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0],
			[1, 0, 1, 0, 1, 0, 1, 0],
			[0, 1, 0, 1, 0, 1, 0, 1],
			[1, 0, 1, 0, 1, 0, 1, 0]]
def split_int(string):
	lista = string.split()
	for a in range(len(lista)):
		lista[a] = int(lista[a])
	return lista
def popular_tabuleiro (tipo):
	global tabuleiro
	global peca_preta
	global peca_vermelha
	global dama_preta
	global dama_vermelha
	global plano_de_fundo
	global jogador_da_vez
	if tipo == 0:
		global tela
		tela.blit(plano_de_fundo, (0, 0))
		tela.blit(jogador_da_vez, (10,20))
		for i in range(8):
			for a in range(8):
				if tabuleiro[i][a] == 1:
					tela.blit(peca_vermelha, (203 + a * 78, 74 + i * 78))
				elif tabuleiro[i][a] == 2:
					tela.blit(peca_preta, (203 + a * 78, 74 + i * 78))
				elif tabuleiro[i][a] == 3:
					tela.blit(dama_vermelha, (203 + a * 78, 74 + i * 78))
				elif tabuleiro[i][a] == 4:
					tela.blit(dama_preta, (203 + a * 78, 74 + i * 78))
				elif tabuleiro[i][a] == 5:
					tela.blit(seta_baixo, (203 + a * 78, 74 + i * 78))
	else:
		print "   ", [0, 1, 2, 3, 4, 5, 6, 7]
		print ""
		for i in range(len(tabuleiro)):
			print [i], tabuleiro[i]
def formatar_tabuleiro():
	global tabuleiro
	for i in range(8):
		for a in range(8):
			if tabuleiro[i][a] == 5:
				tabuleiro[i][a] = 0
def movimentos_possiveis(coords, tipo, permissao):
	#tipo: 0 = pode tudo, 1 = pode só capturar
	tem_movimentos = False
	global tabuleiro
	global pecas_para_remover
	print "i, a, tabuleiro[i][a]"
	for i in range(8):
		for a in range(8):
			peca_central = ((i + coords[0])/ 2, (a + coords[1])/ 2)
			print i, a, tabuleiro[i][a] 
			# Quando a peça não é uma dama
			if tipo <= 2:
				if permissao == 0 and i == coords[0] + (2 * tipo - 3) and tabuleiro[i][a] == 0 and abs(a - coords[1]) == 1:
					tabuleiro[i][a] = 5
					tem_movimentos = True
				if abs(i - coords[0]) == 2 and abs(a - coords[1]) == 2 and tabuleiro[i][a] == 0:
					print "passou da parte 1"
					if tabuleiro[peca_central[0]][peca_central[1]] == (-1 * tipo + 3) or tabuleiro[peca_central[0]][peca_central[1]] == (-1 * tipo + 3):
						print "passou da 2"
						if not((i, a) in movimentos) and not(peca_central in pecas_para_remover):
							print "passou da 3"
							tabuleiro[i][a] = 5
							tem_movimentos = True
							possiveis_remocoes[(i, a)] = ((i + coords[0])/ 2, (a + coords[1])/ 2)
			#else:
				#if i - a == coords[0] - coords[1] and tabuleiro[i][a] == 0:
					#for b in range(abs(i - coords[0])):
						#if tabuleiro[i + b][a + b] == (-1 * (tipo - 2) + 3):
					
			#Quando a peça é uma dama
			
			#else:
	popular_tabuleiro(0)
	
	return tem_movimentos
def iniciar_jogada():
	jogada_em_andamento = True
def finalizar_jogada():
	jogada_em_andamento = False
	print "chegou aqui"
	global movimentos
	print movimentos
	print tabuleiro[movimentos[0][0]][movimentos[0][1]]
	print tabuleiro[movimentos[-1][0]][movimentos[-1][1]]
	tabuleiro[movimentos[0][0]][movimentos[0][1]], tabuleiro[movimentos[-1][0]][movimentos[-1][1]] = tabuleiro[movimentos[-1][0]][movimentos[-1][1]], tabuleiro[movimentos[0][0]][movimentos[0][1]]
	popular_tabuleiro(1)
	popular_tabuleiro(0)
	formatar_tabuleiro()
	movimentos = []
	global clique
	global item
	global jogador
	clique, item = False, False
	global possiveis_remocoes
	global pecas_para_remover
	for a in pecas_para_remover:
		tabuleiro[a[0]][a[1]] = 0
	if jogador:
		jogador = 0
	else:
		jogador = 1
	pecas_para_remover = []
	possiveis_remocoes = dict()
	print "peças para remover: ", pecas_para_remover
	print "possiveis_remocoes: ", possiveis_remocoes
	print "movimentos: ", possiveis_remocoes
	print "jogador: ", (jogador * -1 + 2)
	
	popular_tabuleiro(1)
	popular_tabuleiro(0)
def mapeia_clique (mouse_pos):
	for i in range(8):
		for a in range(8):
			if abs(mouse_pos[0] - (240 + a * 78)) <= 39 and abs(mouse_pos[1] - (110 + i * 78)) <= 39:
				if (i + a) % 2 == 1:
					return (i, a)
	return False
#vermelha: 1 - preta: 2 - damavermelha: 3 - damapreta: 4 - espaco_vazio: 0


pygame.display.set_caption('PyDamas')
movimentos = []
pecas_para_remover = []
possiveis_remocoes = dict()
jogador = 1
jogada_em_andamento = False
local = ""
clique = False
verde = (0, 255, 0)
font = pygame.font.SysFont("courrier new", 30, bold = False)	
jogador_da_vez = font.render("Hello World", True, verde)
while True:
	# Ver evento de saída
	for event in pygame.event.get():
		if event.type == QUIT:
			exit()
	# Atualizar tabuleiro
	popular_tabuleiro(0)
	mouse_pos = pygame.mouse.get_pos()
	mouse_press = pygame.mouse.get_pressed()
	# Receber peça para mover
	jogador_da_vez = font.render("Vez do jogador %i" % (jogador * -1 + 2), True, verde)
	if jogada_em_andamento and clique == False:
		print "jogada em andamento e clique == false"
		popular_tabuleiro(1)
		item = False
		jogada_em_andamento = False
		formatar_tabuleiro()
	if mouse_press[0]:
		popular_tabuleiro(1)
		clique = mapeia_clique(mouse_pos)
		if clique:
			print "clicou em (%i, %i)" % (clique[0], clique[1])
			item = tabuleiro[clique[0]][clique[1]]
	if clique and item == 5:
		print "clicou num movimento possivel"
		popular_tabuleiro(1)
		if possiveis_remocoes.get((clique[0], clique[1]), False):
			print "e esse movimento remove uma peça"
			popular_tabuleiro(1)
			pecas_para_remover.append(possiveis_remocoes.get((clique[0], clique[1])))
		movimentos.append((clique[0], clique[1]))
		formatar_tabuleiro()
		if len(pecas_para_remover) == 0:
			finalizar_jogada()
			print "finalizou jogada porque não tem como andar mais de uma casa"
			popular_tabuleiro(1)
		else:
			if not(movimentos_possiveis(clique, tabuleiro[movimentos[0][0]][movimentos[0][1]], 1)):
				print "finalizou jogada porque não ezistem mais movimentos possíveis"
				popular_tabuleiro(1)
				finalizar_jogada()
	elif clique and item != 0 and item % 2 == jogador:
		pecas_para_remover = []
		possiveis_remocoes = dict()
		print "clicou em uma peça sua"
		popular_tabuleiro(1)
		movimentos = [(clique[0], clique[1])]
		formatar_tabuleiro()
		if movimentos_possiveis(clique, item, 0):
			print "existem movimentos possiveis"
			popular_tabuleiro(1)
			clique = False
			iniciar_jogada()
	popular_tabuleiro(0)
	pygame.display.update()
