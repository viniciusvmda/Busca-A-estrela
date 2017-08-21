'''#####################################################
#	Laboratorio de Inteligencia Artificial
#
#	Alunos:	Renan Mateus Bernardo do Nascimento
#			Vinicius Magalhaes D'Assuncao
#
'''#####################################################

from Dicionario import Dicionario
from Cidade import Cidade


class Mapa:

	mapa = {}
	arvore = None


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


	'''
		Compara o menor custo com todas as cidades nao visitadas de niveis superiores
		Se houver algum com custo inferior, volta para esta cidade
	'''
	def comparaCidadesAnteriores(self, origem, menor, cidade):
		outra_menor = menor

		# Percorre as adjacentes cidades
		for c in cidade.adjacentes:
			# Verifica se o custo da cidade eh menor
			if not c.visitada and c.nome != origem and c.f < outra_menor[1]:
				outra_menor = (c.nome, c.f)
			# Se a cidade tiver cidades adjacentes utiliza recursao
			if c.adjacentes:
				aux = self.comparaCidadesAnteriores(origem, outra_menor, c)
				if aux.f < outra_menor[1]:
					outra_menor = aux

		return outra_menor


	# Expande as cidades do no origem e retorna qual tem o menor custo 
	def vaiProximaCidade(self, origem):
		adjacentes = self.mapa[origem.nome]
		# Se possuir cidades adjacentes
		if adjacentes:					
			# Pega a primeira cidade adjacente como menor distancia
			aux = adjacentes.keys()[0]
			menor = (aux, adjacentes[aux] + Dicionario.distancia_reta[aux])			# (nome, distancia)
			
			# Verifica qual a cidade com menor distancia dentre as adjacentes
			for cidade in adjacentes:
				distancia = adjacentes[cidade]
				g = origem.g + distancia
				h = Dicionario.distancia_reta[cidade]

				# Salva a cidade na arvore
				C = Cidade(cidade, False, g, h)
				origem.adjacentes.append(C)

				if C.f < menor[1] and not C.visitada:
					menor = (cidade, C.f)
				
		else:
			menor = None

		print self.arvore.nome
		print origem.nome

		# Se a origem for a raiz da arvore nao precisa verificar
		if self.arvore.nome != origem.nome:
			menor = self.comparaCidadesAnteriores(origem, menor, self.arvore)
		
		# Retorna o nome da menor cidade
		return menor[0]




	def andarMapa(self, origem, destino):
		visitada = True
		g = 0
		h = Dicionario.distancia_reta[origem]
		self.arvore = Cidade(origem, visitada, g, h)

		cidade = self.arvore
		
		while (cidade.nome != destino):
			# busca cidade com menor distancia
			proxima = self.vaiProximaCidade(cidade)
			for c in cidade.adjacentes:
				if c.nome == proxima:
					c.visitada = True
					cidade = c
					achou = True
					break
			# Verifica em niveis superiores
			#if not achou:
	

	def imprimirArvore(self):
		print 'Arvore: \n', self.arvore,'\n'

	def imprimirMapa(self):
		print 'Mapa: \n', self.mapa,'\n'