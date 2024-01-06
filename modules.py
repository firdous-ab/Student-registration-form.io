# from flask import
from mysql.connector import MySQLConnection, Error
import mysql.connector
import pymysql


class StudentDatabase():

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Damilola2004.",
            database="students",
            auth_plugin="mysql_native_password"
        )
        self.my_cursor = self.mydb.cursor()

        self.my_cursor.execute('USE students')

    def addStudent(self, first_name, middle_name, last_name,
                   gender, date_of_birth, matric_no, email, phone_number,
                   college, department, level, photo, address,
                   state_of_origin, local_government, guardian_name,
                   guardian_number, guardian_address):
        sql = "INSERT INTO students(first_name,middle_name,last_name,\
                   gender,date_of_birth,matric_no,email,phone_number,\
                   college,department,level,photo,address,\
                   state_of_origin,local_government,guardian_name,\
                   guardian_number,guardian_address) VALUES (%s,%s,%s,%s,%s,%s,\
                   %s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        val = (first_name, middle_name, last_name,
               gender, date_of_birth, matric_no, email, phone_number,
               college, department, level, photo, address,
               state_of_origin, local_government, guardian_name,
               guardian_number, guardian_address)
        self.my_cursor.execute(sql, val)
        self.mydb.commit()
