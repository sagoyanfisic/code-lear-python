class animal:


	def __init__(self,nombre=None, patas=4):
		self.nombre = nombre
		self.patas = patas
		self.tipo = "can"



x = animal("LOLO",2)
y = animal("MANIA")		

print x.nombre,x.patas,x.tipo
print y.nombre,y.patas,y.tipo

	
		