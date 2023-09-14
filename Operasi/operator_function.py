import csv
import os
import pyinputplus as pyip
from tabulate import tabulate as tbl
from Operasi import crud as df

#Login Function
def login():
    clear_screen()
    print("\t\tLOGIN\n")
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

#find Function
def find_NISN(database):
    clear_screen()
    df.show(database)
    NISN = pyip.inputInt(prompt='Masukan Nomor Siswa yang dicari: ')
    clear_screen()
    if NISN in database:
        print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
    else:
        print('Data tidak ditemukan!')