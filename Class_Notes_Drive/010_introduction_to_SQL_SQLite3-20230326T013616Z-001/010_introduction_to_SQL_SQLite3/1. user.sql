create table users (
 id INT primary key,
 name varchar not null,
 address varchar not null
);

insert into 
users ('id','name', 'address') 
values 
(1, 'Ramesh Pradhan', 'Lalitpur'), 
(2, 'Hari Bahadur', 'Kathmandu'), 
(3, 'Madan Bahadur', "Kathmanud");

insert into 
users ('id','name', 'address') 
values 
(4, 'Sita Dhakal', 'Lalitpur'),
(5, 'Gita Shrestha', 'Kathmandu'), 
(6, 'Maya Khanal', "Kathmanud");

select * from users;

alter table users add gender varchar(1) DEFAULT 'M';

select * from users ;

update users set gender = 'F' where id=4 or id=5 or id=6;

select * from users u where u.address == 'Lalitpur';

select * from users where name LIKE 'r%';

select * from users where name LIKE '%l';

select * from users where name LIKE '%i%';

select * from users where name LIKE '_i%';

select * from users where name LIKE '%a_';


