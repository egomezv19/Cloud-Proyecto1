package com.example.microservice_estudiante.Estudiante;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/estudiantes")
public class EstudianteController {

    @Autowired
    private EstudianteService estudianteService;


    @GetMapping
    public ResponseEntity<List<Estudiante>> getAllEstudiantes() {
        List<Estudiante> estudiantes = estudianteService.getAllEstudiantes();
        return ResponseEntity.ok(estudiantes);
    }


    @GetMapping("/{id}")
    public ResponseEntity<Estudiante> getEstudianteById(@PathVariable Long id) {
        Estudiante estudiante = estudianteService.getEstudianteById(id);
        return ResponseEntity.ok(estudiante);
    }


    @PostMapping
    public ResponseEntity<Estudiante> createEstudiante(@RequestBody Estudiante estudiante) {
        Estudiante savedEstudiante = estudianteService.saveEstudiante(estudiante);
        return ResponseEntity.status(201).body(savedEstudiante);
    }


    @PutMapping("/{id}")
    public ResponseEntity<Estudiante> updateEstudiante(@PathVariable Long id, @RequestBody Estudiante estudianteDetails) {
        Estudiante updatedEstudiante = estudianteService.updateEstudiante(id, estudianteDetails);
        return ResponseEntity.ok(updatedEstudiante);
    }


    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deleteEstudiante(@PathVariable Long id) {
        estudianteService.deleteEstudiante(id);
        return ResponseEntity.noContent().build();
    }
}
