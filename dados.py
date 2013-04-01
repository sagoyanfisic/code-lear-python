import random

while True :
    valor = raw_input("Tirar dados(Si(1) or No(0)) : ")
    if valor is "1" : 
        dado=random.randint(1,6)
        dado2=random.randint(1,6)
        print dado 
        print dado2
    if dado==dado2 :
        print "SOn iguales"
    elif valor is "0":   
      print "Encontraron dados seguro :( \n Apagando...."
      print "\nApagando..."*6
      break	
   
