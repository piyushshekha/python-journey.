-- 1. Database Setup (Used by python_mysql_bridge.py)
CREATE DATABASE IF NOT EXISTS college;
USE college;

DROP TABLE IF EXISTS course;
DROP TABLE IF EXISTS student;

CREATE TABLE student (
    stu_id INT PRIMARY KEY,
    name VARCHAR(50)
);

CREATE TABLE course (
    stu_id INT PRIMARY KEY,
    course VARCHAR(50)
);

-- 2. Insert Sample Data
INSERT INTO student (stu_id, name) VALUES
(101, 'RAHUL'),
(102, 'KUSHIK'),
(103, 'NIKHIL');

INSERT INTO course (stu_id, course) VALUES
(102, 'ENGLISH'),
(105, 'MATH'),
(103, 'SCIENCE'),
(107, 'COMPUTER SCIENCE');

-- 3. Left Join
SELECT * FROM student AS s
LEFT JOIN course AS c
ON s.stu_id = c.stu_id;

-- 4. Full Exclusive Join (Left Exclusive UNION Right Exclusive)
SELECT * FROM student AS s
LEFT JOIN course AS c
ON s.stu_id = c.stu_id
WHERE c.stu_id IS NULL
UNION
SELECT * FROM student AS s
RIGHT JOIN course AS c
ON s.stu_id = c.stu_id
WHERE s.stu_id IS NULL;

-- 5. Self Join Setup (Employee-Manager Hierarchy)
DROP TABLE IF EXISTS employee;

CREATE TABLE employee (
    id INT PRIMARY KEY,
    name VARCHAR(50),
    manager_id INT
);

INSERT INTO employee (id, name, manager_id) VALUES
(101, 'ADAM', 103),
(102, 'BOB', 104),
(103, 'CASEY', NULL),
(104, 'DONALD', 103);

-- 6. UNION ALL Demo
SELECT name FROM employee
UNION ALL
SELECT name FROM employee;

-- 7. Self Join Query (Find Manager of each Employee)
SELECT a.name AS manager_name, b.name AS employee_name
FROM employee AS a
JOIN employee AS b
ON a.id = b.manager_id;

-- Reset commands (Keep commented so script runs cleanly)
-- TRUNCATE TABLE course;
-- TRUNCATE TABLE employee;Added college SQL schema with joins, union, and Python bridge script"