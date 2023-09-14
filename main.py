#Import Module
import os
import csv
import sys
from CRUD import Database_Func as df
from Operasi import operator_function as opfu
import pyinputplus as pyip

def initialize_db():
    with open(PATH, 'r',newline="") as file:
        # Read the data from csv file
        reader = csv.reader(file, delimiter=";")
        # Create dictionary from csv
        header = next(reader)
        database = {"column": header}
        # Input row into dictionary
        for row in reader:
            NISN, Nama, Sex, Kelas, Matematika, Indonesia, Inggris, Nilai, Hasil = row
            database.update({int(NISN): [int(NISN), Nama, Sex, Kelas, int(Matematika), int(Indonesia), int(Inggris), int(Nilai), Hasil]})
    return database

#Domain
if __name__ == "__main__":
    # Setting the path of database file
    if getattr(sys, 'frozen', False):
        PATH = sys._MEIPASS
        PATH = os.path.join(PATH, 'data/data.csv') 
    else:
        PATH = os.getcwd()
        PATH = os.path.join(PATH, 'data/data.csv')

    db = initialize_db()

    while True:
        Login = pyip.inputChoice(["Admin","Guest"],prompt="""\n\tIngit Melihat Data Sebagai Siapa?\n
- Admin
- Guest

Pilihan: """).upper()
        opfu.clear_screen()
        if Login == "ADMIN":
            while opfu.login() == True:
                opfu.clear_screen()
                while True:
                    df.show(db)
                    inp = int(input("""1. Add
2. Update
3. Delete
4. Exit
Pilih Salah Satu Opsi: """))
                    opfu.clear_screen()
                    match inp:
                        case 1: df.add(db)
                        case 2: df.update(db)
                        case 3: df.delete(db)
                        case 4: break

                        # Keep database up to date
                    with open(PATH, 'w', encoding="utf-8", newline="") as file:
                        # Create a writer object
                        writer = csv.writer(file, delimiter=";")
                        # Write the data to csv file
                        writer.writerows(db.values())
        else:
            df.show(db)
            break

    