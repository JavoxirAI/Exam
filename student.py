from file_manager import read, write
from utils import get_active_user
from datetime import datetime
import ast


def buy_course():
    print("Mavjud kurslar: ")
    courses = read("course.csv")
    user = get_active_user()
    students = []

    for row in courses[1:]:
        print(f"ID:{row[0]}, Course_name:{row[2]}, course_price:{row[4]}")

    id = input("Enter course id: ")
    for row in courses[1:]:
        if row[0] == id and user[1] != row[1]:
            students.append(user[1])
            row[3] = students
            print(f"Siz kursga yozildingiz {user[1]}")
        else:
            print("Id xato yoki siz oldin ro'yxatdan o'tkansiz")

    write("course.csv",courses)



def show_my_courses():
    user = get_active_user()
    courses = read("course.csv")
    users = read("users.csv")

    teacher = {}

    for row in users[1:]:
        if row[4] == 'teacher':
            email = row[1]
            username = row[2]
            teacher[email] = username

    my_courses = []

    for row in courses[1:]:
        student_list = ast.literal_eval(row[3])
        if user[1] in student_list:
            my_courses.append(row)

    if my_courses:
        print("Siz yozilgan kurslar:")
        for course in my_courses:
            teacher_email = course[1]
            teacher_name = teacher.get(teacher_email, "Noma'lum o'qituvchi")
            print(f"ID: {course[0]}, Course name: {course[2]}, Teacher: {teacher_name}, Price: {course[4]}")
    else:
        print("Siz hech qanday kursga yozilmagansiz.")



def send_message():
    student = get_active_user()
    courses = read("course.csv")

    import ast
    teacher_email = None
    for course in courses[1:]:
        student_list = ast.literal_eval(course[3])
        if student[1] in student_list:
            teacher_email = course[1]
            break

    if not teacher_email:
        print("Siz hech bir kursga yozilmagansiz.")
        return

    message = input("O'qituvchiga yuboriladigan xabar: ")
    now = datetime.now().strftime("%Y-%m-%d %H:%M")

    messages = read("messages.csv")
    messages.append([student[1], teacher_email, message, now])
    write("messages.csv", messages)

    print("Xabaringiz yuborildi!")
