package com.galille.tp2sae_h2;

import com.galille.tp2sae_h2.entities.Adherent;
import com.galille.tp2sae_h2.repository.AdherentRepository;
import org.springframework.boot.CommandLineRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;

@SpringBootApplication
public class Tp2SaeH2Application {

    public static void main(String[] args) {
        SpringApplication.run(Tp2SaeH2Application.class, args);
    }
@Bean
    CommandLineRunner runner(AdherentRepository repository) {
        return args -> {
            repository.save(new Adherent(null, "A", "B", 29));
            repository.save(new Adherent(null, "A", "B", 29));
            repository.save(new Adherent(null, "A", "B", 29));
            repository.save(new Adherent(null, "A", "B", 29));
        };
    }
}