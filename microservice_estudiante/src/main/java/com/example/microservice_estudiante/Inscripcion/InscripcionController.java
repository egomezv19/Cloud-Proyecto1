package com.example.microservice_estudiante.Inscripcion;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/inscripciones")
public class InscripcionController {

    @Autowired
    private InscripcionService inscripcionService;

    // GET - Obtener todas las inscripciones
    @GetMapping
    public ResponseEntity<List<Inscripcion>> getAllInscripciones() {
        List<Inscripcion> inscripciones = inscripcionService.getAllInscripciones();
        return ResponseEntity.ok(inscripciones);
    }

    // GET - Obtener una inscripcion por id
    @GetMapping("/{id}")
    public ResponseEntity<Inscripcion> getInscripcionById(@PathVariable Long id) {
        Inscripcion inscripcion = inscripcionService.getInscripcionById(id);
        return ResponseEntity.ok(inscripcion);
    }

    // POST - Crear una nueva inscripcion
    @PostMapping
    public ResponseEntity<Inscripcion> createInscripcion(@RequestBody Inscripcion inscripcion) {
        Inscripcion savedInscripcion = inscripcionService.saveInscripcion(inscripcion);
        return ResponseEntity.status(201).body(savedInscripcion);
    }

    // PUT - Actualizar una inscripcion existente
    @PutMapping("/{id}")
    public ResponseEntity<Inscripcion> updateInscripcion(@PathVariable Long id, @RequestBody Inscripcion inscripcionDetails) {
        Inscripcion updatedInscripcion = inscripcionService.updateInscripcion(id, inscripcionDetails);
        return ResponseEntity.ok(updatedInscripcion);
    }

    // DELETE - Eliminar una inscripcion
    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteInscripcion(@PathVariable Long id) {
        inscripcionService.deleteInscripcion(id);
        return ResponseEntity.noContent().build();
    }
}
