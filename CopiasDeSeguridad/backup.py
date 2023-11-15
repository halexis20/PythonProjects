import shutil
import os
from datetime import datetime

def realizar_copia_de_seguridad(origen, destino):
    fecha_actual = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    directorio_copia = os.path.join(destino, f"backup_{fecha_actual}")

    try:
        shutil.copytree(origen, directorio_copia)
        print(f"Copia de seguridad exitosa en: {directorio_copia}")
    except Exception as e:
        print(f"Error al realizar la copia de seguridad: {e}")

if __name__ == "__main__":
    directorio_origen = r"rutaorigen"
    directorio_destino = r"rutabackup"
    
    realizar_copia_de_seguridad(directorio_origen, directorio_destino)