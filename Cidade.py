'''#####################################################
#	Laboratorio de Inteligencia Artificial
#
#	Alunos:	Renan Mateus Bernardo do Nascimento
#			Vinicius Magalhaes D'Assuncao
#
'''#####################################################

class Cidade:
	
	nome = ''
	adjacentes = []				# Lista com as adjacentes cidades
	visitada = False			# Informa se a cidade ja foi visitada (true)
	menor_anterior = None
	g = 0						# Distancia percorrida desde a cidade de origem
	h = 0						# Heuristica
	f = 0						# Custo total


	def __init__(self, nome, visitada, g, h):
		self.nome = nome
		self.g = g
		self.h = h
		self.f = g + h


	def toString(self):
		return self.nome + "\nf = g + h\n" + (self.g + self.h) + ' = ' + self.g + ' + ' + self.h