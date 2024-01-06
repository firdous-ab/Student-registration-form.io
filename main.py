import datetime
import os

from flask import Flask
from flask import request, redirect, render_template, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import CSRFProtect
# from werkzeug.urls import url_encode
import pymysql
from flaskext.mysql import MySQL
from modules import StudentDatabase
from forms import StudentInputForm

app = Flask(__name__)
Bootstrap(app)
csrf = CSRFProtect(app)
csrf.init_app(app)
mysql = MySQL()
app.config["MYSQL_DATABASE_USER"] = "root"
app.config["MYSQL_DATABASE_PASSWORD"] = "Damilola2004."
app.config["MYSQL_DATABASE_DB"] = "students"
app.config["MYSQL_DATABASE_HOST"] = "localhost"
app.config['SECRET_KEY'] = 'Firdous'
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg'}
mysql.init_app(app)
students = StudentDatabase()


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/add/student', methods=['GET', 'POST'])
def addStudents():
    connection = mysql.connect()
    cursor = connection.cursor(pymysql.cursors.DictCursor)
    form = StudentInputForm()
    print(form)
    if request.method == "POST":
        print("form is valid")
        first_name = request.form.get('first_name')
        middle_name = request.form.get('middle_name')
        last_name = request.form.get('last_name')
        gender = request.form.get('gender')
        date_of_birth = request.form.get('date_of_birth')
        date_of_birth = datetime.datetime.strptime(date_of_birth, '%d-%m-%Y').date() if date_of_birth else None
        matric_no = request.form.get('matric_no')
        email = request.form.get('email')
        phone_number = request.form.get('phone_number')
        college = request.form.get('college')
        department = request.form.get('department')
        level = request.form.get('level')
        if 'photo' in request.files:
            photo = request.files['photo']

            if photo and allowed_file(photo.filename):
                # Save the photo to the upload folder
                photo_path = os.path.join(app.config['UPLOAD_FOLDER'], photo.filename)

            else:
                # Handle the case where no valid photo is uploaded
                photo_path = None
        else:
            # Handle the case where 'photo' is not in request.files
            photo_path = None
        # Handle the cas
        address = request.form.get('address')
        state_of_origin = request.form.get('state_of_origin')
        local_government = request.form.get('local_government')
        guardian_name = request.form.get('guardian_name')
        guardian_number = request.form.get('guardian_number')
        guardian_address = request.form.get('guardian_address')
        print(form.data)
        print("form submitted")
        students.addStudent( first_name=first_name, middle_name=middle_name, last_name=last_name, gender=gender,
                            date_of_birth=date_of_birth,
                            matric_no=matric_no, email=email, phone_number=phone_number, college=college,
                            department=department, level=level, photo=photo_path, address=address,
                            state_of_origin=state_of_origin, local_government=local_government,
                            guardian_name=guardian_name, guardian_number=guardian_number,
                            guardian_address=guardian_address)
        print('form added')
        cursor.close()

        flash('Successfully Registered', 'success')
        # Redirect to the submission_result.html with the submitted data
        return redirect(url_for('submission_result', **request.form))

    return render_template('add_student.html', title='Add', form=form)


@app.route('/submission_result', methods=['GET'])
def submission_result():
    return render_template('submission_result.html')


if __name__ == "__main__":
    print("App is running")
    app.run(debug=True)

