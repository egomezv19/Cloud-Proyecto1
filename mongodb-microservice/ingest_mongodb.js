const mongoose = require('mongoose');
const fs = require('fs');

// Conectar a MongoDB
mongoose.connect('mongodb://localhost:27017/universidad', {
  useNewUrlParser: true,
  useUnifiedTopology: true
}).then(() => {
  console.log('Conectado a MongoDB');
}).catch((error) => {
  console.error('Error al conectar a MongoDB:', error);
});

// Definir el esquema de Alojamiento
const alojamientoSchema = new mongoose.Schema({
  ID_Alojamiento: String,
  ID_Programa: String,
  Descripción: String,
  Dirección: String,
  Precio: Number
});

// Crear el modelo
const Alojamiento = mongoose.model('Alojamiento', alojamientoSchema);

// Leer el archivo JSON
const alojamientosData = JSON.parse(fs.readFileSync('./data/alojamientos.json', 'utf8'));

// Insertar los datos en la base de datos
Alojamiento.insertMany(alojamientosData)
  .then(() => {
    console.log('Datos de alojamientos insertados correctamente.');
    mongoose.connection.close();
  })
  .catch((err) => {
    console.error('Error al insertar datos: ', err);
    mongoose.connection.close();
  });
