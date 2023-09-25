-- Crea una nueva base de datos "TIF_Grupo_14"
CREATE DATABASE IF NOT EXISTS TIF_Grupo_14;

-- Crea una tabla llamada "Usuarios" en la base de datos "TIF_Grupo_14"
CREATE TABLE TIF_Grupo_14.usuarios (
  id_usuario INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombre_usuario VARCHAR(255) NOT NULL,
  clave varchar(255),
  email VARCHAR(255) NOT NULL,
  nombre VARCHAR(255) NOT NULL,
  apellido VARCHAR(255) NOT NULL,
  imagen_perfil VARCHAR(255) NOT NULL
);

-- Crea una tabla llamada "Servidores" en la base de datos "TIF_Grupo_14"
CREATE TABLE TIF_Grupo_14.servidores (
  id_Servidor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombreServidor VARCHAR(255) NOT NULL,
  descripcion TEXT NOT NULL
);

-- Crea una tabla llamada "Usuario_Servidor" en la base de datos "TIF_Grupo_14"
CREATE TABLE TIF_Grupo_14.usuario_Servidor (
  id_usuarioServidor INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  id_usuario INT NOT NULL,
  id_servidor INT NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
  FOREIGN KEY (id_servidor) REFERENCES servidores (id_servidor)
);

-- Crea una tabla llamada "Canales" en la base de datos "TIF_Grupo_14"
CREATE TABLE TIF_Grupo_14.canales (
  id_canal INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  nombreCanal VARCHAR(255),
  descripcion TEXT NOT NULL,
  id_usuario INT NOT NULL,
  id_servidor INT NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
  FOREIGN KEY (id_servidor) REFERENCES servidores (id_servidor)
);


-- Crea una tabla llamada "Chasts" en la base de datos "TIF_Grupo_14"
CREATE TABLE TIF_Grupo_14.chats (
  id_mensaje INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  contenido TEXT NOT NULL,
  fecha_creacion TIMESTAMP NOT NULL,
  id_usuario INT NOT NULL,
  id_canal INT NOT NULL,
  FOREIGN KEY (id_usuario) REFERENCES usuarios (id_usuario),
  FOREIGN KEY (id_canal) REFERENCES canales (id_canal)
);























