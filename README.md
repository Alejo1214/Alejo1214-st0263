# info de la materia: Tópicos Especiales en Telemática - Reto1-2 <nombre>
#
# Estudiante(s): Alejandro Cardona Jaramillo, acardonaj@eafit.edu.co -eafit
#
# Profesor: Alvaro Ospina, aeospinas@eafit.brightspace.com -eafit
#

# Reto 1-2 

# 1. breve descripción de la actividad
<texto descriptivo> 

La actividad consiste en el diseño e implementación de un sistema P2P (Peer-to-Peer) utilizando Python y Flask para la creación de un servidor centralizado y solicitudes HTTP para la comunicación entre clientes y servidor. El sistema permite a los usuarios registrarse, iniciar sesión, enviar índices de archivos y buscar archivos compartidos por otros usuarios. 
#
## 1.1. Que aspectos cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

 Se ha creado un sistema peer-to-peer donde cada nodo contiene módulos servidor (PServidor) definidos como varios microservicios y un módulo cliente (PCliente). Este diseño permite la comunicación entre los peers de la red de manera distribuida y descentralizada, en cada nodo soportan concurrencia, permitiendo que más de un proceso remoto se comunique simultáneamente. Cada peer tiene todas las funcionalidades propuestas login(), enviar_indice(), buscar() y logout().
#

## 1.2. Que aspectos NO cumplió o desarrolló de la actividad propuesta por el profesor (requerimientos funcionales y no funcionales)

Para este reto, se solicitó implementar la comunicación entre los nodos utilizando el middleware gRPC. Sin embargo, en la implementación proporcionada, se utilizó el middleware API REST para la comunicación entre los nodos
#

# 2. información general de diseño de alto nivel, arquitectura, patrones, mejores prácticas utilizadas.

El sistema sigue una arquitectura cliente-servidor donde cada nodo peer actúa tanto como cliente como servidor. Los nodos se comunican entre sí mediante solicitudes HTTP utilizando la API REST para realizar operaciones como login, enviar índices de archivos y buscar archivos. 

Cada nodo peer se divide en varios microservicios, como PServidor y PCliente, para separar las diferentes funcionalidades y promover la modularidad, el mantenimiento y la escalabilidad del sistema. Cada microservicio se encarga de una tarea específica, como la gestión de archivos, la autenticación o la interacción con otros nodos.

Se uso un archivo en formato JSON, se utilizan para almacenar información del usuario y sus archivos. La base de datos se carga y guarda en el archivo en cada operación de inicio de sesión,  índice de archivos y búsqueda de archivos.

Implementar un sistema de autenticación básico mediante nombre de usuario y contraseña para permitir el acceso seguro a los nodos. Sin embargo, esta implementación se puede mejorar mediante el uso de técnicas de autenticación y autorización más avanzadas.
#
# 3. Descripción del ambiente de desarrollo y técnico: lenguaje de programación, librerias, paquetes, etc, con sus numeros de versiones.
Lenguaje de Programación: Python



Framework Web: Flask 2.0.2

Descripción: Flask es un framework ligero de Python para construir aplicaciones web. Se utiliza en el lado del servidor para crear las API REST que permiten la comunicación entre los nodos peers.

Biblioteca para solicitudes HTTP:

Versión: Requests 2.26.0

Descripción: Requests es una biblioteca de Python que facilita el envío de solicitudes HTTP/1.1 y HTTPS. Se utiliza en los nodos peers para comunicarse entre sí a través de la API REST.
#
## como se compila y ejecuta.
1. **Ejecución del Script Python:**
   Para ejecutar un script Python:
   ```bash
   python3 -m venv myenv
   pip install Flask requests
   python server.py
   python pclient.py

## como se lanza el servidor.
    
        python server.py
  

# referencias:

## sitio1-url: https://www.youtube.com/watch?v=b0ZrmhyyCY4&t=427s 
## sitio2-url: https://www.youtube.com/watch?v=Esdj9wlBOaI
## 
