# Creating table students

CREATE TABLE students (
 id INT NOT NULL AUTO_INCREMENT,
 lastname VARCHAR(20) NOT NULL,
 firstname VARCHAR(20) NOT NULL,
 email VARCHAR(50) NOT NULL,
 age SMALLINT NOT NULL,
 ssn VARCHAR(10) NOT NULL UNIQUE,
 primary key (id)
 );

# Creating table courses

 CREATE TABLE courses (
 id INT NOT NULL AUTO_INCREMENT,
 name VARCHAR(50) NOT NULL,
 number VARCHAR(7) NOT NULL,
 description VARCHAR(255) NOT NULL,
 primary key (id)
 );


 # Creating table staff

 CREATE TABLE staff (
 id INT NOT NULL AUTO_INCREMENT,
 lastname VARCHAR(20) NOT NULL,
 firstname VARCHAR(20) NOT NULL,
 email VARCHAR(50) NOT NULL,
 age SMALLINT NOT NULL,
 ssn VARCHAR(10) NOT NULL UNIQUE,
 primary key (id)
 );



