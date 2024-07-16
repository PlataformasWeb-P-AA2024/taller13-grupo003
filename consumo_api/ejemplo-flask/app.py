from flask import Flask, render_template
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/losedificios")
def los_edificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificios/",
            auth=(usuario,clave))
    edificios = json.loads(r.content)['results']
    numero_edificios = json.loads(r.content)['count']
    return render_template("losedificios.html", edificios=edificios,
    numero_edificios=numero_edificios)


@app.route("/losdepartamentos")
def los_departamentos():
    """
    """
    r = requests.get("http://127.0.0.1:5000/api/departamentos/",
            auth=(usuario,clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losdepartamentos.html", datos=datos,
    numero=numero)


@app.route("/losdepartamentosdos")
def los_departamentos_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
            auth=(usuario,clave))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'nombrePropietario':d['nombrePropietario'], 'costo':d['costo'],'numero_cuartos':d['numero_cuartos'],
        'edificio': obtener_edificio(d['edificio'])})
    return render_template("losdepartamentosdos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_edificio(url):
    """
    """
    r = requests.get(url, auth=(usuario,clave))
    nombre_edificio = json.loads(r.content)['nombre']
    direccion_edificio = json.loads(r.content)['direccion']
    cadena = "%s %s" % (nombre_edificio, direccion_edificio)
    return cadena

# Crear un edificio
@app.route("/crear_edificio_formulario")
def crear_edificio_formulario():
    return render_template("crearedificios.html")

@app.route("/crear_edificio", methods=['POST'])
def crear_edificio():
    nombre = request.form['nombre']
    direccion = request.form['direccion']
    payload = {'nombre': nombre, 'direccion': direccion}
    r = requests.post("http://127.0.0.1:8000/api/edificios/", data=payload, auth=(usuario, clave))
    return redirect('/losedificios')

# Editar un departamento
@app.route("/editar_departamento/<int:id>", methods=['GET'])
def editar_departamento_formulario(id):
    r = requests.get(f"http://127.0.0.1:8000/api/departamentos/{id}/", auth=(usuario, clave))
    datos = json.loads(r.content)
    return render_template("editar_departamento.html", datos=datos)

@app.route("/editar_departamento/<int:id>", methods=['POST'])
def editar_departamento(id):
    nombrePropietario = request.form['nombrePropietario']
    costo = request.form['costo']
    numero_cuartos = request.form['numero_cuartos']
    edificio = request.form['edificio']  # Ajusta según tu formulario
    payload = {
        'nombrePropietario': nombrePropietario,
        'costo': costo,
        'numero_cuartos': numero_cuartos,
        'edificio': edificio
    }
    r = requests.put(f"http://127.0.0.1:8000/api/departamentos/{id}/", data=payload, auth=(usuario, clave))
    return redirect('/losdepartamentosdos')

# Eliminar un departamento
@app.route("/eliminar_departamento/<int:id>", methods=['GET'])
def eliminar_departamento(id):
    r = requests.delete(f"http://127.0.0.1:8000/api/departamentos/{id}/", auth=(usuario, clave))
    return redirect('/losdepartamentosdos')