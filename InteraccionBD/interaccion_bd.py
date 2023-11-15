import sqlite3

def crear_tabla():
    conexion = sqlite3.connect("ejemplo.db")

    # Creación de una tabla llamada 'usuarios'
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS usuarios (
            id INTEGER PRIMARY KEY,
            nombre TEXT NOT NULL,
            edad INTEGER
        )
    ''')
    conexion.commit()
    conexion.close()

def insertar_usuario(nombre, edad):
    # Conexión a la base de datos
    conexion = sqlite3.connect("ejemplo.db")
    cursor = conexion.cursor()

    # Insertar un nuevo usuario
    cursor.execute("INSERT INTO usuarios (nombre, edad) VALUES (?, ?)", (nombre, edad))

    conexion.commit()
    conexion.close()

def obtener_usuarios():
    # Conexión a la base de datos
    conexion = sqlite3.connect("ejemplo.db")
    cursor = conexion.cursor()

    # Obtener todos los usuarios
    cursor.execute("SELECT * FROM usuarios")
    usuarios = cursor.fetchall()

    for usuario in usuarios:
        print(f"ID: {usuario[0]}, Nombre: {usuario[1]}, Edad: {usuario[2]}")

    conexion.close()

if __name__ == "__main__":
    crear_tabla()

    # Inserta algunos usuarios
    insertar_usuario("Juan", 25)
    insertar_usuario("María", 30)

    # Obtiene y muestra todos los usuarios
    obtener_usuarios()