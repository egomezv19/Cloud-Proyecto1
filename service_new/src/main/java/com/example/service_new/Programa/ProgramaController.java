package com.example.service_new.Programa;


import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/programas")
public class ProgramaController {

    @Autowired
    private ProgramaService programaService;


    @GetMapping
    public ResponseEntity<List<Programa>> getAllProgramas() {
        List<Programa> programas = programaService.getAllProgramas();
        return ResponseEntity.ok(programas);
    }


    @GetMapping("/{id}")
    public ResponseEntity<Programa> getProgramaById(@PathVariable Long id) {
        Programa programa = programaService.getProgramaById(id);
        return ResponseEntity.ok(programa);
    }


    @PostMapping
    public ResponseEntity<Programa> createPrograma(@RequestBody Programa programa) {
        Programa savedPrograma = programaService.savePrograma(programa);
        return ResponseEntity.status(201).body(savedPrograma);
    }


    @PutMapping("/{id}")
    public ResponseEntity<Programa> updatePrograma(@PathVariable Long id, @RequestBody Programa programaDetails) {
        Programa updatedPrograma = programaService.updatePrograma(id, programaDetails);
        return ResponseEntity.ok(updatedPrograma);
    }


    @DeleteMapping("/{id}")
    public ResponseEntity<Void> deletePrograma(@PathVariable Long id) {
        programaService.deletePrograma(id);
        return ResponseEntity.noContent().build();
    }
}

