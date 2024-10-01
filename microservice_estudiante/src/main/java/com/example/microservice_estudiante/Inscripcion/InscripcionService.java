package com.example.microservice_estudiante.Inscripcion;

import com.example.microservice_estudiante.Exceptions.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class InscripcionService {

    @Autowired
    private InscripcionRepository inscripcionRepository;

    // Obtener todas las inscripciones
    public List<Inscripcion> getAllInscripciones() {
        return inscripcionRepository.findAll();
    }

    // Obtener una inscripcion por id
    public Inscripcion getInscripcionById(Long id) {
        return inscripcionRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Inscripción no encontrada con id: " + id));
    }

    // Crear una nueva inscripcion
    public Inscripcion saveInscripcion(Inscripcion inscripcion) {
        return inscripcionRepository.save(inscripcion);
    }

    // Actualizar una inscripcion existente
    public Inscripcion updateInscripcion(Long id, Inscripcion inscripcionDetails) {
        Inscripcion inscripcion = inscripcionRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Inscripción no encontrada con id: " + id));

        inscripcion.setFecha(inscripcionDetails.getFecha());
        inscripcion.setEstado(inscripcionDetails.getEstado());

        return inscripcionRepository.save(inscripcion);
    }

    // Eliminar una inscripcion
    public void deleteInscripcion(Long id) {
        Inscripcion inscripcion = inscripcionRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Inscripción no encontrada con id: " + id));
        inscripcionRepository.delete(inscripcion);
    }
}
