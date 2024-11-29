-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS calificaciones_db;
USE calificaciones_db;

-- Estructura de la tabla calificaciones
CREATE TABLE `calificaciones` (
    `Estudiante` varchar(45) NOT NULL,
    `Asignatura` varchar(45) NOT NULL,
    `Nota` float DEFAULT NULL,
    PRIMARY KEY (`Estudiante`, `Asignatura`)
);