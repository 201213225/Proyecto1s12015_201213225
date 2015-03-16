from flask import Flask
from Arbol import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    return "hola"

@app.route('/intento')
def projects():
    try:
        arbol = ArbolAVL()

        arbol.incertar("Jose","svesv","pepe","SMP",555,"credo","VNueva")
        arbol.incertar("Dose","svesv","pepe","SMP",455,"credo","VNueva")
        arbol.incertar("Meme","svesv","pepe","SMP",355,"credo","VNueva")

        return arbol.raiz.izq.izq.nombre
    except ValueError:
        return "ValueError"
    except IOError:
        return "IOError"

@app.route('/about')
def about():
    return 'The about page'
if __name__ == '__main__':
    app.run()


