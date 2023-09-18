import csv
import os
import pyinputplus as pyip
from tabulate import tabulate as tbl
from Operasi import crud as df

#Var
NISN = 0

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

#Find NISN Function
def find_NISN(database):
    global NISN
    clear_screen()
    df.show(database)
    NISN = pyip.inputInt(prompt='Masukan Nomor Siswa yang dicari: ')
    NISN = NISN
    clear_screen()
    if NISN in database:
        print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
    else:
        False   

#Find Kelas Function
def find_Kelas(database):
    datacustom = list(database.values())[1:]
    data0 = []
    clear_screen()
    df.show(database)
    Kelas = pyip.inputChoice(["12A","12B","12C"],prompt="Input Kelas Siswa (12A/12B/12C): ").upper()
    clear_screen()
    for value in datacustom:
        if Kelas in value[3]:
            data0.append(value)
    if data0:
        print(tbl(data0, database['column'], tablefmt='mixed_grid'), '\n')
    else:
        print("data not found")

#Find Hasil Function
def find_Hasil(database):
    data0 = []
    datacustom = list(database.values())[1:]
    clear_screen()
    df.show(database)
    hinput = int(pyip.inputChoice(["1","2"],prompt="""1. Lulus 
2. Tidak Lulus
Pilihan:  """))
    if hinput == 1:
        Hasil = "Lulus"
    else:
        Hasil = "Tidak Lulus"
    clear_screen()
    for value in datacustom:
        if Hasil == value[8]:
            data0.append(value)
    if data0:
        print(tbl(data0, database['column'], tablefmt='mixed_grid'), '\n')
    else:
        print("data not found")

#Update Combination For Selected
def upcom(database):
    while True:
        clear_screen()
        print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'))
        pilih = int(pyip.inputChoice(["1","2","3"],prompt="""
1. Edit Value
2. Edit Row
3. Back
Pilihan : """))
        if pilih == 1: upcolfun(database)
        elif pilih  == 2: updateselectedRowNISN(database)
        else :
            break

#Update Combination For Non Selected
def upcomfornon(database):
    global NISN
    clear_screen()
    df.show(database)
    NISN = pyip.inputInt(prompt='Masukan Nomor Siswa yang ingin diubah: ')
    if NISN in database:
        while True:
            clear_screen()
            print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'))
            pilih = int(pyip.inputChoice(["1","2","3"],prompt="""
1. Edit Value
2. Edit Row
3. Back
Pilihan : """))
            if pilih == 1: upcolfun(database)
            elif pilih  == 2: updateselectedRowNISN(database)
            else :
                break
    else : print("NISN Tidak Terdaftar!!!")

#Update Row Selected Function
def updateselectedRowNISN(database): #selected row
    global NISN
    NISN = NISN
    clear_screen()
    if NISN in database:
        print(tbl([database[NISN]], database["column"], tablefmt='mixed_grid'))
        continue_update = pyip.inputYesNo(prompt='Apakah anda ingin mengubah data ini (yes/no)?: ')
        if continue_update == 'yes':
                Nama = pyip.inputStr("Input Nama Siswa: ").title()
                Sex = pyip.inputChoice(["M","F"],prompt="Input Jenis Kelamin (M/F): ")
                Kelas = pyip.inputChoice(["12A","12B","12C"],prompt="Input Kelas Siswa (12A/12B/12C): ")
                Matematika = pyip.inputNum("Input Nilai Mapel Matematika: ")
                Indonesia = pyip.inputNum("Input Nilai Mapel Bahasa Indonesia: ")
                Inggris = pyip.inputNum("Input Nilai Mapel Bahasa Inggris: ")
                Nilai = Matematika + Indonesia + Inggris
                if Nilai >= 210: Hasilx = "Lulus"
                else: Hasilx = "Tidak Lulus"
                Hasil = Hasilx
        else: return database
        confirm = pyip.inputYesNo(prompt='Apakah anda ingin menyimpan data ini (yes/no)?: ')
        if confirm == 'yes':
            database[NISN] = [NISN, Nama, Sex, Kelas, Matematika,Indonesia, Inggris, Nilai, Hasil]
            print('Data Berhasil diubah')
    else : print('Nomor Siswa tidak ada!')
    clear_screen()
    print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
    return database

#Update Column Function For Selected
def upcolfun(database):
    global NISN
    old={}
    new={}
    clear_screen()
    df.show(database)
    NISN = NISN
    clear_screen()
    print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'))
    while True:
        upin = int(pyip.inputChoice(["1","2","3","4","5"],prompt="""
1. Nama
2. Sex
3. Kelas
4. Mapel
5. Back
Pilihan : """))
        clear_screen()
        if upin == 1: x = "Nama"
        if upin == 2: x = "Sex"
        if upin == 3: x = "Kelas"
        if upin == 4: x = mapelsum(database,NISN)
        if upin == 5: break
        if upin != 4 :
            for key,val in list(database.items()):
                if key == "column":
                    old.update({"column":val})
                    new.update({"column":val})
                    continue
                if key == NISN:
                    old.update({key:val})
                    print(tbl(list(old.values())[1:],old["column"],tablefmt="mixed_grid"))
                    colin = pyip.inputStr(prompt=f"Input Value baru untuk {x}: ",applyFunc = lambda x: x.title(),default = "N/A",limit = 1)
                    val[upin] = colin
                    new.update({key:val})
                    clear_screen()
                    print(tbl(list(new.values())[1:],new["column"],tablefmt="mixed_grid"))

#Delete Selected Function
def deleteselectedNISN(database):
    global NISN
    NISN = NISN
    clear_screen()
    if NISN in database:
        print(tbl([database[NISN]], database["column"], tablefmt='mixed_grid'))
        continue_update = pyip.inputYesNo(prompt='Apakah anda ingin menghapus data ini (yes/no)?: ')
        if continue_update == 'yes':
            for key, value in database.copy().items():
                if key == "column":
                    continue
                if NISN in value:
                    del database[key]
    clear_screen()
    print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
    return database  

#Mapel Sum Function For Selected
def mapelsum(database,NISN):
    NISN = NISN
    clear_screen()
    print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
    inmap = int(pyip.inputChoice(["1","2","3","4","5"],prompt="""Pilih Mapel Yang Ingin Di Rubah:
1. Matematika
2. Indonesia
3. Inggris
4. All
5. Back
Pilihan: """))
    for key,val in list(database.items()):
        if inmap == 1:
            if key == NISN:
                clear_screen()
                print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
                Matematika = pyip.inputNum("Input Nilai Mapel Matematika: ")
                val[4] = Matematika
                val[7] = val[4] + val [5] + val[6]
                if val[7] >= 210:
                    val[8] = "Lulus"   
                else:
                    val[8] = "Tidak Lulus"
        if inmap == 2:
            if key == NISN:
                clear_screen()
                print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
                Indonesia = pyip.inputNum("Input Nilai Mapel Bahasa Indonesia: ")
                val[5] = Indonesia
                val[7] = val[4] + val [5] + val[6]
                if val[7] >= 210:
                    val[8] = "Lulus"   
                else:
                    val[8] = "Tidak Lulus"
        if inmap == 3:
            if key == NISN:
                clear_screen()
                print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
                Inggris = pyip.inputNum("Input Nilai Mapel Bahasa Inggris: ")
                val[6] = Inggris
                val[7] = val[4] + val [5] + val[6]
                if val[7] >= 210:
                    val[8] = "Lulus"   
                else:
                    val[8] = "Tidak Lulus"
        if inmap == 4:
            if key == NISN:
                clear_screen()
                print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')
                Matematika = pyip.inputNum("Input Nilai Mapel Matematika: ")
                Indonesia = pyip.inputNum("Input Nilai Mapel Bahasa Indonesia: ")
                Inggris = pyip.inputNum("Input Nilai Mapel Bahasa Inggris: ")
                val[4],val[5],val[6] = Matematika,Indonesia,Inggris
                val[7] = val[4] + val [5] + val[6]
                if val[7] >= 210:
                    val[8] = "Lulus"   
                else:
                    val[8] = "Tidak Lulus"
    print(tbl([database[NISN]], database['column'], tablefmt='mixed_grid'), '\n')

#Guest Login Function
def guest(database):
    while True:
        clear_screen()
        df.show(database)
        fitur = int(pyip.inputChoice(["1","2","3","4"],prompt="""\tMasukan Opsi yang anda inginkan: 
1. Find NISN
2. Find Kelas
3. Find Siswa Lulus / Tidak Lulus
4. Back
Pilihan: """))
        clear_screen()
        match fitur:
            case 1: find_NISN(database)
            case 2: find_Kelas(database)
            case 3: find_Hasil(database)
            case 4: break

        while fitur == 1:
            fitur1 = int(pyip.inputChoice(["1","2"],prompt="""\tMasukan Opsi yang anda inginkan:
1. Cari NISN Lain
2. Back                                      
Pilihan: """))
            match fitur1:
                case 1: find_NISN(database)
                case 2: break

        while fitur == 2:
            fitur1 = int(pyip.inputChoice(["1","2"],prompt="""\tMasukan Opsi yang anda inginkan:
1. Lihat Kelas Lain
2. Back                                      
Pilihan: """))
            match fitur1:
                case 1: find_Kelas(database)
                case 2: break
        while fitur  == 3:
            fitur1 = int(pyip.inputChoice(["1","2"],prompt="""\tMasukan Opsi yang anda inginkan:
1. Input Hasil lain
2. Back                                      
Pilihan: """))
            match fitur1:
                case 1: find_Hasil(database)
                case 2: break

#Admin Login Function
def admin(database):
    while login() == True:
        clear_screen()
        while True:
            clear_screen()
            df.show(database)
            fitur = int(pyip.inputChoice(["1","2","3"],prompt="""1. Adv View
2. Edit
3. Exit
Pilih Salah Satu Opsi: """))
            if fitur == 3:
                break
            while fitur == 1:
                clear_screen()
                df.show(database)
                fitur2 = int(pyip.inputChoice(["1","2","3","4"],prompt="""\tMasukan Opsi yang anda inginkan:
1. Find NISN
2. Find Kelas
3. Find Hasil
4. Back
Pilihan: """))
                match fitur2:
                    case 1: find_NISN(database)
                    case 2: find_Kelas(database)
                    case 3: find_Hasil(database)
                    case 4: break
                while fitur2 == 1:
                    fitur3 = int(pyip.inputChoice(["1","2","3","4"],prompt="""\tMasukan Opsi yang anda inginkan:
1. Find NISN Lain
2. Edit Selected
3. Delete Selected
4. Back                                      
Pilihan: """))
                    match fitur3:
                        case 1: find_NISN(database)
                        case 2: upcom(database)
                        case 3: deleteselectedNISN(database)
                        case 4: break

                    # Keep database up to date
                    with open("data/data.csv", 'w', encoding="utf-8", newline="") as file:
                        # Create a writer object
                        writer = csv.writer(file, delimiter=";")
                        # Write the data to csv file
                        writer.writerows(database.values())
                while fitur2 == 2:
                    fitur3 = int(pyip.inputChoice(["1","2"],prompt="""\tMasukan Opsi yang anda inginkan:
1. Find Kelas Lain
2. Back                             
Pilihan: """))
                    match fitur3:
                        case 1: find_Kelas(database)
                        case 2: break
                    
                    # Keep database up to date
                    with open("data/data.csv", 'w', encoding="utf-8", newline="") as file:
                        # Create a writer object
                        writer = csv.writer(file, delimiter=";")
                        # Write the data to csv file
                        writer.writerows(database.values())
                while fitur2  == 3:
                    fitur3 = int(pyip.inputChoice(["1","2"],prompt="""\tMasukan Opsi yang anda inginkan:
1. Input Hasil lain
2. Back                                      
Pilihan: """))
                    match fitur3:
                        case 1: find_Hasil(database)
                        case 2: break
            while fitur == 2:
                clear_screen()
                df.show(database)
                fitur1 = int(pyip.inputChoice(["1","2","3","4"],prompt="""1. Add
2. Edit
3. Delete
4. Back
Pilih Salah Satu Opsi: """))
                match fitur1:
                    case 1: df.add(database)
                    case 2: upcomfornon(database)
                    case 3: df.delete(database)
                    case 4: break
                    # Keep database up to date
                with open("data/data.csv", 'w', encoding="utf-8", newline="") as file:
                    # Create a writer object
                    writer = csv.writer(file, delimiter=";")
                    # Write the data to csv file
                    writer.writerows(database.values())