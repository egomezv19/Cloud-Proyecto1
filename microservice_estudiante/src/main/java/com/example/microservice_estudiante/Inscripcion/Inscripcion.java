package com.example.microservice_estudiante.Inscripcion;

import com.example.microservice_estudiante.Estudiante.Estudiante;
import com.example.microservice_estudiante.Programa.Programa;
import com.fasterxml.jackson.annotation.JsonFormat;
import com.fasterxml.jackson.annotation.JsonIdentityInfo;
import com.fasterxml.jackson.annotation.ObjectIdGenerators;
import jakarta.persistence.*;
import lombok.Data;
import lombok.Getter;
import lombok.Setter;

import java.util.Date;

@Entity
@Getter
@Setter
@JsonIdentityInfo(generator= ObjectIdGenerators.PropertyGenerator.class, property="id", scope = Inscripcion.class)
public class Inscripcion {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    @JsonFormat(pattern="yyyy-MM-dd HH:mm:ss")
    @Temporal(TemporalType.TIMESTAMP)
    private Date fecha;
    private String estado; // no se si hacerlo bool o que xd

    // Relación Muchos a Uno con Estudiante
    @ManyToOne
    @JoinColumn(name = "estudiante_id")
    private Estudiante estudiante;

    // Relación Muchos a Uno con Programa
    @ManyToOne
    @JoinColumn(name = "programa_id")
    private Programa programa;
    @PrePersist
    protected void onCreate() {
        this.fecha = new Date();
    }
}
