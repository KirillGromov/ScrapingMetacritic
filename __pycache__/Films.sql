drop database if exists films
CREATE DATABASE films
    DEFAULT CHARACTER SET utf8
    DEFAULT COLLATE utf8_general_ci;
USE films;

CREATE TABLE film (
	id INT AUTO_INCREMENT PRIMARY KEY UNIQUE,
	name CHAR(255) NOT NULL,
    picture CHAR(255),
    date CHAR(255) NOT NULL,
    score CHAR(255),
	mppa VARCHAR(255)
);
