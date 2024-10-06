# Utiliza una imagen base oficial de Node.js
FROM node:14

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias package.json y package-lock.json
COPY package*.json ./

# Instala las dependencias de Node.js
RUN npm install

# Copia todo el resto del código de la aplicación al contenedor
COPY . .

# Expone el puerto que tu aplicación utilizará
EXPOSE 3000

# Define el comando que se ejecutará cuando el contenedor arranque
CMD ["node", "ingest_mongodb.js"]
