from src.gestion_usuarios import (
    registrar_usuario,
    iniciar_sesion,
    mostrar_datos_personales,
    mostrar_lista_usuarios,
    cambiar_rol_usuario,
    eliminar_usuario,
)


def mostrar_menu_principal():
    while True:
        print("\n--- Sistema de Usuarios ---")
        print("1. Registrar usuario")
        print("2. Iniciar sesión")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            registrar_usuario()
        elif opcion == "2":
            nombre, rol = iniciar_sesion()
            if nombre:
                mostrar_menu_por_rol(nombre, rol)
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")


def mostrar_menu_por_rol(nombre_usuario, rol):
    if rol == "estandar":
        print(f"\nMenú Usuario Estándar ({nombre_usuario})")
        print("1. Ver mis datos")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            mostrar_datos_personales(nombre_usuario)
        else:
            print("Opción no válida.")
    elif rol == "admin":
        while True:
            print(f"\nMenú Admin ({nombre_usuario})")
            print("1. Ver lista de usuarios")
            print("2. Cambiar rol de un usuario")
            print("3. Eliminar un usuario")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                mostrar_lista_usuarios()
            elif opcion == "2":
                cambiar_rol_usuario()
            elif opcion == "3":
                eliminar_usuario()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")

#Muestra el menú principal y los menús según el rol del usuario.