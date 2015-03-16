__author__ = 'Denis'

class ArbolALV():
    def __init__(self):
        self.raiz = NodoAVL()

class NodoAVL():
    def NodoAVL(self,nombre,password,nickname,direccion,telefono,card,Adireccion):
        self.nombre = nombre
        self.password = password
        self.nickname = nickname
        self.direccion = direccion
        self.tel = telefono
        self.card = card
        self.Adireccion = Adireccion
    def incertar(self,nuevo):
        if self.card>nuevo.card:
            self.izq=nuevo
        else:
            self.der=nuevo

