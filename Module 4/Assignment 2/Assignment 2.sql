CREATE DATABASE GoogleCompany;
USE GoogleCompany;
-- Google Salaries Table Creation 
CREATE TABLE google_salaries (
    Empid INT PRIMARY KEY,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    department VARCHAR(50),
    education VARCHAR(50),
    salary INT
);
-- Google Laptop Table Creation  
CREATE TABLE google_laptop (
    LaptopId INT PRIMARY KEY,
    Empid INT,
    Brand VARCHAR(50),
    Price INT,
    FOREIGN KEY (Empid) REFERENCES google_salaries(Empid)
);
-- Data insertion into Google_Salaries 
INSERT INTO google_salaries VALUES
(376, 'Gary', 'Stokes', 'Accounting', 'Master', 56760),
(377, 'Lorenzo', 'Cortez', 'Accounting', 'Doctorate', 74127),
(378, 'Roberta', 'Mcgee', 'Administration', 'Primary', 23987),
(379, 'Myrtle', 'Munoz', 'Administration', 'Primary', 31079),
(380, 'Molly', 'Walker', 'Administration', 'Primary', 20725),
(381, 'Maria', 'Simmons', 'Administration', 'Secondary', 39723),
(382, 'Muriel', 'Hernandez', 'Administration', 'Bachelor', 58555),
(383, 'Andres', 'Watson', 'BI', 'Bachelor', 56834),
(384, 'Wayne', 'Leonard', 'BI', 'Master', 65180),
(385, 'Julius', 'Poole', 'BI', 'Master', 55842);
-- Data Insertion into google laptop 
INSERT INTO google_laptop VALUES
(100, 376, 'Bran1', 567600),
(101, 377, 'Bran3', 741270),
(102, 378, 'Bran4', 239870),
(103, 379, 'Bran10', 310790),
(104, 380, 'Bran2', 207250),
(105, 381, 'Bran5', 397230),
(106, 382, 'Bran8', 585550),
(107, 383, 'Bran9', 568340),
(108, 384, 'Bran7', 651800),
(109, 385, 'Bran6', 558420);

-- Which Laptop Assigned to which employee 

SELECT 
    gl.LaptopId,
    gl.Empid,
    gl.Brand,
    gl.Price,
    gs.first_name,
    gs.last_name
FROM 
    google_laptop gl
JOIN 
    google_salaries gs
ON 
    gl.Empid = gs.Empid;
