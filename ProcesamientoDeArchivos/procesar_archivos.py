def procesar_archivos(entrada, salida):
    with open(entrada, 'r') as archivo_entrada:
        # Convertir a mayúsculas
        contenido = archivo_entrada.read().upper()

    with open(salida, 'w') as archivo_salida:
        archivo_salida.write(contenido)

if __name__ == "__main__":
    archivo_entrada = "ProcesamientoDeArchivos/entrada.txt"
    archivo_salida = "ProcesamientoDeArchivos/salida.txt"
    procesar_archivos(archivo_entrada, archivo_salida)
    print(f"Procesamiento completado. Resultado en {archivo_salida}")