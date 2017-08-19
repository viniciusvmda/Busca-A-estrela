class Mapa:

	mapa = {}

	def __init__():
		pass

	# Adiciona a rota ao mapa
	def adicionarRota(origem, destino, distancia):
		if not origem in mapa:
			mapa[origem] = {}

		if not destino in mapa:
			mapa[destino] = {}

		mapa[origem][destino] = distancia
		mapa[destino][origem] = distancia


	def montarMapa(nome_arquivo):
		arquivo = open(nome_arquivo, 'r')
		for rota in arquivo:
			

