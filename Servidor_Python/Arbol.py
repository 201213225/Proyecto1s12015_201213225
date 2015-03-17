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
    def equilibrado(self,raiz):
        if raiz != None:
            izq = self.equilibrado(self.raiz.izq)
            der = self.equilibrado(self.raiz.der)
            return 2
        else:
            return 0