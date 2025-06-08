-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS usuario_app_db;

USE usuario_app_db;

-- Tabla de roles
CREATE TABLE rol (
    id INT AUTO_INCREMENT PRIMARY KEY,
    rol VARCHAR(50) UNIQUE NOT NULL
);

-- Tabla de usuarios
CREATE TABLE usuario (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre_usuario VARCHAR(50) UNIQUE NOT NULL,
    contraseña VARCHAR(255) NOT NULL,
    rol_id INT NOT NULL,
    FOREIGN KEY (rol_id) REFERENCES rol(id)
        ON DELETE RESTRICT ON UPDATE CASCADE
);

-- Tabla de sesiones
CREATE TABLE sesion (
    id INT AUTO_INCREMENT PRIMARY KEY,
    usuario_id INT NOT NULL,
    fecha_hora DATETIME DEFAULT CURRENT_TIMESTAMP,
    exito BOOLEAN NOT NULL,
    FOREIGN KEY (usuario_id) REFERENCES usuario(id)
        ON DELETE CASCADE ON UPDATE CASCADE
);

-- Insertar roles iniciales
INSERT INTO rol (nombre) VALUES ('admin'), ('usuario');

-- Insertar usuarios iniciales

INSERT INTO Usuario (nombre_usuario, contraseña, rol) VALUES ('Pablo', 'abc123', 'usuario');
INSERT INTO Usuario (nombre_usuario, contraseña, rol) VALUES ('Admin', 'admin', 'admin');