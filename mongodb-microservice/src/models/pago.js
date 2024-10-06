const mongoose = require('mongoose');

const pagoSchema = new mongoose.Schema({
    ID_Pago: { type: String, required: true },
    ID_Inscripción: { type: String, required: true },
    Monto: { type: Number, required: true },
    Fecha_Pago: { type: Date, required: true },
    Metodo_Pago: { type: String, required: true }
});

module.exports = mongoose.model('Pago', pagoSchema);
