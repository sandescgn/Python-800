create table student(
	id int primary key,
	name varchar not null,
	address varchar not null,
	college varchar not null,
	age int not null,
	gender varchar(1) not null,
	faculty varchar not null
);

INSERT into student 
('id', 'name', 'address', 'college', 'age', 'gender', 'faculty')
values
(1, 'ram', 'kathmandu', 'ncit', 18, 'm', 'IT'),
(2, 'shyam', 'lalitpur', 'islington', 20, 'm', 'CSIT'),
(3, 'gita', 'pokhara', 'ncit', 21, 'f', 'SE'),
(4, 'sita', 'kathmandu', 'ioe pulchowk', 24, 'f','CE');

-- get all columns from student table
SELECT * from student;

SELECT name, address from student;

UPDATE student set address = 'lalitpur' where id = 3;

ALTER table student add university default 'TU';

UPDATE student set university = 'UK' where college='islington';

UPDATE student set university = 'PK' where id=1 or id=3;

DELETE from student where id = 3;

INSERT into student 
('id', 'name', 'address', 'college', 'age', 'gender', 'faculty')
values
(3, 'gita', 'pokhara', 'ncit', 21, 'f', 'SE'),
(5, 'hari', 'kathmandu', 'ioe pulchowk', 24, 'm','CIVIL'),
(6, 'madan', 'pokhara', 'ncit', 21, 'f', 'SE'),
(7, 'maya', 'kathmandu', 'isglington', 24, 'f','BIT');

UPDATE student set gender  = 'm' where id=6;

SELECT * from student where gender = 'f';

SELECT * from student where age > 20;

SELECT * from student where age > 20 and gender = 'm';

SELECT * from student WHERE age >= 20 and age <=25;

SELECT * FROM student where age BETWEEN 20 and 25;

SELECT * FROM student where age BETWEEN 20 and 25 order by age;

SELECT * FROM student where age BETWEEN 20 and 25 order by age desc;

SELECT * FROM student where age BETWEEN 20 and 25 order by age desc, gender asc;

SELECT * FROM student where address ='kathmandu' and gender = 'm' and college = 'ioe pulchowk';

SELECT * FROM student where 
(address = 'kathmandu' AND college = 'ncit') 
or (address='pokhara' and college='ncit');

SELECT * FROM student where 
(address = 'kathmandu' AND college = 'ncit') 
or (address='pokhara' and college='ncit') and gender = 'm';


SELECT * FROM student where 
(
	(address = 'kathmandu' AND college = 'ncit') 
	or (address='pokhara' and college='ncit')
) and (gender = 'm');


SELECT * FROM student where 
(
	(address = 'kathmandu' AND college = 'ncit' and gender = 'm') 
	or (address='pokhara' and college='ncit' and gender = 'm')
);

SELECT * FROM student where 
(address = 'Kathmandu' AND college = 'ncit') 
or (address='Pokhara' and college='ncit') and gender = 'm';

SELECT * from student;

SELECT * from student WHERE name like 'm%';

SELECT * from student WHERE name like '%a';

SELECT * from student WHERE name like 'g%a';

SELECT * from student WHERE name like '%it%';

SELECT * from student WHERE name like '_i%';

SELECT * from student WHERE name like '%t_';

ALTER table student add contact varchar(20);

ALTER table student add email varchar(20);







