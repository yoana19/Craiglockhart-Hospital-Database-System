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

INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("John", "Layard", "26", "", "", "", "");
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("Siegfried", "Sassoon", "31", "shell-shocked", "officer", "upper-class aristocrat", "war poet");
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("David", "Burns", "22", "cannot eat without throwing up", "officer", ?, ?);
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES ("Billy", "Prior", "23", "mutism, asthma", "officer", "working class", ?);
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES (?, "Anderson", "30", "unable to tolerate the sight of blood", "surgeon", ?, ?);
INSERT INTO patients (first_name, last_name, age, diagnosis, military_status, social_status, add_occupation) VALUES (?, "Willard", "25", "hypochondriasis", ?, ?, ?);


INSERT INTO doctors (name, age, occupation) VALUES ("Bryce", "old", "psychiatrist");
INSERT INTO doctors (name, age, occupation) VALUES ("Rivers", "old", "psychiatrist (has war neurosis)");
