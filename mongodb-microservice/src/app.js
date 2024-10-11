require('dotenv').config();
const express = require('express');
const mongoose = require('mongoose');
const alojamientoRoutes = require('./routes/alojamientoRoutes');
const pagoRoutes = require('./routes/pagoRoutes');
const swaggerUi = require('swagger-ui-express');
const swaggerJsDoc = require('swagger-jsdoc');
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

const swaggerOptions = {
    swaggerDefinition: {
        openapi: '3.0.0',
        info: {
            title: 'API de Alojamientos y Pagos',
            version: '1.0.0',
            description: 'Documentación de la API para gestionar alojamientos y pagos',
            contact: {
                name: 'Soporte',
                email: 'soporte@tuempresa.com'
            },
        },
        servers: [
            {
                url: 'http://localhost:8080',
                description: 'Servidor de desarrollo'
            }
        ],
    },
    apis: ['./routes/*.js'],
};

const swaggerDocs = swaggerJsDoc(swaggerOptions);
app.use('/api-docs', swaggerUi.serve, swaggerUi.setup(swaggerDocs));
