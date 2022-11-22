# NAMA : ALOIS
# PROGRAM : JOB CONNECTOR DATA SCIENCE
# INTAKE : OKTOBER 2022
# PENJELASAN PROGRAM
#       PROGRAM INI MERUPAKAN PROGRAM SEDERHANA UNTUK MENGOLAH DATA RENTAL MOBIL 'SEMANTAPNYA', PROGRAM INI DAPAT MELAKUKAN
#   MENGECEK KETERSEDIAAN MOBIL (READ DATA), MENDAFTARKAN MOBIL BARU KE RENTAL (CREATE DATA), MELAKUKAN UPDATE IDENTITAS MOBIL
#   (UPDATE DATA), DAN MELAKUKAN DELETE MOBIL YANG SUDAH TIDAK DIRENTALKAN (DELETE DATA)

# KETERANGAN TAMBAHAN
#   1. DATA AWAL SUDAH DI DEKLARASIKAN DENGAN DICTIONARY 'DATABASE'
#   2. VARIABEL SEMENTARA YANG DIGUNAKAN MEMILIKI AWALAN 'INPUT%' YANG DIGUNAKAN UNTUK MENERIMA MASUKAN INFORMASI
#   3. PROGRAM MASIH MEMILIKI BANYAK KEKURANGAN DAN MASIH PERLU DITINGKATKAN
#   4. PROGRAM INI DIBUAT UNTUK MENYELESAIKAN CAPSTONE PROJECT MODULE 1 MENGENAI PROGRAMMING FUNDAMENTAL

database = {
    1 : ['Toyota', 'Calya', 'B 2624 ABC','Tersedia'],
    2 : ['Daihatsu', 'GrandMax', 'B 1234 CDF','Tidak Tersedia'],
    3 : ['Toyota', 'Almaz', 'B 5234 EFG','Tersedia'] 
}

# HELLO PROGRAM UNTUK MENENTUKAN MENU YANG INGIN DIGUNAKAN
def hello ():
    print('''
        ---------------------------------------
        SILAKAN INPUT MENU YANG INGIN DITUJU
        1. CEK KETERSEDIAAN UNTUK MENYEWA MOBIL
        2. MENDAFTARKAN MOBIL UNTUK DISEWA
        3. MELAKUKAN UPDATE KETERANGAN MOBIL
        4. MELAKUKAN DELETE DATA MOBIL
        5. EXIT MENU
    ''')

# MENU 1 : CEK KETERSEDIAAN MOBIL/READ DATA
def menu1():
    while(True):
        print('''
        ------------------------------------
        Menu yang dapat diakses : 
        1. Mencari status ketersediaan mobil
        2. Mencari spesifikasi mobil
        3. exit menu
        ''')
        input1=int(input('masukkan nomor menu yang ingin digunakan : '))
    # OPSI MENU UNTUK CEK KETERSEDIAAN KESELURUHAN MOBIL
        if(input1==1):
    # JIKA DATA KOSONG, AKAN KEMBALI KE MENU READ DATA
            if len(database)>0:
                print_data()
            else:
                print ('Saat ini mobil tidak teresedia')
    # OPSI MENU UNTUK CEK SPESIFIKASI DETAIL DENGAN INPUT DETAIL MOBIL 
        if(input1==2):
    # JIKA DATA KOSONG, AKAN KEMBALI KE MENU READ DATA
            if(len(database)>0):
                while (True):
                    print('''
        --------------------------------
        Pencarian yang dapat dilakukan : 
        1. Id Mobil
        2. Merk Mobil
        3. Tipe Mobil
        4. Exit Menu
                    ''')
                    input2=int(input('masukan nomor pencarian yang ingin dilakukan : '))
    # MELAKUKAN PENCARIAN DETAIL MOBIL BERDASARKAN INPUT
                    if(input2==1):    
                        input3=int(input('Masukkan Id Mobil : '))
                        print('Id Mobil {} adalah mobil {} tipe {} dengan nomor Polisi {}. saat ini status kendaraan {}'.format(input3,database[input3][0],database[input3][1],database[input3][2],database[input3][3]))
                    
                    if(input2==2):
                        input3=input('Masukkan Merk Mobil : ')
                        for i in database:
                            if input3 == database[i][0]:
                                print ('Merk Mobil {} memiliki nomor id {} dengan tipe {} dan nomor polisi {}. saat ini status kendaraan {}'. format(input3,i,database[i][1],database[i][2],database[i][3])) 

                    if(input2==3):
                        input3=input('Masukkan Nama Mobil 3: ')
                        for i in database:
                            if input3 == database[i][1]:
                                print ('Nama Mobil {} memiliki nomor id {} dengan merk {} dan nomor polisi {}. saat ini status kendaraan {}'. format(input3,i,database[i][0],database[i][2],database[i][3])) 
                    
                    if(input2==4):
                        break
    # KELUAR LOOP KARENA DATA KOSONG/TIDAK ADA
            else:
                print ('Saat ini mobil tidak teresedia')
    # KELUAR DARI MENU READ DATA
        if(input1==3):
            break


# MENU 2 : MENDAFTARKAN/CREATE DATA
def menu2():
    global database
    while(True):
        print('''
        -------------------------------------------
        Menu yang dapat diakses : 
        1. Menambahkan/Mendaftarkan data mobil baru
        2. exit menu
        ''')
        input1=int(input('Masukkan menu yang ingin digunakan : '))
    # MELAKUKAN PENAMBAHAN DATA
        if (input1==1):
            input2=int(input('Masukkan ID mobil yang baru : '))
    # CEK KETERSEDIAAN DATA
            if input2 in database:
                print('ID yang anda masukkan sudah tersedia')
            else:
                input3=input('Masukkan Merk mobil yang ingin di daftarkan : ')
                input4=input('Masukkan Tipe mobil yang ingin di daftarkan : ')
                input5=input('Masukkan Nomor Polisi mobil yang ingin di daftarkan : ')
                print('''data yang ingin ditambahkan adalah 
                    ID = {}
                    Merk  = {}
                    Tipe = {}
                    Nomor Polisi = {}
                '''.format(input2,input3,input4,input5,"Tersedia"))
                input6=input('apakah data sudah benar? (Y/N)')
    # JIKA DATA BENAR, Y AKAN MEMASUKAN INPUT KE DATABASE
                if (input6=='Y'):
                    database[input2]=[input3,input4,input5,"Tersedia"]
                    print ('Data yang ada input sudah tesimpan')

    # KELUAR DARI MENU CREATE DATA
        if (input1==2):
            break
    return database

# MENU 3 : MERUBAH ID DAN KETERANGAN MOBIL/UPDATE DATA
def menu3():
    global database
    if len(database)>0:
        while(True):
            print('''
        --------------------------
        Menu yang dapat diakses : 
        1. update keterangan mobil
        2. exit menu
            ''')
    # MELAKUKAN UPDATE/PERUBAHAN DATA
            input1=int(input('masukkan nomor menu yang ingin digunakan : '))
    # INPUT ID YANG INGIN DIRUBAH
            if input1==1:
                print_data()
                input2=int(input('masukkan id mobil yang ingin diganti : '))
                print ('ID yang anda pilih adalah {}. mobil {} {} dengan nomor polisi {} dan status saat ini adalah {}'.format(input2,database[input2][0],database[input2][1],database[input2][2],database[input2][3]))
                if input2 in database:
                    print('''
        -------------------------------
        Nomor menu yang dapat diakses :
        1. Mengganti Merek Mobil
        2. Mengganti Tipe Mobil
        3. Mengganti No.Polisi
        4. Mengganti Status Mobil
        5. Exit Menu
                    ''')
                    input3=int(input('Masukkan nomor menu yang ingin diakses : '))
        # MENGGANTI MERK MOBIL
                    if(input3==1):
                        baru=str(input('masukkan merk mobil baru : '))
                        print ('anda akan mengubah data merk mobil dari {} menjadi {}. \n'.format(database[input2][0],baru))
                        cek=input('apakah data yang ingin dirubah sudah benar? (Y/N)')
                        if cek=='Y':
                            database[input2][0]=baru
                            print('Database telah di update, berikut merupakan data terbaru : ','\n',)
                            print_data()
                        else:
                            break
        # MENGGANTI TIPE MOBIL
                    elif(input3==2):
                        baru=str(input('masukkan tipe mobil baru : '))
                        print ('anda akan mengubah data tipe mobil dari {} menjadi {}. \n'.format(database[input2][1],baru))
                        cek=input('apakah data yang ingin dirubah sudah benar? (Y/N)')
                        if cek=='Y':
                            database[input2][1]=baru
                            print('Database telah di update, berikut merupakan data terbaru : ','\n')
                            print_data()
                        else:
                            break
        # MENGGANTI NOMOR POLISI MOBIL
                    elif(input3==3):
                        baru=str(input('masukkan nomor polisi mobil baru : '))
                        print ('anda akan mengubah data nomor polisi mobil dari {} menjadi {}. \n'.format(database[input2][2],baru))
                        cek=input('apakah data yang ingin dirubah sudah benar? (Y/N)')
                        if cek=='Y':
                            database[input2][2]=baru
                            print('Database telah di update, berikut merupakan data terbaru : ','\n')
                            print_data()
                        else:
                            break
        # UPDATE STATUS MOBIL
                    elif (input3==4):
                        baru=str(input('update ketersediaan mobil : '))
                        print ('anda akan mengubah status ketersediaan mobil dari {} menjadi {}. \n'.format(database[input2][3],baru))
                        cek=input('apakah data yang ingin dirubah sudah benar? (Y/N)')
                        if cek=='Y':
                            database[input2][3]=baru
                            print('Database telah di update, berikut merupakan data terbaru : ','\n')
                            print_data()
                        else:
                            break
                    elif (input3==5):
                        break                
                    else:
                        print('Menu yang anda pilih tidak tersedia')
        # INPUT ID TIDAK ADA
                else:
                    print("id yang anda cari tidak tersedia") 
        # INPUT KELUAR DARI MENU 
            if (input1==2):
                break
    else:
        print('Saat ini data mobil tidak tesedia')
    return database

# MENU 4 : DELETE DATA
def menu4():
    global database
    while(True):
        print('''
        -------------------------
        Menu yang dapat diakses : 
        1. Menghapus Data
        2. exit menu
        ''')
    # INPUT MENU YANG DIPILIH
        input1=int(input('Masukkan menu yang ingin digunakan : ')) 
        if(input1==1):
    # MENGECEK ISI DATA, JIKA ADA ADA MAKA BISA DILAKUKAN DELETE DATA
            if(len(database)>0):
                print_data()
                input2=int(input('masukkan ID mobil yang ingin dihapus : '))
    # MENGECEK ID MOBIL YANG ADA UNTUK DIHAPUS
                for i in database:
                    if (input2==i):
                        print('ID yang akan dihapus memiliki ID {} dengan keterangan merk mobil {}, tipe mobil {} dengan nomor polisi {}'.format(input2,database[i][0],database[i][1],database[i][2]))
    # KONFIRMASI HAPUS DATA
                        input3=input('Apakah data yang ingin dihapus sudah benar?(Y/N) : ')
                        if(input3=='Y'):
                            database.pop(i)
                            print ('Data sudah berhasil dihapus')
                            break
                        else:
                            break
                else:
                    print('ID yang ingin di hapus tidak ada')
            else:
                print('Saat ini data mobil tidak tesedia')
        if(input1==2):
            break
    return database

# MENU TAMBAHAN : DISPLAY DATA TABEL
def print_data ():
    global database
    print ("{:<5} | {:<15} | {:<15} | {:<15} | {:<15}".format ('ID','Merk Mobil','Tipe Mobil','No.Polisi','Status'))
    for key, value  in database.items():
        ID = key
        Merk,Tipe,Nopol,status = value
        print ("{:<5} | {:<15} | {:<15} | {:<15} | {:<15}".format(ID,Merk,Tipe,Nopol,status))

# MENU UTAMA
print( 'SELAMAT DATANG DI SEWA MOBIL SEMANTAPNYA')
while (True):
    hello()
    menu=int(input('silakan masukkan nomor menu yang ingin dituju : '))
    if(menu==1):
        menu1()
    elif(menu==2):
        menu2()
    elif(menu==3):
        menu3()
    elif(menu==4):
        menu4()
    elif(menu==5):
        break
    else:
        print('Pilihan yang anda masukkan salah')
        continue