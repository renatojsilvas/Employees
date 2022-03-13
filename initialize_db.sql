CREATE TABLE IF NOT EXISTS employees (
	id serial PRIMARY KEY,
	name VARCHAR ( 200 ) NOT NULL,	
	email VARCHAR ( 255 ) UNIQUE NOT NULL,
	department VARCHAR ( 50 ) NOT NULL);

DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM employees) THEN
      INSERT INTO 
		employees (name, email, department)
	  VALUES
		('Felipe Morais', 'felipe.morais@igs-software.com.br', 'Tester'),
		('Tatiane Laura', 'tatiane.laura@igs-software.com.br', 'Developer'),
		('Mauricio Alegretti', 'mauricio.alegretti@igs-software.com.br', 'RH');  
   END IF;
END
$do$