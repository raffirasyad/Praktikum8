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