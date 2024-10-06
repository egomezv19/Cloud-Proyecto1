const express = require('express');
const router = express.Router();
const alojamientoController = require('../controllers/alojamientoController');

router.get('/', alojamientoController.getAllAlojamientos);
router.post('/', alojamientoController.createAlojamiento);
router.get('/:id', alojamientoController.getAlojamientoById);
router.put('/:id', alojamientoController.updateAlojamiento);
router.delete('/:id', alojamientoController.deleteAlojamiento);

module.exports = router;
