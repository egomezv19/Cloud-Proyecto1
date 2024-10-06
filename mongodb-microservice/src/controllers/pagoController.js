const Pago = require('../models/pago');

// Obtener todos los pagos
exports.getAllPagos = async (req, res) => {
    try {
        const pagos = await Pago.find();
        res.status(200).json(pagos);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Crear un nuevo pago
exports.createPago = async (req, res) => {
    const newPago = new Pago(req.body);
    try {
        const savedPago = await newPago.save();
        res.status(201).json(savedPago);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
};

// Obtener un pago por ID
exports.getPagoById = async (req, res) => {
    try {
        const pago = await Pago.findById(req.params.id);
        if (!pago) return res.status(404).json({ message: 'Pago no encontrado' });
        res.status(200).json(pago);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Actualizar un pago
exports.updatePago = async (req, res) => {
    try {
        const updatedPago = await Pago.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updatedPago) return res.status(404).json({ message: 'Pago no encontrado' });
        res.status(200).json(updatedPago);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Eliminar un pago
exports.deletePago = async (req, res) => {
    try {
        const deletedPago = await Pago.findByIdAndDelete(req.params.id);
        if (!deletedPago) return res.status(404).json({ message: 'Pago no encontrado' });
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};
