const mongoose = require('mongoose');

const alojamientoSchema = new mongoose.Schema({
    ID_Alojamiento: { type: String, required: true },
    ID_Programa: { type: String, required: true },
    Descripción: { type: String, required: true },
    Dirección: { type: String, required: true },
    Precio: { type: Number, required: true }
});

module.exports = mongoose.model('Alojamiento', alojamientoSchema);
