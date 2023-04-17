----------------------------------------------------------------------------------
--- user table
----------------------------------------------------------------------------------
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

insert into 
users ('id','name', 'address') 
values 
(9, 'Daya Khanal', "Lalitpur");

select * from users;

alter table users add gender varchar(1) DEFAULT 'M';

select * from users;

update users set gender = 'F' where id=4 or id=5 or id=6;

select name, address from users;

select DISTINCT address from users;

select * from users where address = 'Kathmanud';

update users set address = 'Kathamandu' where id=3 or id=6;

update users set address = 'Kathamandu' where id=7;

select * from users where address = 'Kathmanud';
----------------------------------------------------------------------------------