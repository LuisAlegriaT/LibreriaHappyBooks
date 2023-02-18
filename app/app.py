#Importamos la libreria de flask
from flask import Flask 

#creamos una variable para almacenar la aplicacion con el modulo de Flask
app=Flask(__name__)

#Definimos una ruta
@app.route('/')
def index():
    return 'CodigoFacilito'

#Otra forma de añadir rutas concat line 18
def helloworld():
    return 'Hello World'
    
#Inicializamos la aplicación con app.run
if __name__ =='__main__':
    app.add_url_rule('/holaMundo', view_func=helloworld)
    app.run(debug=True, port=5000)
        #debug true sirve para actualizar el servidor en tiempo real

