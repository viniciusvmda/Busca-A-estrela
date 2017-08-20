class Cidade:
	
	nome = ''
	proximas = []				# Lista com as próximas cidades
	visitada = False			# Informa se a cidade já foi visitada (true)
	menor_anterior = None
	g = 0						# Distancia percorrida desde a cidade de origem
	h = 0						# Heurística
	f = 0						# Custo total


	def __init__(nome, visitada, g, h):
		self.nome = nome
		self.g = g
		self.h = h
		self.f = g + h


	def toString()
		return self.nome + "\nf = g + h\n" + (self.g + self.h) + ' = ' + self.g + ' + ' + self.h