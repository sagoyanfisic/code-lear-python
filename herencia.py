class Animal(object):
	def __init__(self, nombre):
		self.nombre = nombre

	def imprimirNonbre(self):
		print "Nombre",self.nombre

class Canino(Animal):
	def __init__(self,nombre):
		super(Canino,self).__init__(nombre)
		self.patas = 4
		self.tipo = "Canino"

perro = Canino("Toby")
perro.imprimirNonbre()
