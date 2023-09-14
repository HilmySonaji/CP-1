import csv
import os
import pyinputplus as pyip

#Login Function
def login():
    User = input("Masukan User: ")
    Password = input("Masukan Password: ")
    with open("data/user.csv",mode="r") as file:
        reader = csv.reader(file, delimiter=";")
        for row in reader:
            if row == [User,Password]:
                return True
            else:
                print("Wrong Password!!!")
    return False

#Clear Function
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')