import csv
from tabulate import tabulate as tbl

def read():
    with open("data/temp.csv", 'r') as file:
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
db = read()
def show(database, title="\t\t\t\t\tData Nilai Ujian Siswa\n"):
    # Show the title
    print(title)
    # Setup header and data
    data = list(database.values())[1:]
    header = database['column']
    # Print data to user screen
    print(tbl(data, header, tablefmt="mixed_grid"))

show(db)