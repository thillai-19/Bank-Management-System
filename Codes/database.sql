create database user_account;
use user_account;
create table Personal_Details(User_Name varchar(25) primary key,User_Password varchar(25),Account_Holder_Name varchar(30),Sex Varchar(11),Father_Name varchar(30),Mother_Name varchar(30),DOB date,AGE int,Aadar_Number varchar(12),Mobile_Number varchar(10),Email_ID varchar(30),Education_Qualification varchar(30),Nationality varchar(30),Parmanent_Address varchar(255),Current_Address varchar(255));
create table Account_Details(User_Name varchar(25) primary key,Account_Holder_Name varchar(30),Account_Number Varchar(30),Bank_Balence varchar(255));
create table Withdrawal_Codes(Codes varchar(18) primary key);
create table User_Changes(User_Name varchar(25) primary key,Changes_parameter varchar(40),Changes varchar(255));
select * from Personal_Details;
select * from Account_Details;
select * from User_Changes;

create database Admins;
use Admins;
create table Admin_Details(Admin_User_Name varchar(25) primary key,Admin_Password varchar(25),Admin_Pass_for_Work Varchar(15),Mobile_Number varchar(10),Security_Question varchar(155),Security_Answer varchar(20));
insert into Admin_details values("Mohan","Mohankumar@72","Mohasmk@321","9790211349","What is Your son's pet name","Lucky");
insert into Admin_details values("karpagavali","karpu@73","thinan@123","9944427996","what Your Favorite laptop Brand","Lenovo");
insert into Admin_details values("Thillai","Thillai@05","Thillai@123", "8220143830","what is Your dad's favorite Food","Biriyani");
insert into Admin_details values("Nanditha","Nandi@07","Nandu@123", "6374421548","what is Your favorite Game","Badminton");
select * from Admin_details;

create database new_user_account;
use new_user_account;
create table New_User_Details(New_User_Name varchar(25) primary key,New_User_Password varchar(25),New_User_Account_Holder_Name varchar(30),New_User_Sex Varchar(11),New_User_Father_Name varchar(30),New_User_Mother_Name varchar(30),New_User_DOB date,New_User_AGE int,New_User_Aadar_Number varchar(12),New_User_Mobile_Number varchar(10),New_User_Email_ID varchar(30),New_User_Education_Qualification varchar(30),New_User_Nationality varchar(30),New_User_Parmanent_Address varchar(255),New_User_Current_Address varchar(255));
select * from New_User_Details;
