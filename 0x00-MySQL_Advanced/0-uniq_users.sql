-- create a table users with the following fields
-- id, email, name
CREATE TABLE IF NOT EXISTS users (
	id INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
	email VARCHAR(255) NOT NULL UNIQUE,
	name VARCHAR(255)
)
