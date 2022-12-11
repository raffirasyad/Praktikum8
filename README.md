# Praktikum8

Buat program sederhana dengan mengaplikasikan penggunaan class. Buatlah
class untuk menampilkan daftar nilai mahasiswa, dengan ketentuan:

• Method tambah() untuk menambah data

• Method tampilkan() untuk menampilkan data

• Method hapus(nama) untuk menghapus data berdasarkan nama

• Method ubah(nama) untuk mengubah data berdasarkan nama

• Buat diagram class, flowchart dan penjelasan programnya pada
README.md.


1. Membuat ```diagram class``` dan ```flowchart``` dari pemograman yang akan kita buat

![foto 6](https://user-images.githubusercontent.com/115473988/206904327-49552722-e6f8-4529-a764-55c816ff5f96.png)


![foto 5](https://user-images.githubusercontent.com/115473988/206904347-5df7f29c-6ff2-4add-9ea7-88c2df3835c1.png)


2. Membuat folder dan file baru untuk pengerjaan pemogramman yang akan dibuat

<img width="146" alt="foto 1" src="https://user-images.githubusercontent.com/115473988/206904434-471c4212-1d2a-4f8e-a861-dda83f93e040.png">


3. Masukan Kodingan Berikut

``` pyhton

from tabulate import tabulate

class Mahasiswa:
    def __init__(self):

        self.dataMasiswa = {
            'No' : [],
            'Nim' : [],
            'Nama' : [],
            'Tugas' : [],
            'Uts' : [],
            'Uas' : [],
            'Nilai Akhir' : []
        }
    def tampilkan(self):
        print("Berikut data yang ada")
        print(tabulate(self.dataMasiswa, headers=[
            'No','Nim','Nama','Tugas','UTS','UAS','Nilai Akhir'], tablefmt="fancy_grid"))
    
    def tambah(self, no):
        nim = int(input("Masukan Nim : "))
        nama = input("Masukan Nama : ")
        tugas = int(input("Masukan Nilai Tugas : "))
        uts = int(input("Masukan Nilai Uts : "))
        uas = int(input("Masukan Nilai Uas : "))
        nilai_akhir =(tugas * 30 / 100) + (uts * 35 / 100) + (uas * 35 / 100)

        self.dataMasiswa['No'].append(no)
        self.dataMasiswa['Nim'].append(nim)
        self.dataMasiswa['Nama'].append(nama)
        self.dataMasiswa['Uts'].append(uts)
        self.dataMasiswa['Tugas'].append(tugas)
        self.dataMasiswa['Uas'].append(uas)
        self.dataMasiswa['Nilai Akhir'].append(nilai_akhir)
        print('Data berhasil ditambahkan. ')

    def ubah(self, nama):

            if nama in self.dataMasiswa['Nama']:
                namaIndex = self.dataMasiswa['Nama'].index(nama)
                print("Pilih data yang akan dirubah")

                while True:
                    editApa = int(input(
                        "(1)Nim, \n (2) Nama,\n (3) Nilai Tugas,\n (4) Nilai Uts,\n (5) Nilai Uas,\n (0) Simpan Perubahan & Keluar \n : "))
                    print("")

                    if editApa == 1:

                        NewNim = int(input("Masukan Nim Baru :"))
                        self.dataMasiswa['Nim']['namaIndex'] = NewNim
                    elif editApa == 2:
                        newNama = input ("Masukan Nama baru : ")
                        self.dataMasiswa['Nama'][namaIndex] = newNama
                    elif editApa == 3:
                        newTugas = int(input("Masukan Nilai Tugas : "))
                        nilai_akhir = (newTugas * 30 / 100 ) + (self.dataMasiswa['Uts']['namaIndex'] * 35 / 100 ) + (
                            self.dataMasiswa['Uas'][namaIndex] * 35 / 100 )
                        self.dataMasiswa['Tugas'][namaIndex] = newTugas
                        self.dataMasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
                    elif editApa == 4:
                        newUts = int(input("Masukan Nilai UTS : "))
                        nilai_akhir = (self.dataMasiswa['Tugas']['namaIndex'] * 30 / 100 ) + (newUts * 35 / 100) + (
                            self.dataMasiswa['Uas'][namaIndex] * 35 / 100)
                        self.dataMasiswa['Uts'][namaIndex] = newUts
                        self.dataMasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
                    elif editApa == 5:
                        newUas = int(input("Masukan Nilai Uas : "))
                        nilai_akhir = (self.dataMasiswa['Tugas'][namaIndex] * 30 / 100 ) + (self.dataMasiswa['Uts'][namaIndex] * 35 / 100 ) + (
                            newUas * 35 / 100 )
                        self.dataMasiswa['Uas']['namaIndex'] = newUas
                        self.dataMasiswa['Nilai Akhir'][namaIndex] = nilai_akhir
                    elif editApa == 0:
                        print('Perubahan Berhasil')
                        break
                else:
                    print("Data Tidak Ditemukan")

    def hapus(self, nama):
                if nama in self.dataMahasiswa['Nama']:
                    namaIndex = self.dataMahasiswa['Nama'].index(nama)

                    del self.dataMahasiswa['No'][namaIndex]
                    del self.dataMahasiswa['Nim'][namaIndex]
                    del self.dataMahasiswa['Nama'][namaIndex]
                    del self.dataMahasiswa['Tugas'][namaIndex]
                    del self.dataMahasiswa['Uts'][namaIndex]
                    del self.dataMahasiswa['Uas'][namaIndex]
                    del self.dataMahasiswa['Nilai Akhir'][namaIndex]
                    print("data berhasil dihapus. ")
                else:
                    print("Data Tidak Ditemukan")
no = 0
instanceMhs = Mahasiswa()

while True:
    tanya = input(
        "(C) Menambah Data, \n (R) Tampilkan Semua Data,\n (U) Perbaruhi data,\n (D) Hapus Data,\n (F) Mencari data,\n (Q) Keluar Program : ")
    if tanya == "C" :

        while True :
            no += 1

            instanceMhs.tambah(no)
            tambahDataLagi = input("Tambah data Lagi (y/n) :")
            if tambahDataLagi == 'n' :
                break
        
    elif tanya == 'R':
        instanceMhs.tampilkan()
        print("")

    elif tanya == 'U' :
        print(tabulate(instanceMhs.dataMasiswa, headers=['No','Nim','Nama','Tugas','UTS','UAS','Nilai Akhir'], tablefmt="fancy_grid"))
        nama = input('Masukan Nama Yang Akan Dirubah : ')
        print("")
        instanceMhs.ubah(nama)
        print("")
    elif tanya == 'D':
        print(tabulate(instanceMhs.dataMasiswa, headers=['No','Nim','Nama','Tugas','UTS','UAS','Nilai Akhir'], tablefmt="fancy_grid"))
        nama = input('Masukan Nama Yang Akan Dihapus: ')
        print("")
        instanceMhs.hapus(nama)
    
        
    elif tanya == "Q":
        print("")
        print("Anda Tela Keluar Dari Program")
        break

```

3. Berikut merupakan hasil Outputnya

<img width="499" alt="foto 2" src="https://user-images.githubusercontent.com/115473988/206904585-2b21e16d-1d60-4167-8c94-ade521c4ee77.png">
<img width="456" alt="foto 3" src="https://user-images.githubusercontent.com/115473988/206904588-84661a6c-816a-4b72-98f5-4714ef2b80a3.png">
<img width="470" alt="foto 4" src="https://user-images.githubusercontent.com/115473988/206904591-eee97b5d-2bde-4950-b402-5c52f80cf9a1.png">

