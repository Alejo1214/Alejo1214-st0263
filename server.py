from flask import Flask, request, jsonify
import json

app = Flask(__name__)

# Ruta al archivo de base de datos
DATABASE_FILE = 'database.txt'

# Función para cargar la base de datos desde el archivo
def load_database():
    try:
        with open(DATABASE_FILE, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {'usuarios': {}}

# Función para guardar la base de datos en el archivo
def save_database(database):
    with open(DATABASE_FILE, 'w') as file:
        json.dump(database, file)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    url = data.get('url')  

    database = load_database()

    if username in database['usuarios'] and database['usuarios'][username]['password'] == password:
        # Guardar la URL del usuario en la base de datos si es un nuevo usuario
        if 'url' not in database['usuarios'][username]:
            database['usuarios'][username]['url'] = url
            save_database(database)
        return jsonify({'message': 'Login exitoso'}), 200
    else:
        # Si es un nuevo usuario, agregarlo a la base de datos
        if username not in database['usuarios']:
            database['usuarios'][username] = {'password': password, 'url': url, 'archivos': []}
            save_database(database)
            return jsonify({'message': 'Usuario creado y login exitoso'}), 200
        else:
            return jsonify({'message': 'Credenciales inválidas'}), 401
    
@app.route('/enviar_indice', methods=['POST'])
def enviar_indice():
    data = request.get_json()
    username = data.get('username')
    archivos = data.get('archivos')

    database = load_database()

    # Actualizar la lista de archivos del usuario en la base de datos
    if username in database['usuarios']:
        database['usuarios'][username]['archivos'] = archivos
        save_database(database)
        return jsonify({'message': 'Índice de archivos actualizado'}), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404

@app.route('/buscar', methods=['POST'])
def buscar():
    data = request.get_json()
    nombre_archivo = data.get('archivos')

    database = load_database()
    resultados = []

    for usuario, info in database['usuarios'].items():
        if nombre_archivo in info['archivos']:
            resultados.append({'usuario': usuario, 'url': f"{info['url']}/download/{nombre_archivo}"})

    return jsonify({'resultados': resultados}), 200

@app.route('/logout', methods=['POST'])
def logout():
    data = request.get_json()
    username = data.get('username')

    database = load_database()

    if username in database['usuarios']:
        del database['usuarios'][username]
        save_database(database)
        return jsonify({'message': 'Logout exitoso'}), 200
    else:
        return jsonify({'message': 'Usuario no encontrado'}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
