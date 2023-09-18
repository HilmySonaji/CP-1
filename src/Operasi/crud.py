import pyinputplus as pyip
import csv
from tabulate import tabulate as tbl
from Operasi import operator_function as opfu

#Show Function
def show(database, title="\t\t\t\t\tData Nilai Ujian Siswa\n"):
    """_summary_

    Args:
        database (dict): Showing Database
    Returns:
        Returns a printed table of the database using tabulate module
    """    
    # Show the title
    print(title)
    coldata = database.get("column",[])
    filterdict = {key: value for key, value in database.items() if key != "column"}
    # Sorting
    sortdata = dict(sorted(filterdict.items(), key = lambda item: item[1][0], reverse=False))
    sortdatabase = {"column": coldata,**sortdata}
    # Setup header and data
    data = list(sortdatabase.values())[1:]
    header = sortdatabase['column']
    # Print data to user screen
    print(tbl(data, header, tablefmt="mixed_grid"))

#Add Function
def add(database):
    """_summary_

    Args:
        database (dict): Adding new data to database
    Returns:
        New Data
    """    
    opfu.clear_screen()
    show(database)
    NISN = pyip.inputInt("Input NISN: ")
    if NISN in database:
        print("NISN Sudah Terdaftar")
    else:
        Nama = pyip.inputStr("Input Nama Siswa: ").title()
        Sex = pyip.inputChoice(["M","F"],prompt="Input Jenis Kelamin (M/F): ")
        Kelas = pyip.inputChoice(["12A","12B","12C"],prompt="Input Kelas Siswa (12A/12B/12C): ").upper()
        Matematika = pyip.inputNum("Input Nilai Mapel Matematika: ")
        Indonesia = pyip.inputNum("Input Nilai Mapel Bahasa Indonesia: ")
        Inggris = pyip.inputNum("Input Nilai Mapel Bahasa Inggris: ")
        Nilai = Matematika + Indonesia + Inggris
        if Nilai >= 210: Hasilx = "Lulus"
        else: Hasilx = "Tidak Lulus"
        Hasil = Hasilx
        confirm = pyip.inputYesNo(prompt='Apakah anda ingin menyimpan data ini (yes/no)?: ')
        if confirm == 'yes':
            database[NISN] = [NISN, Nama, Sex, Kelas, Matematika,Indonesia, Inggris, Nilai, Hasil]
            print('Data Berhasil diubah')
    opfu.clear_screen()
    return database

#Update Function
def update(database ): 
    """_summary_

    Args:
        database (dict): updating data that is already available
    Returns:
        updated data
    """    
    opfu.clear_screen()
    show(database)
    NISN = pyip.inputInt(prompt='Masukan Nomor Siswa yang ingin diubah: ')
    opfu.clear_screen()
    if NISN in database:
        print(tbl([database[NISN]], database["column"], tablefmt='mixed_grid'))
        continue_update = pyip.inputYesNo(prompt='Apakah anda ingin mengubah data ini (yes/no)?: ')
        if continue_update == 'yes':
                Nama = pyip.inputStr("Input Nama Siswa: ").title()
                Sex = pyip.inputChoice(["M","F"],prompt="Input Jenis Kelamin (M/F): ")
                Kelas = pyip.inputChoice(["12A","12B","12C"],prompt="Input Kelas Siswa (12A/12B/12C): ").upper()
                Matematika = pyip.inputNum("Input Nilai Mapel Matematika: ")
                Indonesia = pyip.inputNum("Input Nilai Mapel Bahasa Indonesia: ")
                Inggris = pyip.inputNum("Input Nilai Mapel Bahasa Inggris: ")
                Nilai = Matematika + Indonesia + Inggris
                if Nilai >= 210: Hasilx = "Lulus"
                else: Hasilx = "Tidak Lulus"
                Hasil = Hasilx
        else:
            return database
        confirm = pyip.inputYesNo(prompt='Apakah anda ingin menyimpan data ini (yes/no)?: ')
        if confirm == 'yes':
            database[NISN] = [NISN, Nama, Sex, Kelas, Matematika,Indonesia, Inggris, Nilai, Hasil]
            print('Data Berhasil diubah')
    else :
        print('Nomor Siswa tidak ada!')
    opfu.clear_screen()
    print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
    return database

#Delete Function
def delete(database):
    """_summary_

    Args:
        database (dict): deleting data that is already available
    Returns:
        Deleted Data
    """    
    opfu.clear_screen()
    show(database)
    NISN = pyip.inputInt(prompt="Masukan Nomor Siswa: ")
    opfu.clear_screen()
    if NISN in database:
        print(tbl([database[NISN]], database["column"], tablefmt='mixed_grid'))
        continue_update = pyip.inputYesNo(prompt='Apakah anda ingin menghapus data ini (yes/no)?: ')
        if continue_update == 'yes':
            for key, value in database.copy().items():
                if key == "column":
                    continue
                if NISN in value:
                    del database[key]
    else :
        print('Nomor Siswa tidak ada!')
    opfu.clear_screen()
    return database
