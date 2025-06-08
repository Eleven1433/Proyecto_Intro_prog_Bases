
-- Crear usuario
INSERT INTO usuario (nombre_usuario, contraseña, nombre_completo, correo, rol_id)
VALUES ('jose01', 'clave123', 'José Gómez', 'jose@mail.com', 2);
-- Ver todos los usuarios
SELECT u.id, u.nombre_usuario, u.nombre_completo, u.correo, r.nombre AS rol
FROM usuario u
JOIN rol r ON u.rol_id = r.id;
-- Cambiar rol a un usuario
UPDATE usuario SET rol_id = 1 WHERE nombre_usuario = 'jose01';
-- Eliminar usuario
DELETE FROM usuario WHERE nombre_usuario = 'jose01';
