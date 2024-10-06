const fs = require('fs');
const mongoose = require('mongoose');

// Conexión a MongoDB
mongoose.connect('mongodb://localhost:27017/universidad', { useNewUrlParser: true, useUnifiedTopology: true });

// Definición del esquema y modelo para Alojamiento
const alojamientoSchema = new mongoose.Schema({
  ID_Alojamiento: String,
  ID_Programa: String,
  Descripción: String,
  Dirección: String,
  Precio: Number
});

const Alojamiento = mongoose.model('Alojamiento', alojamientoSchema);

// Definición del esquema y modelo para Pago
const pagoSchema = new mongoose.Schema({
  ID_Pago: String,
  ID_Inscripción: String,
  Monto: Number,
  Fecha_Pago: String,
  Metodo_Pago: String
});

const Pago = mongoose.model('Pago', pagoSchema);

// Cargar datos de Alojamiento desde el archivo JSON
const alojamientos = JSON.parse(fs.readFileSync('./data/alojamientos.json', 'utf8'));

// Cargar datos de Pago desde el archivo JSON
const pagos = JSON.parse(fs.readFileSync('./data/pagos.json', 'utf8'));

// Insertar los datos en MongoDB
Alojamiento.insertMany(alojamientos, (err, docs) => {
  if (err) {
    console.error('Error al insertar alojamientos:', err);
  } else {
    console.log('Alojamientos insertados con éxito:', docs);
  }
});

Pago.insertMany(pagos, (err, docs) => {
  if (err) {
    console.error('Error al insertar pagos:', err);
  } else {
    console.log('Pagos insertados con éxito:', docs);
  }
});
