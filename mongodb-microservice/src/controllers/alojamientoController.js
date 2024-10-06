const Alojamiento = require('../models/alojamiento');

// Obtener todos los alojamientos
exports.getAllAlojamientos = async (req, res) => {
    try {
        const alojamientos = await Alojamiento.find();
        res.status(200).json(alojamientos);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Crear un nuevo alojamiento
exports.createAlojamiento = async (req, res) => {
    const newAlojamiento = new Alojamiento(req.body);
    try {
        const savedAlojamiento = await newAlojamiento.save();
        res.status(201).json(savedAlojamiento);
    } catch (error) {
        res.status(400).json({ message: error.message });
    }
};

// Obtener un alojamiento por ID
exports.getAlojamientoById = async (req, res) => {
    try {
        const alojamiento = await Alojamiento.findById(req.params.id);
        if (!alojamiento) return res.status(404).json({ message: 'Alojamiento no encontrado' });
        res.status(200).json(alojamiento);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Actualizar un alojamiento
exports.updateAlojamiento = async (req, res) => {
    try {
        const updatedAlojamiento = await Alojamiento.findByIdAndUpdate(req.params.id, req.body, { new: true });
        if (!updatedAlojamiento) return res.status(404).json({ message: 'Alojamiento no encontrado' });
        res.status(200).json(updatedAlojamiento);
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};

// Eliminar un alojamiento
exports.deleteAlojamiento = async (req, res) => {
    try {
        const deletedAlojamiento = await Alojamiento.findByIdAndDelete(req.params.id);
        if (!deletedAlojamiento) return res.status(404).json({ message: 'Alojamiento no encontrado' });
        res.status(204).send();
    } catch (error) {
        res.status(500).json({ message: error.message });
    }
};
