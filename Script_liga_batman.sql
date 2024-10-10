CREATE TABLE roles(
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(250),
	PRIMARY KEY(id)
);

CREATE TABLE subscriptions (
	id INT NOT NULL AUTO_INCREMENT,
	name TEXT,
	PRIMARY KEY(id)
);

CREATE TABLE calendars (
	id INT NOT NULL AUTO_INCREMENT,
	playtime INT,
	home_team TEXT,
	visit_team TEXT,
	score_ht INT,
	score_vt INT,
	picture_results TEXT,
	PRIMARY KEY(id)
);


CREATE TABLE tournaments (
	id INT NOT NULL AUTO_INCREMENT,
	name TEXT NOT NULL,
	state VARCHAR(250),
	city VARCHAR(250),
	cp VARCHAR(250),
	status BOOL,
	invitation_code VARCHAR(250),
	PRIMARY KEY(id)
	
);

CREATE TABLE users(
	id INT NOT NULL AUTO_INCREMENT,
	name TEXT NOT NULL,
	email VARCHAR(250) UNIQUE,
	pass TEXT,
	account_type TEXT,
	picture TEXT,
	id_suscription INT,
	PRIMARY KEY(id),
	FOREIGN KEY (id_suscription) REFERENCES subscriptions(id)
);


CREATE TABLE teams (
	id INT NOT NULL AUTO_INCREMENT,
	name VARCHAR(250),
	primary_color VARCHAR(250),
	secondary_color VARCHAR(250),
	logo TEXT,
	goals_favor INT,
	goals_against INT,
	red_cards INT,
	yellow_cards INT,
	id_tournament INT,
	PRIMARY KEY(id),
	FOREIGN KEY (id_tournament) REFERENCES tournaments(id)
);

CREATE TABLE players (
	id INT NOT NULL AUTO_INCREMENT,
	name TEXT,
	curp TEXT,
	picture TEXT,
	goals INT,
	red_cards INT,
	yellow_cards INT,
	id_tournament INT,
	id_team INT,
	PRIMARY KEY(id),
	FOREIGN KEY (id_team) REFERENCES teams(id),
	FOREIGN KEY (id_tournament) REFERENCES tournaments(id)
);


CREATE TABLE log_calendars (
	id INT NOT NULL AUTO_INCREMENT,
	playtime INT,
	home_team TEXT,
	visit_team TEXT,
	score_ht INT,
	score_vt INT,
	picture_results TEXT,
	original_play INT,
	PRIMARY KEY(id),
	FOREIGN KEY (original_play) REFERENCES calendars(id)
);

CREATE TABLE user_tournament_rol (
	id INT NOT NULL AUTO_INCREMENT,
	id_user INT,
	id_tournament INT,
	id_rol INT,
	PRIMARY KEY(id),
	FOREIGN KEY (id_user) REFERENCES users(id),
	FOREIGN KEY (id_tournament) REFERENCES tournaments(id),
	FOREIGN KEY (id_rol) REFERENCES roles(id)
);











