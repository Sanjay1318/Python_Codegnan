use pfs45_46;
select * from student ;
insert into student values("s123","sivakrishna",28,"sivakrishna@gamil.com",
9012345678),("s124","ramakrishna",35,"rk@gmail.com",9102345678);

insert into student(std_id,name,age,mobile) values("s125","vikaram",40,9120345678);

select std_id,name,mobile,email,age from student where name <> "sivakrishna";

update student set  email="vikram@gmail.com" where name="vikaram";

delete from student where age > 30;

set sql_safe_updates=1;

update student set name="vikram",email="vk@gmail.com" where name="vikaram";

rename table student to std_info;

select * from std_info;

alter table std_info rename student_data;

select * from student_data;

alter table student_data rename column name  to s_name;


alter table student_data rename column age to s_age,
rename column  email to s_email, rename column mobile to s_mobile;

alter table student_data change s_name   name char(30);

alter table student_data change s_age age char(3),
change s_email email varchar(40);


