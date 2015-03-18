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

class NodoVuelo():
    llegada = ""
    Hsalida = ""
    Hllegada = ""
    Primera = 0
    Turista = 0
    Ejecutiva = 0
    estado = "En areopuerto"
    id  = 0
    izq = None
    der = None
    def asignar(self, llegada, Hsalida, Hllegada, Primera, Turista, Ejecutiva, id):
        self.llegada = llegada
        self.Hsalida = Hsalida
        self.Hllegada = Hllegada
        self.Primera = Primera
        self.Turista = Turista
        self.Ejecutiva = Ejecutiva
        self.id = id
    def incertar(self,nuevo):
        if nuevo.id < self.id:
            if self.izq is None:
                self.izq = nuevo
            else:
                self.izq.incertar(nuevo)
        else:
            if self.der is None:
                self.der = nuevo
            else:
                self.der.incertar(nuevo)

class NodoAereopuerto():
    nombre = ""
    pais = ""
    password = ""
    sig = None
    ant = None
    raiz = None
    def asignar(self,nombre,pais,password):
        self.nombre = nombre
        self.pais = pais
        self.password = password
    def incertarV(self,llegada,Hsalida,Hllegada,Primera,Turista,Ejecutiva,id):
        if self.raiz is None:
            self.raiz = NodoVuelo()
            self.raiz.asignar(llegada,Hsalida,Hllegada,Primera,Turista,Ejecutiva,id)
        else:
            nuevo = NodoVuelo()
            nuevo.asignar(llegada,Hsalida,Hllegada,Primera,Turista,Ejecutiva,id)
            self.raiz.incertar(nuevo)

class Aeropueros():
    raiz = None
    ids = 0
    def incertarA(self,nombre,pais,password):
        if self.raiz is None:
            self.raiz = NodoAereopuerto()
            self.raiz.asignar(nombre,pais,password)
        else:
            aux = self.raiz
            while aux.sig != None:
                aux = aux.sig
            aux.sig = NodoAereopuerto()
            aux.sig.asignar(nombre,pais,password)
    def invertarV(self,nombre,llegada,Hsalida,Hllegada,Primera,Turista,Ejecutiva,id):
        if self.raiz != None:
            if self.raiz.nombre == "nombre":
                self.raiz.incertarV(llegada,Hsalida,Hllegada,Primera,Turista,Ejecutiva,id)
            else:
                aux = self.raiz
                while aux != None and aux.nombre != nombre:
                    aux = aux.sig
                if aux != None:
                    aux.incertarV(llegada,Hsalida,Hllegada,Primera,Turista,Ejecutiva,id)