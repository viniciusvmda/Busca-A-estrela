#####################################################
#	Laboratorio de Inteligencia Artificial
#
#	Alunos:	Renan Mateus Bernardo do Nascimento
#			Vinicius Magalhaes D'Assuncao
#
#####################################################


from Mapa import Mapa

arquivo = 'mapa_cidades.txt'

mapa = Mapa()
mapa.montarMapa(arquivo)
mapa.andarMapa('lugoj', 'bucharest')