from graphviz import Digraph
class grafo:
	#global dot
	
	def __init__(self,nombre):
		self.dot = None
		self.dot = Digraph(comment=nombre)
		self.dot = Digraph(format='svg')

		#dot = Digraph(comment=nombre)
#dot  #doctest: +ELLIPSIS
	def declararNodos(self,numero,valor):
		self.dot.node(str(numero), str(valor))

	def declararNodo(self,valor):
		self.dot.node(str(valor))

	def declararTrancisiones(self, actual,siguiente):
		self.dot.edge(str(actual),str(siguiente))

	def terminarGrafo(self,nombre):
		self.dot.render('Grafos/'+nombre, view=False)