import csv
import os
from file_manager import read, write


def generate_id(file_path):
    if not os.path.exists(file_path):
        return 1

    with open(file_path, mode="r", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        last_id = 0
        for row in reader[1:]:
            if row and row[0].isdigit():
                last_id = max(last_id, int(row[0]))

        return last_id + 1



def logout():
    users = read("users.csv")

    for index in range(len(users))[1:]:
        users[index][-1] = "offline"
    write(filename="users.csv", data=users)


def get_active_user():
    users = read(filename="users.csv")

    for user in users:
        if user[-1] == "online":
            return user