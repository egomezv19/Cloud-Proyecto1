
FROM openjdk:17-jdk-alpine
WORKDIR /app
COPY target/microservice_estudiante-0.0.1-SNAPSHOT.jar /app/microservice_estudiante.jar
EXPOSE 8080
ENTRYPOINT ["java", "-jar", "/app/microservice_estudiante.jar"]
