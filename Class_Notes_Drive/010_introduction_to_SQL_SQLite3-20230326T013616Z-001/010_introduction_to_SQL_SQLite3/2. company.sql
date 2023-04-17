----------------------------------------------------------------------------------
--- company table
----------------------------------------------------------------------------------
CREATE TABLE company (
   id INTEGER PRIMARY KEY AUTOINCREMENT,
   name TEXT NOT NULL,
   age INT NOT NULL,
   address CHAR(50),
   salary REAL
);

insert into 
company ('name','age', 'address', 'salary') 
values 
('Ramesh Pradhan', 95, 'Lalitpur', 10000), 
('Hari Bahadur', 45, 'Kathmandu', 15000), 
('Madan Bahadur', 36, 'Kathmandu', 13000),
('Sita Devi', 36, "Kathmanud", 12000),
('Gita Maya', 32, "Kathmanud", 5000),
('Maya Devi', 31, 'Lalitpur', 8000);


DELETE from company where id=1;
DELETE from company where id=2 or id=3;
DELETE from company ;

ALTER TABLE company 
RENAME COLUMN salary TO max_offered_salary;

ALTER TABLE company 
DROP COLUMN age;

insert into 
company ('name','address', 'max_offered_salary') 
values 
('Broadway Infosys', "Kathmanud", 5000),
('Google',  'Lalitpur', 10000), 
('Meta', 'Kathmandu', 15000), 
('Stack OverFlow', 'Kathmandu', 13000),
('Turing', "Kathmanud", 12000),
('Tesla', 'Lalitpur', 8000);

update company set address = 'Kathamandu' where name="Turing" or name='Broadway Infosys';

SELECT * from company;

SELECT * FROM company where address = 'Kathmandu' and max_offered_salary >= 15000;

SELECT * FROM company where (address = 'Kathmandu' and max_offered_salary > 15000);

SELECT * FROM company where 
(address = 'Kathmandu' and max_offered_salary > 15000) 
or address ='Lalitpur';

SELECT * FROM company where 
(address = 'Kathmandu' and max_offered_salary > 15000) 
or 
(address ='Lalitpur' and max_offered_salary > 2000);