import os

def main():
    # Obtener el secreto desde la variable de entorno
    secret_message = os.getenv('GS_SECRET_MESSAGE')

    if secret_message:
        print(f"Mensaje secreto desde GitHub: {secret_message}")
    else:
        print("No se pudo obtener el mensaje secreto. Verifica la configuración del secreto en GitHub.")

if __name__ == "__main__":
    main()