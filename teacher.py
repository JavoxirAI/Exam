from file_manager import write, read
from utils import generate_id, get_active_user
import ast


def add_course():
    course_name = input("Enter course name: ")
    balance = float(input("Enter course price: "))
    new_id = generate_id("course.csv")
    students_str = list()
    user = get_active_user()

    data = [new_id, user[1], course_name, students_str, balance]
    write("course.csv", data, "a")

    print("Kurs qo'shildi.")


def show_clients():
    course_data = read("course.csv")
    user = get_active_user()[1]

    students = list()
    for row in course_data[1:]:
        if user == row[1]:
            student_list = ast.literal_eval(row[3])
            for iteam in student_list:
                students.append(iteam)

    print(students)


def change_price():
    course_data = read("course.csv")
    user = get_active_user()[1]
    for row in course_data[1:]:
        if user == row[1]:
            new_price = float(input("New course price: "))
            row[4] = new_price

    write("course.csv",course_data,"w")

    print("Kurs ma'lumotlari o'zgartirildi")


def incoming_messages():
    teacher = get_active_user()
    teacher_email = teacher[1]

    messages = read("messages.csv")

    if not messages:
        print("Xabarlar mavjud emas.")
        return

    inbox = []
    for row in messages[1:]:
        if len(row) > 1 and row[1] == teacher_email:
            inbox.append(row)

    if inbox:
        print("Sizga studentlardan yuborilgan xabarlar:")
        for msg in inbox:
            print(f"Kimdan: {msg[0]}\nXabar: {msg[2]}\nVaqt: {msg[3]}\n")
    else:
        print("Sizga hech qanday xabar yuborilmagan.")

