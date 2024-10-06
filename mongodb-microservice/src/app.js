const express = require('express');
const mongoose = require('mongoose');
const alojamientoRoutes = require('./routes/alojamientoRoutes');
const pagoRoutes = require('./routes/pagoRoutes');
require('dotenv').config();

const app = express();
const port = process.env.PORT || 8080;

// Middleware
app.use(express.json());

// Rutas
app.use('/api/alojamientos', alojamientoRoutes);
app.use('/api/pagos', pagoRoutes);

// Conectar a MongoDB
mongoose.connect(process.env.MONGODB_URI, {
    useNewUrlParser: true,
    useUnifiedTopology: true
})
    .then(() => console.log('MongoDB conectado...'))
    .catch(err => console.log(err));

// Iniciar el servidor
app.listen(port, () => {
    console.log(`Servidor corriendo en el puerto ${port}`);
});
