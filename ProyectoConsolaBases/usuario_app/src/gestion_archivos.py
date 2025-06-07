import json
import os

ARCHIVO_USUARIOS = "data/usuarios.json"

def cargar_usuarios():
    os.makedirs(os.path.dirname(ARCHIVO_USUARIOS), exist_ok=True)

    if not os.path.exists(ARCHIVO_USUARIOS):
        with open(ARCHIVO_USUARIOS, "w") as archivo:
            json.dump({}, archivo)
        return {}

    with open(ARCHIVO_USUARIOS, "r") as archivo:
        try:
            return json.load(archivo)
        except json.JSONDecodeError:
            print("⚠️ Advertencia: El archivo 'usuarios.json' estaba dañado o vacío. Se ha restaurado automáticamente.")
            with open(ARCHIVO_USUARIOS, "w") as archivo_escritura:
                json.dump({}, archivo_escritura)
            return {}

def guardar_usuarios(usuarios):  
    with open(ARCHIVO_USUARIOS, "w") as archivo:
        json.dump(usuarios, archivo, indent=4)



# Manejo de archivos JSON (leer y guardar usuarios). Seria reemplazado por la conexion a la base de datos desde python
# tema que no se vio en este modulo introductorio.
# ¿Qué hace este código?
# Si no existe la carpeta data/, la crea.
# Si no existe usuarios.json, lo crea con {}.
# Si el archivo existe pero está vacío o tiene contenido inválido, lo resetea a {} automáticamente sin romper el programa.