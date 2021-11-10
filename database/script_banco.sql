CREATE TABLE Localicazao(
	ID SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	tipo VARCHAR(255) NOT NULL,
	dimensao VARCHAR(255) NOT NULL
);

CREATE TABLE Personagem(
	ID SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	status VARCHAR(255) NOT NULL,
	especie VARCHAR(255) NOT NULL,
	subespecie VARCHAR(255) NOT NULL,
	genero VARCHAR(255) NOT NULL,
	id_origem INT NOT NULL,
	FOREIGN KEY (id_origem) REFERENCES Localicazao(ID)
);

CREATE TABLE Episodio(
	ID SERIAL PRIMARY KEY,
	nome VARCHAR(255) NOT NULL,
	data_exibicao VARCHAR(255) NOT NULL,
	codigo_exibicao VARCHAR(255) NOT NULL
);

CREATE TABLE Aparece(
	ID SERIAL PRIMARY KEY,
	ID_personagem INT NOT NULL,
	ID_episodio INT NOT NULL,
	FOREIGN KEY (ID_personagem) REFERENCES Personagem(ID),
	FOREIGN KEY (ID_episodio) REFERENCES Episodio(ID),
	UNIQUE(ID_personagem, ID_episodio)
);