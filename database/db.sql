CREATE TABLE Location(
    location_id INT PRIMARY KEY,
    location_name VARCHAR(64) NOT NULL,
    location_type VARCHAR(64),
    dimension VARCHAR(64),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE Episode(
    episode_id INT PRIMARY KEY,
    episode_name VARCHAR(64) NOT NULL,
    air_date VARCHAR(64),
    episode_code VARCHAR(64),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TYPE type_character AS ENUM('Alive', 'Dead', 'unknown');
CREATE TYPE type_gender AS ENUM('Female', 'Male', 'Genderless', 'unknown');
CREATE TABLE Character(
    character_id INT PRIMARY KEY,
    character_name VARCHAR(64) NOT NULL,
    status type_character,
    specie VARCHAR(64),
    subspecie VARCHAR(64),
    gender type_gender,
    id_origin INT,
    id_last_location INT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (id_origin) REFERENCES Location(ID),
    FOREIGN KEY (id_last_location) REFERENCES Location(ID)
);

CREATE TABLE Appear(
    appear_id SERIAL PRIMARY KEY,
    character_id_fk INT NOT NULL,
    episode_id_fk INT NOT NULL,
    FOREIGN KEY (character_id_fk) REFERENCES Character(character_id),
    FOREIGN KEY (episode_id_fk) REFERENCES Episode(episode_id),
    UNIQUE(character_id_fk, episode_id_fk)
);

CREATE ROLE superuser;
GRANT ALL PRIVILEGES ON DATABASE "ricknmorty" TO superuser;
GRANT ALL ON ALL TABLES IN SCHEMA public TO superuser;

CREATE USER master WITH PASSWORD 'senhamaster123';

GRANT superuser TO master;

CREATE USER usr WITH PASSWORD 'senhausr123';
GRANT SELECT ON ALL TABLES IN SCHEMA public TO usr;
GRANT USAGE ON SCHEMA public TO usr;

CREATE INDEX character_specie_index ON character(specie);
