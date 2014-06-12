#!/usr/bin/python2
# -*- coding: utf-8 -*-

#implementar la class singleton 
class Singleton(object):
    _instance = None
    #
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = object.__new__(cls, *args, **kwargs)
         
        return cls._instance

class Sexo():
	def imprimirla(self):
		print "",self.det
         
primera = Sexo()
segunda = Sexo()


primera.det = "mujer"
segunda.det = "hombre"
print primera.det, segunda.det # Gorrion Gorrion

if primera.det == segunda.det:
	print " estas usando Singleton"
else: 
    print "No esta usando Singleton"