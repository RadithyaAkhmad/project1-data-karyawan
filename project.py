import csv
import os

# Variabel untuk menyimpan file
nama_file = r'C:\Users\Toshiba\OneDrive\Desktop\belajar python\data_karyawan.csv'

# Fungsi untuk membuat file csv
def init_csv():
    if not os.path.exists(nama_file):  # Perbaikan pengecekan file
        with open(nama_file, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama', 'Jabatan', 'Gaji'])

# Fungsi untuk menambahkan karyawan           
def tambah_karyawan(id, name, jabatan, gaji):
    with open(nama_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, name, jabatan, gaji])
    print("Data karyawan berhasil ditambahkan")

# Fungsi untuk menghapus karyawan 
def hapus_karyawan(id):
    rows = []
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])  # Menulis header
        found = False
        for row in rows[1:]:
            if row[0] != id:
                writer.writerow(row)
            else:
                found = True
        if found:
            print(f'Data karyawan dengan ID {id} berhasil dihapus')
        else:
            print(f'Data karyawan dengan ID {id} tidak ditemukan')

# Fungsi untuk mengubah data karyawan               
def update(id, nama=None, jabatan=None, gaji=None):
    rows = []
    updated = False
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)
        
    with open(nama_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])  # Menulis header
        for row in rows[1:]:
            if row[0] == id:
                if nama is not None:
                    row[1] = nama
                if jabatan is not None:
                    row[2] = jabatan
                if gaji is not None:
                    row[3] = gaji
                updated = True
            writer.writerow(row)
    
    if updated:
        print(f'Data karyawan dengan ID {id} berhasil diperbarui')
    else:
        print(f'Data karyawan dengan ID {id} tidak dapat diperbarui')

# Fungsi untuk menampilkan semua karyawan 
def tampilkan_data():
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')

# Fungsi untuk menampilkan karyawan berdasarkan ID
def tampilkan_data_id(id):
    found = False
    with open(nama_file, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader)  # Melewati header
        for row in reader:
            if row[0] == id:
                found = True
                print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')
                break
    if not found:
        print(f'Tidak dapat menemukan karyawan dengan ID {id}')

# Fungsi menu
def menu():
    while True:
        print('\nPilihan')
        print('1. Menambahkan Karyawan')
        print('2. Menghapus Karyawan')
        print('3. Update Karyawan')
        print('4. Tampilkan Semua Karyawan')
        print('5. Tampilkan Karyawan Berdasarkan ID')
        print('6. Keluar')

        input_user = int(input('Masukkan Pilihan: '))
        if input_user == 1:
            id = input('Masukkan ID: ')
            nama = input('Masukkan Nama Karyawan: ')
            jabatan = input('Masukkan Jabatan: ')
            gaji = input('Masukkan Gaji: ')
            tambah_karyawan(id, nama, jabatan, gaji)
        elif input_user == 2:
            id = input('Masukkan ID Karyawan yang ingin dihapus: ')
            hapus_karyawan(id)
        elif input_user == 3:
            id = input('Masukkan ID Karyawan yang ingin diperbarui: ')
            nama = input('Masukkan Nama Baru (kosongkan jika tidak diubah): ')
            jabatan = input('Masukkan Jabatan Baru (kosongkan jika tidak diubah): ')
            gaji = input('Masukkan Gaji Baru (kosongkan jika tidak diubah): ')
            update(id, nama if nama else None, jabatan if jabatan else None, gaji if gaji else None)
        elif input_user == 4:
            tampilkan_data()
        elif input_user == 5:
            id = input('Masukkan ID Karyawan yang ingin Anda cari: ')
            tampilkan_data_id(id)
        elif input_user == 6:
            print('Keluar dari program')
            break
        else:
            print('Perintah tidak valid')

if __name__ == "__main__":
    init_csv()
    menu()
