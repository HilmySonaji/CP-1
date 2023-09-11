import pyinputplus as pyip
from tabulate import tabulate as tbl

DB_Siswa = "data.csv"
Nilai = 0

#Function to Count Hasil
def hasilakhir():
    global Nilai
    if Nilai >= 210:
        hasil = "Lulus"
        return hasil
    else:
        hasil = "Tidak Lulus"
        return hasil 

def show(database, title="\nData Nilai Ujian Siswa\n"):
    # Show the title
    print(title)
    
    # Setup header and data
    data = list(database.values())[1:]
    header = database['column']

    # Print data to user screen
    print(tbl(data, header, tablefmt="mixed_grid"))

#Add Function
def add(database):
    global Nilai

    show(database)
 
    #Input Option
    NISN = pyip.inputInt("Input NISN: ") 
    Nama = input("Input Nama Siswa: ").capitalize()
    Sex = pyip.inputChoice(["M","F"],prompt="Input Jenis Kelamin (M/F): ")
    Kelas = input("Input Kelas Siswa: ").upper()
    Matematika,Indonesia,Inggris = input("Input Nilai Mapel MTK, B.Indonesia, B.Inggris: ").strip().split()
    Nilai = int(Matematika) + int(Indonesia) + int(Inggris)
    Hasil = hasilakhir()

    database.update({f"{Nama}": [len(database)-1,NISN, Nama, Sex, Kelas, Matematika, Indonesia, Inggris, Nilai, Hasil]})
    return database

#Update Function
#def update():

#Delete Function
def delete(database):
    """A function to remove fruit from the database

    Args:
        database (dict): Fruit database

    Returns:
        dict: Latest database
    """
    # Show the data
    show(database)

    # Input the index of fruit to be deleted
    id = pyip.inputInt(prompt="Masukan Index Siswa: ", lessThan=len(database)-1)

    # Iterations of fruit in the database
    for key, value in database.copy().items():
        # If header then continue
        if key == "column":
            continue
        # If fruit is available, remove by index
        if id in value:
            del database[key]
        # In addition, update the index of the remaining fruit
        elif id < value[0]: 
            value[0] -= 1
            database.update({f"{key}": value})
    # Show the data
    show(database)
    return database