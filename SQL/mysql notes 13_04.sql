create database  pfs45_46;

use PFS45_46;

create table if not exists student_ (std_id char(10),name varchar(20),age int,email char(30),
mobile bigint);

describe student;

select * from pfs45_46.student;

insert into student values("s125","rajesh","35",'rajesh.s125@gmail.com',9234567801),
("s126","vinay","37",'vinay.s126@gmail.com',9345678012);

insert into student values("s123","pavan",40,'pavan>s123@gmail.com',9012345678);

select std_id,age,name from student_;

insert into student (std_id,age,name) values("s127",25,"bharat");

insert into student (std_id,age,name) values("s128",28,"ravena"),("s129",39,"sarath");

truncate student;

drop table student;