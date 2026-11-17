CREATE DATABASE college;
USE college;
DROP TABLE IF EXISTS student;

CREATE TABLE student(
 roll_no INT PRIMARY KEY,
 name VARCHAR(50),
 marks INT NOT NULL,
 grade varchar(1),
 city VARCHAR(20)
 );
 
INSERT INTO student 
(roll_no,name,marks,grade,city)
VALUES
(101,"PIYUSH",88,"A","JAMNAGAR"),
(102,"NIKHIL",45,"C","RAJKOT"),
(103,"SIDHART",55,"B","JAMNAGAR"),
(104,"RAHUL",78,"A","RAJKOT");

SELECT city,AVG(marks) AS average_marks
FROM student
GROUP BY city
ORDER BY city ASC;