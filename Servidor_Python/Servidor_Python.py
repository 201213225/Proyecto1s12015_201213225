from Estructuras import *
from flask import Flask, jsonify, session, request, render_template, Response
import json
import uuid
import random

app = Flask(__name__)

class Plane(object):
    '''Object that we use to model planes with name, id, and status.'''
    STATUS_STRINGS = ["flying", "landing"]

    def __init__(self, name, model):
        self.id = uuid.uuid4()
        self.name = name.title()
        self.model = model
        self.status = 0


    def create_public_view(self):
        return {"nombre": self.name, "id": int(self.id), "status": Plane.STATUS_STRINGS[self.status]}

lista = None

@app.route('/')
def imprimir():
    imprimir = ""
    aux = lista.raiz.nombre
    return str(aux)
    '''while aux!= None:
        pass
    return "hola"+str(nombre)+str(apellido)'''
def armar(raiz):
    a = ""
    return a
@app.route('/cliente/agregar/<nombre>/<password>/<int:nickname>/<direccion>/<int:telefono>/<int:credito>/<actual>')
def reenviar(nombre,password,nickname,direccion,telefono,credito,actual):
    lista = ArbolAVL()
    lista.incertar(str(nombre),str(password),nickname,str(direccion),telefono,credito,str(actual))
    return "hola su nombre actual es:"+str(nombre)+" contrasena:"+str(password)+" nickname:"+str(nickname)+" y su direccion es:"+str(actual)

@app.route('/intento')
def projects():

    '''
    try:
        arbol = ArbolAVL()

        arbol.incertar("Jose","svesv",100,"SMP",555,"credo","VNueva")
        arbol.incertar("Dose","svesv",101,"SMP",655,"credo","VNueva")
        arbol.incertar("Meme","svesv",90,"SMP",355,"credo","VNueva")
        #resultado = [{'param':'foo','val':3},{'param':'ads','val':7}]
        #return jsonify(results=resultado)
        resultado = {'nombre':arbol.raiz.izq.nombre,'nickname':arbol.raiz.izq.nickname,'pass':arbol.raiz.izq.password,'direccion':arbol.raiz.izq.direccion,'telefono':arbol.raiz.izq.tel,'TarjetaCed':arbol.raiz.izq.card,'DireccActual':arbol.raiz.izq.Adireccion}
        return jsonify(results=resultado)
        return arbol.raiz.izq.nombre +"\n"+arbol.raiz.izq.izq.nombre
    except ValueError:
        return "ValueError"
    except IOError:
        return "IOError"
    '''

@app.route('/about')
def about():
    return 'The about page'

planes_list = []

@app.route('/aviones/agregar', methods=['POST'])
def create_plane():
  '''Creates a plane instance based on a POST form with name and model set, returns the object.

  Useage sample: $ curl -X POST -d "name=avioncio&model=797-5000" http://localhost:5000/aviones/agregar
  '''

  name_sent = request.form['name']
  model_sent = request.form['model']
  plane = Plane(name_sent, model_sent)
  app.logger.debug(plane.create_public_view())
  planes_list.append(plane)
  return jsonify(plane.create_public_view())



if __name__ == '__main__':
    app.run()