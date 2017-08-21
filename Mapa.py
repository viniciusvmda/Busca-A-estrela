#####################################################
#	Laboratorio de Inteligencia Artificial
#
#	Alunos:	Renan Mateus Bernardo do Nascimento
#			Vinicius Magalhaes D'Assuncao
#
#####################################################

import operator

from Dicionario import Dicionario
from Cidade import Cidade


class Mapa:

	mapa = {}
	arvore = None
	cidades_expandidas = []


	''' 
		Adiciona a rota ao mapa
		As cidades origem e destino serao indices do dicionario
	'''

	def adicionarRota(self, origem, destino, distancia):
		# Eh necessario adicionar um dicionario vazio caso nao exista o indice
		if not origem in self.mapa:
			self.mapa[origem] = {}

		if not destino in self.mapa:
			self.mapa[destino] = {}

		self.mapa[origem][destino] = distancia
		self.mapa[destino][origem] = distancia


	'''
		Le as rotas do mapa de um arquivo
		Arquivo esta no formato: "origem,destino,distancia"
	'''
	def montarMapa(self, nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		for linha in arquivo:
			rota = linha.split(',')
			self.adicionarRota(rota[0], rota[1], int(rota[2][:-1]))


	# Expande as cidades do no origem e retorna qual tem o menor custo
	def vaiProximaCidade(self, origem):
		adjacentes = self.mapa[origem.nome]
		# Se possuir cidades adjacentes
		if adjacentes:
			# Verifica qual a cidade com menor distancia dentre as adjacentes
			for cidade in adjacentes:
				distancia = adjacentes[cidade]
				g = origem.g + distancia
				h = Dicionario.distancia_reta[cidade]

				# Salva a cidade na arvore
				C = Cidade(cidade, origem, g, h)
				origem.adjacentes.append(C)

				# Coloca na lista de cidades expandidas
				self.cidades_expandidas.append(C)

			self.cidades_expandidas = sorted(self.cidades_expandidas, key=operator.attrgetter('f'))

			# Pega a primeira cidade adjacente como menor distancia
			menor = self.cidades_expandidas.pop(0)
			return menor



	def andarMapa(self, origem, destino):
		self.cidades_expandidas = []
		anterior = None
		g = 0
		h = Dicionario.distancia_reta[origem]
		self.arvore = Cidade(origem, anterior, g, h)
		cidade = self.arvore				# ponteiro da arvore

		while (cidade.nome != destino):
			# busca cidade com menor distancia
			cidade = self.vaiProximaCidade(cidade)

		self.imprimirPercurso(cidade)


	def imprimirPercurso(self, destino):
		percurso = [destino]
		cidade = destino
		while cidade.anterior != None:
			cidade = cidade.anterior
			percurso.insert(0, cidade)
		for cidade in percurso:
			print cidade.toString()
			print '\n\n'


	def imprimirMapa(self):
		print 'Mapa: \n', self.mapa,'\n'