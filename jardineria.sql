CREATE DATABASE Jardineria;
USE Jardineria;

-- Tabla de Empleados
CREATE TABLE Empleados (
    id_empleado INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(50),
    apellido VARCHAR(50),
    email VARCHAR(100),
    telefono VARCHAR(20),
    pais VARCHAR(50)
);

-- Tabla de Clientes
CREATE TABLE Clientes (
    id_cliente INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    direccion VARCHAR(255),
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- Tabla de Productos
CREATE TABLE Productos (
    id_producto INT PRIMARY KEY AUTO_INCREMENT,
    nombre VARCHAR(100),
    descripcion TEXT,
    precio DECIMAL(10,2),
    stock INT
);

-- Tabla de Pedidos
CREATE TABLE Pedidos (
    id_pedido INT PRIMARY KEY AUTO_INCREMENT,
    id_cliente INT,
    id_empleado INT,
    fecha_pedido DATE,
    total DECIMAL(10,2),
    FOREIGN KEY (id_cliente) REFERENCES Clientes(id_cliente),
    FOREIGN KEY (id_empleado) REFERENCES Empleados(id_empleado)
);

-- Tabla de Detalles de Pedidos
CREATE TABLE Detalles_Pedidos (
    id_detalle INT PRIMARY KEY AUTO_INCREMENT,
    id_pedido INT,
    id_producto INT,
    cantidad INT,
    precio_unitario DECIMAL(10,2),
    FOREIGN KEY (id_pedido) REFERENCES Pedidos(id_pedido),
    FOREIGN KEY (id_producto) REFERENCES Productos(id_producto)
);

-- Insertar 10 empleados en diferentes países
INSERT INTO Empleados (nombre, apellido, email, telefono, pais) VALUES
('Juan', 'Pérez', 'juanp@example.com', '555-1234', 'México'),
('Ana', 'Gómez', 'anag@example.com', '555-5678', 'España'),
('Luis', 'Martínez', 'luism@example.com', '555-9101', 'Argentina'),
('Carlos', 'Fernández', 'carlosf@example.com', '555-1122', 'Colombia'),
('María', 'Rodríguez', 'mariar@example.com', '555-3344', 'Chile'),
('José', 'López', 'josel@example.com', '555-5566', 'Perú'),
('Elena', 'Díaz', 'elenad@example.com', '555-7788', 'Ecuador'),
('Pedro', 'Sánchez', 'pedros@example.com', '555-9900', 'Brasil'),
('Marta', 'Ramírez', 'martar@example.com', '555-2233', 'Uruguay'),
('Ricardo', 'Torres', 'ricardot@example.com', '555-4455', 'Paraguay');

-- Insertar 10 clientes
INSERT INTO Clientes (nombre, direccion, telefono, email) VALUES
('Jardines Verdes', 'Calle 123, Ciudad A', '111-2222', 'contacto@verdes.com'),
('Florería Bella', 'Av. Las Flores 456, Ciudad B', '333-4444', 'info@bella.com'),
('Parques y Jardines', 'Zona Central, Ciudad C', '555-6666', 'admin@parques.com'),
('Decoración Natural', 'Colonia X, Ciudad D', '777-8888', 'ventas@natural.com'),
('Paisajismo Total', 'Carrera 7, Ciudad E', '999-0000', 'atencion@paisajismo.com'),
('Jardines y más', 'Blvd. 20, Ciudad F', '123-4567', 'servicio@jardinesymas.com'),
('Naturaleza Viva', 'Callejón Verde, Ciudad G', '234-5678', 'soporte@viva.com'),
('EcoPlant', 'Plaza Mayor, Ciudad H', '345-6789', 'ventas@ecoplant.com'),
('Botánica Express', 'Calle 8, Ciudad I', '456-7890', 'info@botanica.com'),
('GreenWorld', 'Paseo Ecológico, Ciudad J', '567-8901', 'contacto@greenworld.com');

-- Insertar 10 productos
INSERT INTO Productos (nombre, descripcion, precio, stock) VALUES
('Rosa', 'Planta ornamental', 5.00, 100),
('Tulipán', 'Flor colorida', 4.50, 150),
('Cactus', 'Planta resistente', 7.00, 80),
('Orquídea', 'Planta exótica', 15.00, 50),
('Bonsái', 'Árbol en miniatura', 20.00, 30),
('Maceta grande', 'Maceta de cerámica', 10.00, 200),
('Tierra fértil', 'Sustrato especial', 3.00, 300),
('Abono orgánico', 'Fertilizante natural', 6.00, 120),
('Pala de jardinería', 'Herramienta para plantar', 8.00, 100),
('Regadera', 'Para riego de plantas', 12.00, 90);

-- Insertar 10 pedidos
INSERT INTO Pedidos (id_cliente, id_empleado, fecha_pedido, total) VALUES
(1, 2, '2025-03-01', 50.00),
(2, 5, '2025-03-02', 75.00),
(3, 3, '2025-03-03', 100.00),
(4, 1, '2025-03-04', 45.00),
(5, 8, '2025-03-05', 90.00),
(6, 6, '2025-03-06', 110.00),
(7, 7, '2025-03-07', 60.00),
(8, 4, '2025-03-08', 130.00),
(9, 9, '2025-03-09', 85.00),
(10, 10, '2025-03-10', 55.00);

-- Insertar detalles de pedidos
INSERT INTO Detalles_Pedidos (id_pedido, id_producto, cantidad, precio_unitario) VALUES
(1, 1, 5, 5.00),
(2, 2, 10, 4.50),
(3, 3, 8, 7.00),
(4, 4, 3, 15.00),
(5, 5, 2, 20.00),
(6, 6, 6, 10.00),
(7, 7, 10, 3.00),
(8, 8, 5, 6.00),
(9, 9, 7, 8.00),
(10, 10, 4, 12.00);
