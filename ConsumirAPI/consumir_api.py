import requests

def obtener_datos_de_api():
    url = 'https://jsonplaceholder.typicode.com/todos/1'
    respuesta = requests.get(url)

    # Verifica si la solicitud fue exitosa
    if respuesta.status_code == 200:
        datos = respuesta.json()
        print("Datos de la API:")
        print(f"ID: {datos['id']}")
        print(f"Título: {datos['title']}")
        print(f"Completado: {datos['completed']}")
    else:
        print(f"No se pudo obtener datos. Código de estado: {respuesta.status_code}")

if __name__ == "__main__":
    obtener_datos_de_api()