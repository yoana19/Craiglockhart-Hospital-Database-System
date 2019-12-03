CREATE TABLE patients (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT,
	last_name TEXT,
	age TEXT,
	diagnosis TEXT,
	military_status TEXT,
	social_status TEXT,
	add_occupation TEXT
    
);

CREATE TABLE doctors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
	age TEXT,
	occupation TEXT
    
);

INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("Layard", "John", ?, ?, ?, ?, ?);
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("Siegfried", "Sassoon", "young", ?, "officer", "upper-class aristocrat", "war poet");
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("David", "Burns", ?, ?, "officer", ?, ?);
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("Billy", "Prior", ?, ?, "officer", "working class", ?);
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES (?, "Anderson", ?, ?, "surgeon", ?,?);


INSERT INTO doctors (name, age, occupation) VALUES ("Bryce", "old", "psychiatrist");
INSERT INTO doctors (name, age, occupation) VALUES ("Rivers", "old", "psychiatrist");