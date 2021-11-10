CREATE TABLE Location(
	ID INT PRIMARY KEY,
	name VARCHAR(64) NOT NULL,
	type VARCHAR(64),
	dimension VARCHAR(64),
	created_at VARCHAR(64) NOT NULL
);

CREATE TABLE Episode(
	ID INT PRIMARY KEY,
	name VARCHAR(64) NOT NULL,
	air_date VARCHAR(64),
	episode_code VARCHAR(64),
	created_at VARCHAR(64) NOT NULL
);

CREATE TYPE type_character AS ENUM('Alive', 'Dead', 'unknown');
CREATE TYPE type_gender AS ENUM('Female', 'Male', 'Genderless', 'unknown');
CREATE TABLE Character(
	ID INT PRIMARY KEY,
	name VARCHAR(64) NOT NULL,
	status type_character,
	specie VARCHAR(64),
	subspecies VARCHAR(64),
	gender type_gender,
	id_origin INT,
	id_last_location INT,
	created_at VARCHAR(64) NOT NULL,
	FOREIGN KEY (id_origin) REFERENCES Location(ID),
	FOREIGN KEY (id_last_location) REFERENCES Location(ID)
);

CREATE TABLE Appear(
	ID SERIAL PRIMARY KEY,
	character_id INT NOT NULL,
	episode_id INT NOT NULL,
	FOREIGN KEY (character_id) REFERENCES Character(ID),
	FOREIGN KEY (episode_id) REFERENCES Episode(ID),
	UNIQUE(character_id, episode_id)
);

SELECT * FROM Character;
SELECT * FROM Location;
SELECT * FROM Episode;
SELECT * FROM Appear;
