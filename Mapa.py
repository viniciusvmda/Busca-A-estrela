'''#####################################################
#	Laboratório de Inteligência Artificial
#
#	Alunos:	Renan Mateus Bernardo do Nascimento
#			Vinícius Magalhães D'Assunção
#
'''#####################################################

from Dicionario import Dicionario
from Cidade import Cidade


class Mapa:

	mapa = {}
	arvore = {}
	destino = 'Bucareste'

	def __init__():
		pass


	''' 
		Adiciona a rota ao mapa
		As cidades origem e destino serão índices do dicionário
	'''
	def __adicionarRota(origem, destino, distancia):
		# É necessário adicionar um dicionario vazio caso não exista o índice
		if not origem in self.mapa:
			self.mapa[origem] = {}

		if not destino in self.mapa:
			self.mapa[destino] = {}

		self.mapa[origem][destino] = distancia
		self.mapa[destino][origem] = distancia


	'''
		Lê as rotas do mapa de um arquivo
		Arquivo está no formato: "origem,destino,distancia"
	'''
	def montarMapa(nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		for linha in arquivo:
			rota = linha.split(',')
			__adicionarRota(rota[0], rota[1], rota[2])


	'''
		Compara o menor custo com todas as cidades não visitadas de níveis superiores
		Se houver algum com custo inferior, volta para esta cidade
	'''
	def comparaCidadesAnteriores(origem, menor, cidade):
		outra_menor = menor

		# Percorre as proximas cidades
		for c in cidade.proximas:
			# Verifica se o custo da cidade é menor
			if not c.visitada and c.nome != origem and c.f < outra_menor[1]:
				outra_menor = (c.nome, c.f)
			# Se a cidade tiver cidades adjacentes utiliza recursao
			if c.proximas:
				aux = comparaCidadesAnteriores(origem, outra_menor, c)
				if aux.f < outra_menor[1]:
					outra_menor = aux

		return outra_menor


	# Expande as cidades do nó origem e retorna qual tem o menor custo 
	def vaiProximaCidade(origem):
		adjacentes = mapa[origem.nome]
		# Se possuir cidades adjacentes
		if adjacentes:					
			# Pega a primeira cidade adjacente como menor distancia
			aux = adjacentes.keys()[0]
			menor = (aux, adjacentes[aux])			# (nome, distancia)
			
			# Verifica qual a cidade com menor distância dentre as adjacentes
			for cidade, distancia in adjacentes:
				g = origem.g + distancia
				h = Dicionario.distancia_reta[cidade]
				
				# Salva a cidade na árvore
				C = Cidade(cidade, False, g, h)
				origem.proximas.append(C)

				if C.f < menor[1]:
					menor = (cidade, C.f)
				
		else:
			menor = None

		# Se a origem for a raiz da arvore não precisa verificar
		if arvore.nome != origem.nome:
			menor = comparaCidadesAnteriores(origem, menor)
		
		# Retorna o nome da menor cidade
		return menor[0]




	def andarMapa(origem):
		g = 0
		h = Dicionario.distancia_reta[origem]
		self.arvore = Cidade(cidade, True, g, h)

		cidade = arvore
		
		while (cidade.nome != destino):
			# busca cidade com menor distância
			proxima = vaiProximaCidade(cidade)
			for c in proximas:
				if c.nome == proxima
					c.visitada = True
					cidade = c
					achou = True
					break
			# Verifica em níveis superiores
			if not achou:
				