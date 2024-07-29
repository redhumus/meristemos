#Script para escuchar webhooks de github
#La Mica Prieta Software
#Luis Miguel Sánchez Zoque - ReDHumus.org
#COPYLEFT 2023 - Licencia GPL V.3

# Funcionalidad: Abre una web app que escucha los POST de la API de Github. Requiere de la puesta en marcha de un webhook con la app gh (comandos Github) 
#Cada vez que se envíe un evento desde la API de Github, corre una acción pull en el repositorio. Requiere que previamente se gestione la autenticacioń automática. Se sugiere vía SSH 
#Más información: https://aprende.redhumus.org

#Inicio del script

# importa la biblioteca Flask 
import os
from flask import Flask, request

app = Flask(__name__)


import logging

logging.basicConfig(filename='../app.log', level=logging.DEBUG)

# Ejemplo de registro de un mensaje de depuración
logging.debug('Este es un mensaje de depuración')

#Crea una ruta en  aplicación Flask que escuche los eventos webhook de GitHub recibiendo datos de tipo .json
@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

# Cada vez que haya un evento desde la API de Github busca en los datos el contenido refs/heads/main. Se puede modificar a gusto. 
#Se debe modificar la carpeta raíz del repositorio de acuerdo al caso
    if data['ref'] == 'refs/heads/main':
         os.system('cd /var/www/html/osmco/landingpage && git pull git@github.com:OpenStreetMapColombia/landingpage.git')

#devuelve un resultado Ok, leido

    return '', 200

#Falta implementar una respuesta más detallada para hacer depuración de errores

# ejecutar la aplicación Flask y hacerla escuchar los eventos webhook

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=3000)
