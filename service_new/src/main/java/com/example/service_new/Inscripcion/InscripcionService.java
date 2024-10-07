package com.example.service_new.Inscripcion;

import com.example.service_new.Exceptions.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class InscripcionService {

    @Autowired
    private InscripcionRepository inscripcionRepository;


    public List<Inscripcion> getAllInscripciones() {
        return inscripcionRepository.findAll();
    }


    public Inscripcion getInscripcionById(Long id) {
        return inscripcionRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Inscripción no encontrada con id: " + id));
    }


    public Inscripcion saveInscripcion(Inscripcion inscripcion) {
        return inscripcionRepository.save(inscripcion);
    }


    public Inscripcion updateInscripcion(Long id, Inscripcion inscripcionDetails) {
        Inscripcion inscripcion = inscripcionRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Inscripción no encontrada con id: " + id));

        inscripcion.setFecha(inscripcionDetails.getFecha());
        inscripcion.setEstado(inscripcionDetails.getEstado());

        return inscripcionRepository.save(inscripcion);
    }


    public void deleteInscripcion(Long id) {
        Inscripcion inscripcion = inscripcionRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Inscripción no encontrada con id: " + id));
        inscripcionRepository.delete(inscripcion);
    }
}
