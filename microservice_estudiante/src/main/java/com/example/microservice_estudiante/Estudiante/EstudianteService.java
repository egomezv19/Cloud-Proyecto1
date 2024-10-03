package com.example.microservice_estudiante.Estudiante;


import com.example.microservice_estudiante.Exceptions.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class EstudianteService {

    @Autowired
    private EstudianteRepository estudianteRepository;


    public List<Estudiante> getAllEstudiantes() {
        return estudianteRepository.findAll();
    }


    public Estudiante getEstudianteById(Long id) {
        return estudianteRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Estudiante no encontrado con id: " + id));
    }


    public Estudiante saveEstudiante(Estudiante estudiante) {
        return estudianteRepository.save(estudiante);
    }


    public Estudiante updateEstudiante(Long id, Estudiante estudianteDetails) {
        Estudiante estudiante = estudianteRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Estudiante no encontrado con id: " + id));

        estudiante.setNombre(estudianteDetails.getNombre());
        estudiante.setEmail(estudianteDetails.getEmail());
        estudiante.setTelefono(estudianteDetails.getTelefono());
        estudiante.setDni(estudianteDetails.getDni());

        return estudianteRepository.save(estudiante);
    }


    public void deleteEstudiante(Long id) {
        Estudiante estudiante = estudianteRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Estudiante no encontrado con id: " + id));
        estudianteRepository.delete(estudiante);
    }
}

