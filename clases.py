

class perro:
	patas = int(raw_input("ingresa la cantidad de patas: "))
	nombre= " "

	def nombrar(self,n):
		self.nombre = n
		
mascota = perro()
mascota2 = perro()

print "tengo un perro, se llama %s y tiene %s patas"%(mascota.nombre,mascota.patas)
print "tengo otro perro, se llama %s y tiene %s patas"%(mascota2.nombre,mascota2.patas)

