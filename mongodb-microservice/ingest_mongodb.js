const express = require('express');
const MongoClient = require('mongodb').MongoClient;
const fs = require('fs');
const app = express();

// Conexión a MongoDB
const url = 'mongodb://mongo:27017'; // Conexión dentro del contenedor
const dbName = 'universidad';

// Función para insertar datos
async function insertData(collectionName, data) {
    const client = new MongoClient(url, { useNewUrlParser: true, useUnifiedTopology: true });
    try {
        await client.connect();
        console.log(`Conectado a MongoDB, colección: ${collectionName}`);

        const db = client.db(dbName);
        const collection = db.collection(collectionName);
        
        // Inserta los datos en la colección
        await collection.insertMany(data);
        console.log(`Datos insertados en la colección ${collectionName}`);

    } catch (err) {
        console.error(err);
    } finally {
        await client.close();
    }
}

// Lee los archivos JSON y los inserta en MongoDB
const alojamientos = JSON.parse(fs.readFileSync('./data/alojamientos.json', 'utf8')).alojamientos;
const pagos = JSON.parse(fs.readFileSync('./data/pagos.json', 'utf8')).pagos;

insertData('alojamientos', alojamientos);
insertData('pagos', pagos);

// Servidor Express para exponer una API básica
app.get('/', (req, res) => {
    res.send('Microservicio de MongoDB con Node.js');
});

app.listen(8080, () => {
    console.log('Microservicio ejecutándose en el puerto 8080');
});
