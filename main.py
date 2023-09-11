#Import Module
import os
import csv
import sys
from tabulate import tabulate as tbl
from CRUD import Database_Func as df

#Clear Function
def clear_screen():
    """
    A function to clean the user interface
    """
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')

def initialize_db():
    """
    A function to initialize the database 

    Returns:
        dict: Fruit database
    """
    with open(PATH, 'r',newline="") as file:
        # Read the data from csv file
        reader = csv.reader(file, delimiter=";")
        # Create dictionary from csv
        header = next(reader)
        database = {"column": header}
        # Input row into dictionary
        for row in reader:
            No, NISN, Nama, Sex, Kelas, Matematika, Indonesia, Inggris, Nilai, Hasil = row
            database.update({Nama: [int(No), NISN, Nama, Sex, Kelas, Matematika, Indonesia, Inggris, Nilai, Hasil]})

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
        clear_screen()
        df.show(db)
        inp = int(input("""1. Add
2. Update
3. Delete
4. Exit
Pilih Salah Satu Opsi: """))
        match inp:
            case 1: df.add(db)
            case 2: df.Update()
            case 3: df.deleteelete(db)
            case 4: break

            # Keep database up to date
        with open(PATH, 'w', encoding="utf-8", newline="") as file:
            # Create a writer object
            writer = csv.writer(file, delimiter=";")
            # Write the data to csv file
            writer.writerows(db.values())

    