# 🧑‍💻 Sistema de Registro e Inicio de Sesión de Usuarios (Python CLI)

Este proyecto es una aplicación de línea de comandos (CLI) para la gestión de usuarios, que permite registrar usuarios, iniciar sesión y acceder a menús específicos según su rol (`admin` o `estandar`).

## 📁 Estructura del proyecto

usuario_app/
│
├── main.py
├── data/
│ └── usuarios.json # Base de datos en formato JSON
├── src/
│ ├── gestion_archivos.py # Lectura y escritura de archivos
│ ├── gestion_usuarios.py # Registro, login, y funciones admin
│ └── menu.py # Menú principal y por rol
├── requirements.txt
└── README.md


## 🚀 Cómo ejecutar el proyecto

1. Asegúrate de tener Python instalado (3.9 o superior).
2. Abre una terminal y navega a la carpeta del proyecto.
3. Ejecuta el archivo principal:

```bash
python main.py

👥 Roles de usuario
estandar: Puede ver solamente sus propios datos personales.

admin: Puede listar usuarios, cambiar roles y eliminar usuarios.

✅ Funcionalidades

Registro de nuevos usuarios.

Inicio de sesión con validación de credenciales.

Menú personalizado por rol.

Persistencia de datos en usuarios.json.

💡 Notas
Todos los datos se almacenan en el archivo data/usuarios.json.

Se siguen las convenciones estándar de nombres recomendadas por la comunidad Python:

snake_case para variables, funciones y archivos.

Directorios en minúsculas sin espacios.

Grupo 14:  Nicolas Elias Calmucci - Usuario Github: Eleven1433 / Juan Ignacio Alonso - Usuario Github: juanignacioalonso  / Cesar Ramiro Ruggieri - Usuario Github: subrami22 
