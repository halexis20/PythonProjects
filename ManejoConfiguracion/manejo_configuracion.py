import json

def cargar_configuracion(ruta_archivo):
    try:
        with open(ruta_archivo, 'r') as archivo:
            configuracion = json.load(archivo)
        return configuracion
    except FileNotFoundError:
        print(f"El archivo de configuración '{ruta_archivo}' no existe.")
        return None
    except json.JSONDecodeError:
        print(f"Error al decodificar el archivo de configuración '{ruta_archivo}'. Verifica el formato JSON.")
        return None

def main():
    # Ruta del archivo de configuración
    ruta_archivo_config = 'ManejoConfiguracion/config.json'

    # Cargar configuración desde el archivo
    configuracion = cargar_configuracion(ruta_archivo_config)

    if configuracion:
        print("Configuración cargada exitosamente:")
        for clave, valor in configuracion.items():
            print(f"{clave}: {valor}")

if __name__ == "__main__":
    main()