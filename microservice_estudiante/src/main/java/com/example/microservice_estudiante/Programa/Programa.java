package com.example.microservice_estudiante.Programa;

import com.example.microservice_estudiante.Inscripcion.Inscripcion;
import com.fasterxml.jackson.annotation.JsonIdentityInfo;
import com.fasterxml.jackson.annotation.ObjectIdGenerators;
import jakarta.persistence.*;
import lombok.Getter;
import lombok.Setter;

import java.util.List;

@Entity
@Getter
@Setter
@JsonIdentityInfo(generator= ObjectIdGenerators.PropertyGenerator.class, property="id", scope = Programa.class)
public class Programa {
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private long id;
    private String nombre;
    private String descripcion;
    private String fecha_inicio;
    private String fecha_final;

    // Relación Uno a Muchos con Inscripcion
    @OneToMany(mappedBy = "programa")
    private List<Inscripcion> inscripciones;

}
