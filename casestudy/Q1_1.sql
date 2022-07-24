create database my_db;
use my_db;
create user 'Shravani' @'localhost' identified by 'Shauv@20';
grant all on my_db.*to 'Shravani'@'localhost';
create table Student2(PRN VARCHAR(20),NAME VARCHAR(20),middlename VARCHAR(20), Surname VARCHAR(20),address VARCHAR(30),mobilenum VARCHAR(20),emailid VARCHAR(50),DOB date);
