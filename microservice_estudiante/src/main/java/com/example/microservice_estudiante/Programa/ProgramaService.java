package com.example.microservice_estudiante.Programa;

import com.example.microservice_estudiante.Exceptions.ResourceNotFoundException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class ProgramaService {

    @Autowired
    private ProgramaRepository programaRepository;


    public List<Programa> getAllProgramas() {
        return programaRepository.findAll();
    }


    public Programa getProgramaById(Long id) {
        return programaRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Programa no encontrado con id: " + id));
    }


    public Programa savePrograma(Programa programa) {
        return programaRepository.save(programa);
    }


    public Programa updatePrograma(Long id, Programa programaDetails) {
        Programa programa = programaRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Programa no encontrado con id: " + id));

        programa.setNombre(programaDetails.getNombre());
        programa.setDescripcion(programaDetails.getDescripcion());
        programa.setFecha_inicio(programaDetails.getFecha_inicio());
        programa.setFecha_final(programaDetails.getFecha_final());

        return programaRepository.save(programa);
    }


    public void deletePrograma(Long id) {
        Programa programa = programaRepository.findById(id)
                .orElseThrow(() -> new ResourceNotFoundException("Programa no encontrado con id: " + id));
        programaRepository.delete(programa);
    }
}
