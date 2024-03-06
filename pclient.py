import requests

class PClient:
    def __init__(self):
        pass

    def login(self):
        url = input("Ingrese la URL del servidor: ")
        username = input("Ingrese su nombre de usuario: ")
        password = input("Ingrese su contraseña: ")
        data = {'username': username, 'password': password, 'url': url}
        response = requests.post(url + '/login', json=data)

        if response.status_code == 200:
            print("Login exitoso")
            return url, username
        elif response.status_code == 401:
            print("Credenciales inválidas")
            return None, None
        else:
            print("Error en la solicitud")
            return None, None

    def enviar_indice(self, username, archivos, url):
        data = {'username': username, 'archivos': archivos}
        response = requests.post(url + '/enviar_indice', json=data)

        if response.status_code == 200:
            print("Índice de archivos enviado exitosamente")
        else:
            print("Error al enviar el índice de archivos")

    def buscar(self, nombre_archivo, url_servidor):
        data = {'archivos': nombre_archivo}
        response = requests.post(url_servidor + '/buscar', json=data)

        if response.status_code == 200:
            resultados = response.json().get('resultados', [])
            for resultado in resultados:
                usuario = resultado.get('usuario')
                url = resultado.get('url')
                print(f"Usuario: {usuario}, URL: {url}")
        else:
            print("Error al buscar el archivo")

    def logout(self, username, url):
        data = {'username': username}
        response = requests.post(url + '/logout', json=data)

        if response.status_code == 200:
            print("Logout exitoso. Datos del usuario eliminados del servidor.")
        else:
            print("Error al hacer logout.")

    def menu(self):
        url = None
        username = None
        while True:
            print("1. Login")
            print("2. Enviar índice de archivos")
            print("3. Buscar archivo")
            print("4. Logout")
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                url, username = self.login()
            elif opcion == '2':
                if username and url:
                    archivos = input("Ingrese los archivos a compartir separados por coma: ").split(',')
                    self.enviar_indice(username, archivos, url)
                else:
                    print("Debe iniciar sesión primero.")
            elif opcion == '3':
                nombre_archivo = input("Ingrese el nombre del archivo a buscar: ")
                if url:
                    self.buscar(nombre_archivo, url)
                else:
                    print("Debe iniciar sesión primero.")
            elif opcion == '4':
                if username and url:
                    self.logout(username, url)
                    break
                else:
                    print("Debe iniciar sesión primero.")
            else:
                print("Opción no válida")

if __name__ == "__main__":
    client = PClient()
    client.menu()
