__author__ = 'Denis'
class NodoAVL():
    nombre = ""
    password = ""
    nickname = ""
    direccion = ""
    tel = 0
    card = ""
    Adireccion = ""
    izq = None
    der = None
    def NodoAVL(self,nombre,password,nickname,direccion,telefono,card,Adireccion):
        self.nombre = nombre
        self.password = password
        self.nickname = nickname
        self.direccion = direccion
        self.tel = telefono
        self.card = card
        self.Adireccion = Adireccion
    def incertar(self,nuevo):
        if self.nickname>nuevo.nickname:
            if self.izq is None:
                self.izq = nuevo

                #return "incertado"
            else:
                self.izq.incertar(nuevo)
        else:
            if self.der is None:
                self.der = nuevo
            else:
                self.der.incertar(nuevo)
                #return "incertado"

