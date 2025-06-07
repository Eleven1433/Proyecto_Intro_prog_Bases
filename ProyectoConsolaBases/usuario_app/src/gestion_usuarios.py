from src.gestion_archivos import cargar_usuarios, guardar_usuarios


def registrar_usuario():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Ingrese un nombre de usuario: ")
    if nombre_usuario in usuarios:
        print("El usuario ya existe.")
        return

    contraseña = input("Ingrese una contraseña: ")
    rol = input("Ingrese el rol (admin/estandar): ").lower()
    if rol not in ["admin", "estandar"]:
        print("Rol no válido. Se asignará 'estandar' por defecto.")
        rol = "estandar"

    usuarios[nombre_usuario] = {
        "contraseña": contraseña,
        "rol": rol
    }
    guardar_usuarios(usuarios)
    print("Usuario registrado exitosamente.")


def iniciar_sesion():
    usuarios = cargar_usuarios()
    nombre_usuario = input("Nombre de usuario: ")
    contraseña = input("Contraseña: ")

    if nombre_usuario in usuarios and usuarios[nombre_usuario]["contraseña"] == contraseña:
        print(f"Bienvenido, {nombre_usuario}!")
        return nombre_usuario, usuarios[nombre_usuario]["rol"]
    else:
        print("Nombre de usuario o contraseña incorrectos.")
        return None, None


def mostrar_datos_personales(nombre_usuario):
    usuarios = cargar_usuarios()
    datos = usuarios.get(nombre_usuario, {})
    print(f"\nDatos personales de {nombre_usuario}:")
    print(f"Rol: {datos.get('rol', 'Desconocido')}")


def mostrar_lista_usuarios():
    usuarios = cargar_usuarios()
    print("\nLista de usuarios:")
    for nombre, datos in usuarios.items():
        print(f"- {nombre} ({datos['rol']})")


def cambiar_rol_usuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingrese el nombre del usuario a modificar: ")
    if nombre in usuarios:
        nuevo_rol = input("Ingrese el nuevo rol (admin/estandar): ").lower()
        if nuevo_rol in ["admin", "estandar"]:
            usuarios[nombre]["rol"] = nuevo_rol
            guardar_usuarios(usuarios)
            print("Rol actualizado correctamente.")
        else:
            print("Rol no válido.")
    else:
        print("Usuario no encontrado.")


def eliminar_usuario():
    usuarios = cargar_usuarios()
    nombre = input("Ingrese el nombre del usuario a eliminar: ")
    if nombre in usuarios:
        del usuarios[nombre]
        guardar_usuarios(usuarios)
        print("Usuario eliminado correctamente.")
    else:
        print("Usuario no encontrado.")

#Funciones para registrar, iniciar sesión y tareas admin.
