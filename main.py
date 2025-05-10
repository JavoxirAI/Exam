from auth import register, login
from student import buy_course, show_my_courses, send_message
from teacher import add_course, show_clients, change_price, incoming_messages
from utils import logout


def teacher_menu():
    print("""
    1. Add course
    2. Show_clients
    3. Change course price
    4. Incoming messages
    5. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        add_course()
    elif choice == "2":
        show_clients()
        print("salom")
    elif choice == "3":
        change_price()
    elif choice == "4":
        incoming_messages()
    elif choice == "5":
        logout()
        return "Good bye"
    else:
        print("Invalide choice")
    teacher_menu()


def student_menu():
    print("""
        1. Buy course
        2. Show all my course
        3. Send message teacher
        4. Exit
        """)
    choice = input("Enter your choice: ")
    if choice == "1":
        buy_course()
    elif choice == "2":
        show_my_courses()
    elif choice == "3":
        send_message()
    elif choice == "4":
        logout()
        return "Good bye"
    else:
        print("Invalide choice")
    student_menu()

def main():
    print("""
    1. Login
    2. Regstration
    3. Exit
    """)
    choice = input("Enter your choice: ")
    if choice == "1":
        result = login()
        if result == "teacher":
            teacher_menu()
        elif result == "student":
            student_menu()
    elif choice == "2":
        register()
    elif choice == "3":
        return "Good bye 👋🏻"
    else:
        print("Invalide choice")
    main()

if __name__ == "__main__":
    logout()
    main()