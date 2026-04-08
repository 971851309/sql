#对应教材58页第八题
#CREATE TABLE 图书表 ( 书号 nchar(6) primary key, 书名 nvarchar(30) not null, 第一作者 char(10) not null, 出版日期 smalldatetime, 价格 numeric(4,1))
#CREATE TABLE 书店表 ( 书店编号 nchar(6) primary key, 店名 nvarchar(30) not null, 电话 char(8) check (电话 like '[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]'), 地址 varchar(40), 邮政编码 char(6))
#CREATE TABLE 图书销售表 ( 书号 nchar(6) not null, 书店编号 nchar(6) not null, 销售日期 smalldatetime not null, 销售数量 smallint check(销售数量>=1), primary key(书号,书店编号,销售日期), foreign key(书号) references 图书表(书号), foreign key(书店编号) references 书店表(书店编号))
#同页第9题
#ALTER  TABLE 图书表 ADD 印刷数量 INT
#同页第十题
#alter table 图书表 Add 印刷数量 int check( 印刷数量 >= 1000)
#同页第十一题
#alter TABLE 书店表 Drop column 邮政编码#删除列
#同页第十二题，修改列的类型
#alter table 图书销售表 Alter column 销售数量 int





#课本60页第三题
'''
create table Student(

Sno char(7),

Sname  char(10)not null,

Ssex  char(2)  check(Ssex='男'or Ssex='女'),

Sage  tinyint  check(Sage>14AND Sage<46),

Sdept  varchar(20)  default'计算机系',

Sid char(10) unique,-身份证号 
Sdate  date default getdate()

primary  key(Sno)

)

create  table  Course(

Cno char(10) primary key,

Cname  varchar(20)  not null,

Credit  int check (Credit>0),

Semester  tinyint,                                                                                                                                                                                    

)

create  table SC(

Sno char(7),

Cno char(10),

Grade  tinyint  check(Grade>=0AND Grade<=100)

foreign  key(Sno)  references  Student(Sno),

foreign  key(Cno)  references  Course(Cno)

)

 

create   table  Teacher(

Tno char(8) not null,

Tname  char(10)not null,

Salary  decimal(6,2)

)
'''


#(1)为student表添加专业列，列名为spec,类型为char(8)。
#ALTER TABLE student 
#add spec char(8)




#2)为spec列的数据类型改为nchar(8)。
#Alter table student 
#Alter column spec nchar(8)





#(3)为student表的sdept列添加约束，限制该列取值范围为{计算机系，信息管理系，通信工程系}。
#
#alter table student
#add constraint CK_sdept check(sdept='计算机系' or sdept='信息管理系' or sdept='通信工程系')








#4)为SC表的Grade列添加约束，要求此列的取值范围为0~100。
#
#ALTER TABLE SC 
#add constraint CK_Grade check(Grade between 0 and 100)#




#(5)删除student表中新添加的spec列。
#
# ALTER TABLE student   
# DROP COLUMN spec  