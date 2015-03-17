from flask import Flask, jsonify
from Arbol import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hola"

@app.route('/intento')
def projects():
    try:
        arbol = ArbolAVL()

        arbol.incertar("Jose","svesv",100,"SMP",555,"credo","VNueva")
        arbol.incertar("Dose","svesv",99,"SMP",455,"credo","VNueva")
        arbol.incertar("Meme","svesv",98,"SMP",355,"credo","VNueva")
        #resultado = [{'param':'foo','val':3},{'param':'ads','val':7}]
        #return jsonify(results=resultado)
        resultado = {'nombre':arbol.raiz.nombre,'nickname':arbol.raiz.nickname,'pass':arbol.raiz.password,'direccion':arbol.raiz.direccion,'telefono':arbol.raiz.tel,'TarjetaCed':arbol.raiz.card,'DireccActual':arbol.raiz.Adireccion}
        return jsonify(results=resultado)
        return arbol.raiz.izq.nombre +"\n"+arbol.raiz.izq.izq.nombre
    except ValueError:
        return "ValueError"
    except IOError:
        return "IOError"

@app.route('/about')
def about():
    return 'The about page'
if __name__ == '__main__':
    app.run()


