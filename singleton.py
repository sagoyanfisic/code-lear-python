#!/usr/bin/python2
# -*- coding: utf-8 -*-

import os
import sys
import tempfile

OS = None
if sys.platform.startswith('linux'):
    OS = 'linux'
    import fcntl
elif sys.platform.startswith('win32'):
    OS = 'windows'
    
class Singleton:
    def __init__(self):
        # Variable para almacenar el file descriptor
        self.fd = None
        # Ruta para el lock file en la carpeta temporal del sistema
        self.filepath = os.path.abspath(os.path.join(tempfile.gettempdir(), 
            'myapp.pid'))
        
        if OS == 'linux':
            # Para el caso de linux usamos el módulo fcntl para crear el archivo
            # y bloquearlo automáticamente. Si la operación falla es porque el
            # archivo ya existe y está bloqueado.
            self.fd = open(self.filepath, 'w')
            try:
                fcntl.lockf(self.fd, fcntl.LOCK_EX | fcntl.LOCK_NB)
            except IOError:
                self.__exit()
        elif OS == 'windows':
            try:
                # Para el caso windows simplemente creamos el archivo "a mano",
                # pero verificamos primero si el archivo existe e intentamos 
                # removerlo (para casos en que la ejecución previa haya sido 
                # interrumpida)
                if os.path.exists(self.filepath):
                    os.unlink(self.filepath)
                self.fd = os.open(self.filepath, os.O_CREAT|os.O_EXCL|os.O_RDWR)
            except OSError, err:
                if err.errno == 13:
                    self.__exit()
    
    def __del__(self):
        # Para el caso de windows también debemos destruir el archivo "a mano" 
        # al finalizar la ejecución del programa.
        if OS == 'windows':
            if self.fd:
                os.close(self.fd)
                os.unlink(self.filepath)
    
    def __exit(self):
        print 'Ya hay una instancia en ejecución. Saliendo'
        sys.exit(-1)

class MyApp(Singleton):
    def __init__(self):
        Singleton.__init__(self)
        print 'Ejecutando MyApp'
        # Creamos un bucle infinito solo para mantener la aplicación en
        # ejecución
        while 1:
            continue
    
if __name__ == '__main__':
    app = MyApp()