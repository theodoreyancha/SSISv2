import mysql.connector
from prettytable import from_db_cursor

db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="paradox1412",
    database="student_database"
)
mycursor = db.cursor()

def add_student():
    print("Add Student ID")
    while True:
        ID = input()
        query = f"SELECT * FROM `yancha` WHERE `Student ID` = '{ID}'"
        mycursor.execute(query)
        row2 = mycursor.fetchone()
        if row2 != None:
            print("Student ID has already exists")
            print("Input new Student ID: ")
        else:
            break
    print("Add Name")
    name = input()
    print("Add Year Level")
    yrlevel = input()
    print("Add Gender")
    gender = input()
    print("Add Course")
    while True:
        course = input()
        query_new = f"SELECT * FROM `course` WHERE `Course Code` = '{course}'"
        mycursor.execute(query_new)
        row2 = mycursor.fetchone()
        if row2 != None:
            break
        else:
            print("Course Code not Found")
            print("Input Course (BSCA, BSIT, BSCS, BSIS): ")

    mycursor.execute("INSERT INTO `yancha` (`Student ID`, `Name`, `Year Level`, `Gender`, `Course`) "
                     "VALUES (%s,%s,%s,%s,%s)",
                     (ID, name, yrlevel, gender, course))
    db.commit()
    input("Press any key to return to main menu")
def view_student():
    mycursor.execute("SELECT * from `yancha`")
    table = from_db_cursor(mycursor)
    print(table)
    input("Press any key to return to main menu")

def search_student():
    user = input("Please put student ID")
    query = f"SELECT * FROM `yancha` WHERE `Student ID` = '{user}'"
    mycursor.execute(query)

    row = mycursor.fetchone()

    if row != None:
        print(row)
        input("Press any key to return to main menu")
    else:
        print("Student ID not Found")
        input("Press any key to return main menu")

def update_student():
    user = input("Please put student ID\n")
    query = f"SELECT * FROM `yancha` WHERE `Student ID` = '{user}'"
    mycursor.execute(query)

    row = mycursor.fetchone()

    if row != None:
        print(row)
        print("What would change like to happen?\n"
        "1. Change Student ID\n"
        "2. Change Name\n"
        "3. Change Year Level\n"
        "4. Change Gender\n"
        "5. Change Course")
        change = input()
        if change == "1":
            print("Enter new Student ID")
            change_id = input()
            query_new = f"UPDATE `yancha` SET `Student ID` = '{change_id}' WHERE `Student ID` = '{user}'"
            mycursor.execute(query_new)
            db.commit()
        if change == "2":
            print("Enter new Name")
            change_name = input()
            query_new = f"UPDATE `yancha` SET `Name` = '{change_name}' WHERE `Student ID` = '{user}'"
            mycursor.execute(query_new)
            db.commit()
        if change == "3":
            print("Enter new Year Level")
            change_yrlvl = input()
            query_new = f"UPDATE `yancha` SET `Year Level` = '{change_yrlvl}' WHERE `Student ID` = '{user}'"
            mycursor.execute(query_new)
            db.commit()
        if change == "4":
            print("Enter new Gender")
            change_gender = input()
            query_new = f"UPDATE `yancha` SET `Gender` = '{change_gender}' WHERE `Student ID` = '{user}'"
            mycursor.execute(query_new)
            db.commit()
        if change == "5":
            print("Enter new Course")
            change_course = input()
            query_new = f"UPDATE `yancha` SET `Course` = '{change_course}' WHERE `Student ID` = '{user}'"
            mycursor.execute(query_new)
            db.commit()


    else:
        print("Student ID not Found")
        input("Press any key to return main menu")

def delete_student():
    user = input("Please put student ID")
    query = f"SELECT * FROM `yancha` WHERE `Student ID` = '{user}'"
    mycursor.execute(query)

    row = mycursor.fetchone()

    if row != None:
        query_new = f"DELETE FROM `yancha` WHERE `Student ID` = '{user}'"
        mycursor.execute(query_new)
        db.commit()
        print("Deleted Successfully")
        input("Press any key to return main menu")
    else:
        print("Student ID not Found")
        input("Press any key to return main menu")

def view_course():
    mycursor.execute("SELECT * from `Course`")
    table = from_db_cursor(mycursor)
    print(table)
    input("Press any key to return main menu")

def add_course():
    print("Add Course code")
    course_code = input()
    print("Add Course name")
    course_name = input()
    mycursor.execute("INSERT INTO `course` (`Course Code`, `Course`) "
                     "VALUES (%s,%s)",
                     (course_code, course_name))
    db.commit()
    input("Press any key to return main menu")

def update_course():
    user = input("Please put Course code\n")
    query = f"SELECT * FROM `course` WHERE `Course Code` = '{user}'"
    mycursor.execute(query)

    row = mycursor.fetchone()

    if row != None:
        print(row)
        print("What would change like to happen?")
        print("1. Change Course code")
        print("2. Change Course name")
        change = input()
        if change == "1":
            print("Enter new Course Code")
            change_ccode = input()
            query_new = f"UPDATE `course` SET `Course Code` = '{change_ccode}' WHERE `Course Code` = '{user}'"
            mycursor.execute(query_new)
            db.commit()

        if change == "2":
            print("Enter new Course Name")
            change_cname = input()
            query_new = f"UPDATE `course` SET `Course` = '{change_cname}' WHERE `Course Code` = '{user}'"
            mycursor.execute(query_new)
            db.commit()

    input("Press any key to return main menu")

def delete_course():
    user = input("Please put student ID")
    query = f"SELECT * FROM `course` WHERE `Course Code` = '{user}'"
    mycursor.execute(query)

    row = mycursor.fetchone()

    if row != None:
        query_new = f"DELETE FROM `course` WHERE `Course Code` = '{user}'"
        mycursor.execute(query_new)
        db.commit()
        print("Deleted Successfully")
        input("Press any key to return main menu")
    else:
        print("Course code not Found")
        input("Press any key to return main menu")

while True:
    print("--------------------------------------")
    print(" Welcome to Student Management System v2.0")
    print("---------------------------------------")
    print("Press the number correspond to the action\n"
        "1. Add New Student\n"
        "2. View Students\n"
        "3. Search Student\n"
        "4. Update Student\n"
        "5. Delete Student\n"
        "6. View Course/s\n"
        "7. Add Course/s\n"
        "8. Update Course/s\n"
        "9. Delete Course/s\n"
        "0. Quit")

    value = input()
    if value == "1":
        add_student()
    elif value == "2":
        view_student()
    elif value == "3":
        search_student()
    elif value == "4":
        update_student()
    elif value == "5":
        delete_student()
    elif value == "6":
        view_course()
    elif value == "7":
        add_course()
    elif value == "8":
        update_course()
    elif value == "9":
        delete_course()
    else:
        break

print("-------------------------------")
print(" Thank you for using our system")
print("-------------------------------")