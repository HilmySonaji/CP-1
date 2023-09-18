#Import Module
import os
import csv
import sys
from Operasi import crud as df
from Operasi import operator_function as opfu
import pyinputplus as pyip


def initialize_db():
    """_summary_

    Returns:
        dict: initiating database
    """    
    with open(PATH, 'r') as file:
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
        opfu.clear_screen()
        Login = pyip.inputChoice(["Admin","Guest"],prompt="""\n\tIngit Melihat Data Sebagai Siapa?\n
- Admin
- Guest

Pilihan: """).upper()
        if Login == "ADMIN":
            opfu.admin(db)
        if Login == "GUEST":
            opfu.guest(db)


            


