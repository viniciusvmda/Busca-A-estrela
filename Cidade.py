#####################################################
#	Laboratorio de Inteligencia Artificial
#
#	Alunos:	Renan Mateus Bernardo do Nascimento
#			Vinicius Magalhaes D'Assuncao
#
#####################################################

class Cidade:
	
	nome = ''
	anterior = None				# Armazena a cidade anterior
	adjacentes = []				# Lista com as adjacentes cidades
	g = 0						# Distancia percorrida desde a cidade de origem
	h = 0						# Heuristica
	f = 0						# Custo total


	def __init__(self, nome, anterior, g, h):
		self.nome = nome
		self.anterior = anterior
		self.g = g
		self.h = h
		self.f = g + h


	def toString(self):
		return self.nome + "\nf = g + h\n" + str(self.g + self.h) + ' = ' + str(self.g) + ' + ' + str(self.h)