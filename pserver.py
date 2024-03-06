import requests
import json

SERVER_URL = 'http://localhost:5000'

class PServer:
    def __init__(self, peer_id, peer_address):
        self.peer_id = peer_id
        self.peer_address = peer_address

    def send_index(self, index_data):
        data = {'username': self.peer_id, 'archivos': index_data}
        response = requests.post(f"{SERVER_URL}/enviar_indice", json=data)
        return response.json()

    def search(self, keyword):
        data = {'archivos': keyword}
        response = requests.post(f"{SERVER_URL}/buscar", json=data)
        return response.json()
