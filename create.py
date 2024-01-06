# this is to create the database automatically in mysql workbench
import mysql.connector

mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Damilola2004.",
            database="students",
            auth_plugin="mysql_native_password"
        )
my_cursor = mydb.cursor()


# my_cursor.execute('CREATE DATABASE students')
my_cursor.execute("CREATE TABLE students(id INT NOT NULL PRIMARY KEY AUTO_INCREMENT, first_name varchar(255) NOT NULL,middle_name varchar(255) NOT NULL, last_name varchar(255) NOT NULL,gender varchar(255),"
                  "date_of_birth DATE NOT NULL, matric_no varchar(255),email varchar(255),phone_number BIGINT, college varchar(255), department varchar(255), "
                  "level BIGINT,photo BLOB,address varchar(255),state_of_origin varchar(255),local_government varchar(255),"
                  " guardian_name varchar(255),guardian_number BIGINT,guardian_address varchar(255))")