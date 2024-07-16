from flask import Flask, render_template, request,redirect, url_for
import requests
import json
from config import usuario, clave

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    r = requests.get("http://127.0.0.1:8000/api/departamentos/", auth=(usuario, clave))
    departamentos = json.loads(r.content)['results']
    return render_template("index.html", departamentos=departamentos)


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
    r = requests.get("http://127.0.0.1:8000/api/departamentos/",
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
#----------------------------------------

@app.route("/crear_edificio", methods=['GET', 'POST'])
def crear_edificio():
    if request.method == 'POST':
        nombre = request.form['nombre']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        tipo = request.form['tipo']
        data = {'nombre': nombre, 'direccion': direccion, 'ciudad': ciudad,'tipo': tipo}
        requests.post("http://127.0.0.1:8000/api/edificios/", data=data, auth=(usuario, clave))
        return redirect(url_for('los_edificios'))
    return render_template("crear_edificio.html")   

@app.route("/crear_departamento", methods=['GET', 'POST'])
def crear_departamento():
    if request.method == 'POST':
        nombrePropietario = request.form['nombrePropietario']
        costo = request.form['costo']
        numero_cuartos = request.form['numero_cuartos']
        edificio = request.form['edificio']
        data = {'nombrePropietario': nombrePropietario, 'costo': costo, 'numero_cuartos': numero_cuartos,'edificio': edificio}
        requests.post("http://127.0.0.1:8000/api/departamentos/", data=data, auth=(usuario, clave))
        return redirect(url_for('los_departamentos_dos'))
        # Obtener la lista de edificios disponibles
    r = requests.get("http://127.0.0.1:8000/api/edificios/", auth=(usuario, clave))
    edificios = json.loads(r.content)['results']
    return render_template("crear_departamento.html",edificios=edificios)
#-----------------------------------------------
@app.route("/editar_departamento/<int:id>", methods=['GET', 'POST'])
def editar_departamento(id):
    r = requests.get(f"http://127.0.0.1:8000/api/departamentos/{id}/", auth=(usuario, clave))
    departamento = json.loads(r.content)

    if request.method == 'POST':
        nombrePropietario = request.form['nombrePropietario']
        costo = request.form['costo']
        numero_cuartos = request.form['numero_cuartos']
        edificio = request.form['edificio']

        data = {'nombrePropietario': nombrePropietario, 'costo': costo, 'numero_cuartos': numero_cuartos,'edificio': edificio}

        requests.put(f"http://127.0.0.1:8000/api/departamentos/{id}/", data=data, auth=(usuario, clave))
        return redirect(url_for('los_departamentos_dos'))
    r = requests.get("http://127.0.0.1:8000/api/edificios/", auth=(usuario, clave))
    edificios = json.loads(r.content)['results']
    return render_template("editar_departamento.html", departamento=departamento, edificios=edificios)

@app.route("/editar_edificio/<int:id>", methods=['GET', 'POST'])
def editar_edificio(id):
    r = requests.get(f"http://127.0.0.1:8000/api/edificios/{id}/", auth=(usuario, clave))
    edificio = json.loads(r.content)

    if request.method == 'POST':
        nombre= request.form['nombre']
        direccion = request.form['direccion']
        ciudad = request.form['ciudad']
        tipo = request.form['tipo']

        data = {'nombre': nombre, 'direccion': direccion, 'ciudad': ciudad,'tipo': tipo}

        requests.put(f"http://127.0.0.1:8000/api/edificios/{id}/", data=data, auth=(usuario, clave))
    return render_template("editar_edificio.html", edificio=edificio)
#---------------------------------------------------
@app.route("/eliminar_departamento/<int:id>", methods=['POST'])
def eliminar_departamento(id):
    requests.delete(f"http://127.0.0.1:8000/api/departamentos/{id}/", auth=(usuario, clave))
    return redirect(url_for('los_departamentos_dos'))

@app.route("/eliminar_edificio/<int:id>", methods=['POST'])
def eliminar_edificio(id):
    requests.delete(f"http://127.0.0.1:8000/api/edificios/{id}/", auth=(usuario, clave))
    return redirect(url_for('los_edificios'))
