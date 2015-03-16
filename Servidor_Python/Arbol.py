__author__ = 'Denis'
from Nodo import *
class ArbolAVL():
    raiz = None

    def incertar(self,nombre,password,nickname,direccion,telefono,card,Adireccion):
        if(self.raiz is None):
            #a = "holaa"
            self.raiz = NodoAVL()
            self.raiz.NodoAVL(nombre,password,nickname,direccion,telefono,card,Adireccion)
        else:
            aux = NodoAVL()
            aux.NodoAVL(nombre,password,nickname,direccion,telefono,card,Adireccion)
            self.raiz.incertar(aux)

