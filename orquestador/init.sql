-- Crear tabla Empresa
CREATE TABLE IF NOT EXISTS Empresa (
    id_empresa INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    direccion TEXT NOT NULL,
    telefono VARCHAR(20),
    email VARCHAR(100)
);

-- Crear tabla Empleo
CREATE TABLE IF NOT EXISTS Empleo (
    id_empleo INT AUTO_INCREMENT PRIMARY KEY,
    id_empresa INT,
    titulo VARCHAR(100) NOT NULL,
    descripcion TEXT NOT NULL,
    requisitos TEXT,
    salario DECIMAL(10, 2) NOT NULL,
    FOREIGN KEY (id_empresa) REFERENCES Empresa(id_empresa)
);

-- Insertar datos de ejemplo en la tabla Empresa
INSERT INTO Empresa (nombre, direccion, telefono, email) VALUES
('Tech Solutions', '123 Tech Lane', '123456789', 'contact@techsolutions.com'),
('Innovatech', '456 Innovation Ave', '987654321', 'info@innovatech.com'),
('Web Creators', '789 Web Blvd', '555123456', 'hello@webcreators.com'),
('Data Corp', '101 Data Drive', '555654321', 'info@datacorp.com'),
('AI Innovators', '102 AI St', '555987654', 'contact@aiinnovators.com'),
('Cloud Systems', '103 Cloud Way', '555123789', 'support@cloudsystems.com'),
('FinTech Solutions', '104 Finance Rd', '555456987', 'contact@fintech.com'),
('HealthTech Innovations', '105 Health St', '555789654', 'info@healthtech.com'),
('EduTech Corp', '106 Education Blvd', '555321654', 'contact@edutech.com'),
('EcoTech Solutions', '107 Eco Rd', '555654789', 'info@ecotech.com');

-- Insertar datos de ejemplo en la tabla Empleo
INSERT INTO Empleo (id_empresa, titulo, descripcion, requisitos, salario) VALUES
(1, 'Desarrollador Backend', 'Buscamos un desarrollador backend con experiencia en Python.', 'Experiencia en Python y SQL', 50000.00),
(2, 'Diseñador UI/UX', 'Buscamos un diseñador con habilidades en diseño de interfaces.', 'Portafolio y experiencia previa', 45000.00),
(3, 'Desarrollador Frontend', 'Se requiere desarrollador frontend con conocimientos en React.', 'Conocimientos en React y CSS', 55000.00),
(4, 'Analista de Datos', 'Buscamos un analista de datos con experiencia en SQL y Python.', 'Conocimiento en SQL y herramientas de análisis', 60000.00),
(5, 'Gerente de Proyectos', 'Buscamos un gerente de proyectos con experiencia en tecnología.', 'Experiencia en gestión de proyectos', 70000.00),
(6, 'Especialista en Nube', 'Se busca especialista en soluciones en la nube.', 'Experiencia en AWS y Azure', 80000.00),
(7, 'Desarrollador Móvil', 'Buscamos un desarrollador de aplicaciones móviles.', 'Experiencia en desarrollo de apps móviles', 60000.00),
(8, 'Consultor Financiero', 'Se busca consultor con experiencia en finanzas tecnológicas.', 'Experiencia en finanzas y consultoría', 75000.00),
(9, 'Investigador de Mercado', 'Buscamos un investigador de mercado para proyectos de tecnología.', 'Experiencia en investigación de mercado', 50000.00),
(10, 'Asistente Administrativo', 'Se busca asistente administrativo para apoyo a la gestión.', 'Habilidades administrativas y de comunicación', 40000.00);
