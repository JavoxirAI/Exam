from file_manager import read, write
from datetime import datetime
from utils import generate_id
import random
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from time import sleep

def login():

    # Email tekshirish
    email = input("Enter your email: ").strip().lower()
    if '@' not in email:
        print("Noto‘g‘ri email manzil")
        return

    password = input("Enter your password: ").strip()

    users = read("users.csv")
    for index, user in enumerate(users):
        if user[1] == email and user[3] == password:
            users[index][-1] = "online"
            write(filename="users.csv", data=users, mode="w")
            print(f"Welcome {user[2]}")
            return user[4]

    return print("Email yoki parol noto‘g‘ri")


#----------->     Register      <--------

def send_email(receiver_email, body):
    sender_email = "abdukarimjonovjavohir1@gmail.com"
    password = "pqur zlcj ctgu mzos"

    subject = "Test Email"

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()
            server.login(sender_email, password)
            text = msg.as_string()
            server.sendmail(sender_email, receiver_email, text)
            print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def register():
    print("\nRo'yxatdan o'tish:")

    # Email tekshirish
    email = input("Enter your email: ").strip().lower()

    users = read("users.csv")
    for row in users[1:]:
        if row[1].strip().lower() == email:
            print("Bu email allaqachon ro'yxatdan o'tgan")
            return

    message = str(random.randint(1000, 9999))
    threading.Thread(target=send_email, args=(email, message)).start()
    print("Message is sent")
    sleep(6)
    confirm_meassage = input("confir text: ")

    while confirm_meassage != message:
        print("Invalide message !!!")
        confirm_meassage = input("confir text: ")

    print("Email tasdiqlandi")

    # Username va parollar
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()
    password2 = input("Confirm your password: ").strip()

    while password2 != password:
        print("Your pasword eror !!!")
        password = input("Enter your password: ").strip()
        password2 = input("Confirm your password: ").strip()

    # Rol tanlash
    role = input("Enter your role (teacher/student): ").strip().lower()
    while role not in ["teacher", "student"]:
        role = input("Bunday role mavjud emas !!!").strip().lower()

    # ID va vaqt
    new_id = generate_id("users.csv")
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "offline"

    # Faylga yozish
    data = [new_id, email, username, password, role, created_at, status]
    write("users.csv", data, 'a')

    return print("Ro'yxatdan o'tish muvaffaqiyatli yakunlandi!")
