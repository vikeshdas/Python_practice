"""
SQL lite

- SQLite does not require a separate server process or external dependencies to function

- No installation or configuration is needed—just link the library to your application.

-he database runs inside your application, not as a separate service.

-There is no client-server architecture unlike MySQL

-The database is stored as a single file (.db or .sqlite) on disk, making it easy to bundle with an app.

-Unlike traditional databases (e.g., MySQL, SQL Server), SQLite does not require a database server.

"""

import sqlite3


connection=sqlite3.connect('my_database.db')

cursor=connection.cursor()

# sql="""
# create table employee(id integer,name varchar(64),department varchar(64),phone varchar(64),email varchar(64))
# """

# sql="""
# insert into employee (id,name,department,phone,email) values(1,"vikesh","IT","8076110599","vk@gmail.com");
# insert into employee values(2,"rahul","IT","8510996944","rk@gmail.com");
# """



# sql="""
# select * from employee
# """
# sql="""
# select * from employee where name like "v%"
# """
# cursor.execute(sql)
# connection.commit()

# for row in cursor:
#     print(row)
# connection.close()



sql="""
update employee set name="VIKESH" where id=1
"""
cursor.execute(sql)
connection.commit()

connection.close()