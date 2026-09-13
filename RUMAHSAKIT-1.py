import re
from datetime import datetime
from os import system
from collections import deque

hari = datetime.now()

# Fungsi untuk memeriksa email yang valid
def email_valid(email):
    domain_valid = ["@gmail.com", "@madwasleft.com"]
    return any(email.endswith(domain) for domain in domain_valid)

# Fungsi untuk memeriksa kata sandi yang valid
def sandi_valid(sandi):
    if len(sandi) < 7:
        return False
    if not re.search(r"[a-zA-Z]", sandi):
        return False
    if not re.search(r"\d",sandi):
        return False
    return True

# Implementasi Queue
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self):
        self.head = Node ("head")
        self.size = 0

    def isEmpty(self):
        return self.size == 0
    
    def peek(self):
        if self.isEMpty():
            raise Exception("Memriksa antrian yang kosong")
        return self.head.next.value
    
    def enqueue(self, value):
        node = Node(value)
        node.next = self.head.next
        self.head.next = node
        self.size += 1

    def dequeue(self):
        if self.isEmpty():
            raise Exception("menghapus antrian dari tumpukan kosong")
        remove = self.head.next
        self.head.next = self.head.next.next
        self.size -=1
        return remove.value
    
    def getSize(self):
        return self.size
    
class Pasien:
    def __init__(self, nomor_antrian, nama, usia, email, password, tahun_lahir, bulan_lahir, tanggal_lahir):
        # Validasi email dan kata sandi
        if not email_valid(email):
            raise ValueError(input("Email tidak valid. Harus menggunakan @gmail.com atau @madwasleft.com"))
        
        if not sandi_valid(password):
            raise ValueError(input("Kata sandi tidak valid. Panjang minimal 7 karakter dan harus campuran angka dan huruf"))
        
        # Inisialisasi atribut
        self.nomor_antrian = nomor_antrian
        self.nama = nama
        self.usia = usia
        self.email = email
        self.password = password
        self.tanggal_lahir = datetime (tahun_lahir, bulan_lahir, tanggal_lahir)
        self.departemen = ""
        self.biaya = 0
        self.biaya_obat = 0
        self.biaya_vitamin = 0
        self.metode_pembayaran = ""
        self.riwayat_tindakan = Queue()
        self.keluhan = ""
        self.obat = ""
        self.resep = []
        self.harga = 0
        self.lunas = ""
        self.total_harga = 0

    # Metode untuk menambah tindakan
    def tambah_tindakan (self, tindakan):
        self.riwayat_tindakan.enqueue(tindakan)

        # Metode untuk memilih departemen dan mendapatkan keluhan penyakit
    def pilih_departemen(self):
        system('cls')
        template()
        print("Selamat Datang, {}!".format(self.nama))
        print("Departemen di Rumah Sakit Semoga Sehat:")
        print("1. Poli Umum")
        print("2. Poli Spesialis Penyakit Dalam")
        print("3. Poli Gigi")

        pilihan_departemen = input("Pilih departemen (1/2/3): ")

        if pilihan_departemen == "1":
            self.departemen = "Umum                     "
            self.biaya = 500000
            self.biaya_obat = 50000
            self.biaya_vitamin = 20000
            self.gedung_a()

        elif pilihan_departemen == "2":
            self.departemen = "Spesialis Penyakit Dalam "
            self.biaya = 1500000
            self.biaya_obat = 75000
            self.biaya_vitamin = 40000
            self.gedung_b()

        elif pilihan_departemen == "3":
            self.departemen = "Gigi                     "
            self.biaya = 1000000
            self.biaya_obat = 50000
            self.biaya_vitamin = 30000
            self.gedung_c()

        else:
            print("Pilihan departemen tidak valid.")
            return
        
        #self.keluhan = input("Masukkan keluhan penyakit : ")
        #print("\nAnda telah memilih departemen {} dan memasukkan keluhan: '{}'. Terima kasih!".format(self.departemen, self.keluhan))
        
    def gedung_a(self):
        self.gedung = "Gedung A"
        print("\nPasien {} telah memilih Poli {}".format(self.nama,self.departemen))
        self.keluhan = input("Masukkan Keluhan Penyakit: ")

        print("\nPilih Jam Periksa: ")
        print("1. Pukul 10.00 - 11.00")
        print("2. Pukul 12.00 - 13.00")
        print("3. Pukul 14.00 - 15.00")
        print("4. Pukul 15.00 - 16.00")
        print("5. Pukul 16.00 - 17.00")

        while True:
            pilih_jam = input("\nMasukkan pilihan (1/2/3/4/5): ")
            if pilih_jam == "1":
                jadwal = ("10.00 - 11.00", "Dr. Alfiansyah Saputra", "10A")
            elif pilih_jam == "2":
                jadwal = ("12.00 - 13.00", "Dr. Amanda Diana", "12A")
            elif pilih_jam == "3":
                jadwal = ("14.00 - 15.00", "Dr. Aditya Pratama", "14A")
            elif pilih_jam == "4":
                jadwal = ("15.00 - 16.00", "Dr. Mahesa Baskara", "15A")
            elif pilih_jam == "5":
                jadwal = ("16.00 - 17.00", "Dr. Firman Alamsyah", "16A")
            else:
                print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                continue

            if jadwal in jadwal_terisi:
                print("Jadwal ini sudah terisi, silahkan pilih jadwal lain.")
            else:
                self.jam_temu, self.dokter, self.ruang = jadwal
                jadwal_terisi.add(jadwal)
                break

        self.struk_antrian_ruangan()
    
    def gedung_b(self):
        self.gedung = "Gedung B"
        print("\nPasien {} telah memilih Poli {}".format(self.nama, self.departemen))
        print("\nPilih Subspesialis Penyakit Dalam:")
        print("1. Kardiovaskular / jantung")
        print("2. Gastroenterologi dan Hepatologi / sistem pencernaan")
        print("3. Ginjal dan Hipertensi")
        print("4. Reumatologi / Sendi-otot-jaringan")
        print("5. Penyakit tropik-infeksi")

        pilih_spd = input("Masukkan Pilihan (1/2/3/4/5): ")
        if pilih_spd == "1":
            self.keluhan = input("Masukkan Keluhan Penyakit : ")
            print("\nPilih Jam Periksa: ")
            print("1. Pukul 08.00 - 09.00")
            print("2. Pukul 11.30 - 12.30")
            print("3. Pukul 19.00 - 20.00")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2/3): ")
                if pilih_jam == "1":
                    jadwal = ("08.00 - 09.00", "Dr. Angga Sp.PD-KKV (Kardiovaskular)", "02B")
                elif pilih_jam == "2":
                    jadwal = ("11.30 - 12.30", "Dr. Amar Sp.PD-KKV (Kardiovaskular)", "04B")
                elif pilih_jam == "3":
                    jadwal = ("19.00 - 20.00", "Dr. Nuaiman Sp.PD-KKV (Kardiovaskular)", "09B")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break
        
        elif pilih_spd == "2":
            self.keluhan = input("\nMasukkan Keluhan Penyakit : ")
            print("\nPilih Jam Periksa: ")
            print("1. Pukul 10.00 - 11.00")
            print("2. Pukul 16.00 - 17.00")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("10.00 - 11.00", "Dr. Aman Sp.PD-KGEH (Sistem Pencernaan)", "03B")
                elif pilih_jam == "2":
                    jadwal = ("16.00 - 17.00", "Dr. Awan Sp.PD-KGEH (Sistem Pencernaan)", "07B")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break

        elif pilih_spd == "3":
            self.keluhan = input("\nMasukkan Keluhan Penyakit : ")
            print("\nPilih Jam Periksa: ")
            print("1. Pukul 07.00 - 08.00")
            print("2. Pukul 17.30 - 18.30")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("07.00 - 08.00", "Dr. Susi Sp.PD-KGH (Ginjal/hipertensi)", "01B")
                elif pilih_jam == "2":
                    jadwal = ("17.30 - 18.30", "Dr. Fabio Sp.PD-KGH (Ginjal/Hipertensi)", "08B")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break            

        elif pilih_spd == "4":
            self.keluhan = input("\nMasukkan Keluhan Penyakit : ")
            print("\nPilih Jam Periksa: ")
            print("1. Pukul 14.30 - 15.30")
            print("2. Pukul 22.00 - 23.00")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("14.30 - 15.30", "Dr. Shavira Sp.PD-KR (Reumatologi)", "06B")
                elif pilih_jam == "2":
                    jadwal = ("22.00 - 23.00", "Dr. Gio Sp.PD-KR (Reumatologi)", "11B")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break 

        elif pilih_spd == "5":
            self.keluhan = input("\nMasukkan Keluhan Penyakit: ")
            print("\nPilih Jam Periksa: ")
            print("1. Pukul 13.00 - 14.00")
            print("2. Pukul 20.30 - 21.30")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("13.00 - 14.00", "Dr. Erhans Sp.PD-KPTI (Tropik-Infeksi)", "05B")
                elif pilih_jam == "2":
                    jadwal = ("21.30 - 22.30", "Dr. Mulya Sp.PD-KPTI (Tropik-Infeksi)", "10B")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break 

        else:
            input("Silahkan pilih jam temu yang tersedia.")
            return
        
        self.struk_antrian_ruangan()
        
    def gedung_c(self):
        self.gedung = "Gedung C"
        print ("\nPasien {} telah memilih Poli {}".format(self.nama, self.departemen))
        print("\nPilih Subspesialis Gigi:")
        print("1. Ortodonti / gigi tidak sejajar")
        print("2. Konservasi Gigi")
        print("3. Kedokteran Gigi Anak")
        print("4. Prostodonsia / Implan Gigi")
        print("5. Penyakit Mulut / Infeksi")

        pilih_sg = input("Masukkan Pilihan (1/2/3/4/5): ")
        if pilih_sg == "1":
            self.keluhan = input("\nMasukkan Keluhan Penyakit: ")
            print("\nPilih Jam Periksa: ")
            print("1. Pukul 07.00 - 08.00")
            print("2. Pukul 13.00 - 14.00")
            
            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("07.00 - 08.00", "Drg. Ardiansyah Sp.Ort (Ortodonti)", "01C")
                elif pilih_jam == "2":
                    jadwal = ("13.00 - 14.00", "Drg. Jeremy Sp.Ort (Ortodonti)", "05C")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break

        elif pilih_sg == "2":
            self.keluhan = input("\nMasukkan Keluhan Penyakit: ")
            print("\nPilih Jam Periksa:")
            print("1. Pukul 08.30 - 09.30")
            print("2. Pukul 14.30 - 15.30")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("08.30 - 09.30", "Drg. Rakha Sp.Perio (Periodontis)", "02C")
                elif pilih_jam == "2":
                    jadwal = ("14.30 - 15.30", "Drg. Alfar Sp.Perio (Periodonstis)", "06C")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break

        elif pilih_sg == "3":
            self.keluhan = input("\nMasukkan Keluhan Penyakit: ")
            print("\nPilih Jam Periksa:")
            print("1. Pukul 10.00 - 11.00")
            print("2. Pukul 19.00 - 20.00")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("10.00 - 11.00", "Drg. Mirna Sp.KGA (Gigi Anak)", "03C")
                elif pilih_jam == "2":
                    jadwal = ("19.00 - 20.00", "Drg. Bella Sp.KGA (Gigi Anak)", "09C")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break

        elif pilih_sg == "4":
            self.keluhan = input("\nMasukkan Keluhan Penyakit: ")
            print("\Pilih Jam Periksa:")
            print("1. Pukul 11.30 - 12.30")
            print("2. Pukul 20.30 - 21.30")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("11.30 - 12.30", "Drg. Amira Sp.Pros (Prostodonsia)", "04C")
                elif pilih_jam == "2":
                    jadwal = ("20.30 - 21.30", "Drg. Rizky Sp.Pros (Prostodonsia)", "10C")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break
           
        elif pilih_sg == "5":
            self.keluhan = input("\nMasukkan Keluhan Penyakit: ")
            print("\nPilih Jam Periksa: ")
            print("1. Pukul 14.30 - 15.30")
            print("2. Pukul 17.30 - 18.30")

            while True:
                pilih_jam = input("\nMasukkan pilihan (1/2): ")
                if pilih_jam == "1":
                    jadwal = ("14.30 - 15.30", "rg. Bayu Sp.PM (Penyakit Mulut)", "06C")
                elif pilih_jam == "2":
                    jadwal = ("17.30 - 18.30", "Drg. Masnaka Sp.PM (Penyakit Mulut)", "08C")
                else:
                    print("Pilihan tidak valid. Silahkan pilih jam temu yang tersedia.")
                    continue

                if jadwal in jadwal_terisi:
                    print("Jadwal ini sudah terisi, silahkan pilih jadawl lain.")
                else:
                    self.jam_temu, self.dokter, self.ruang = jadwal
                    jadwal_terisi.add(jadwal)
                    break

        else:
            input("Silahkan pilih jam temu yang tersedia.")
            return
        
        self.struk_antrian_ruangan()

    def struk_antrian_ruangan(self):
        system("cls")
        print("-----------------------------------------------------------")
        print("                       STRUK RUANGAN                      ")
        print("-----------------------------------------------------------")
        print(f"POLI            : {self.departemen}")
        print(f"DOKTER          : {self.dokter}")
        print(f"JAM TEMU        : Pukul {self.jam_temu} WIB")
        print(f"RUANG/GEDUNG    : {self.ruang}/{self.gedung}")
        print(f"KELUHAN         : {self.keluhan}")
        print(f"PASIEN          : {self.nama}")
        print("-----------------------------------------------------------\n")
        print("                  Harap untuk datang tepat ")
        print("             dengan waktu yang sudah ditentukan")

        kembali = input("\n\n(!) Tekan enter untuk kembali ke menu utama.")
        kembali = RumahSakitSemogaSehat.jalankan_program

    def pilih_metode_pembayaran(self):
        print("\nPilih Metode Pembayaran: ")
        print("1. ATM")
        print("2. Digital")
        print("3. BPJS")
        
        pilihan_metode = input("Pilih metode pembayran (1/2/3): ")

        if pilihan_metode == "1":
            self.metode_pembayaran = "ATM"
            self.lunas = 'LUNAS'
            self.bayar_pakai_atm()
        elif pilihan_metode == "2":
            self.metode_pembayaran = "Digital"
            self.lunas = "LUNAS"
            self.bayar_pakai_digital()
        elif pilihan_metode == "3":
            self.metode_pembayaran = "Di tanggung oleh BPJS"
            self.lunas = 'LUNAS'
            self.tampilkan_bukti_pembayaran()
        else:
            print("Pilihan metode pembayaran tidak valid.")

    def bayar_pakai_atm(self):
        print(f"Pasien {self.nama} memilih metode pepmbayaram melalui ATM.")

        while True:
            nomor_atm = input("Masukkan nomor ATM (7 digit): ")

            if nomor_atm.isdigit() and len(nomor_atm) == 7:
                self.tambah_tindakan("Pembayaran via ATM")
                self.tampilkan_bukti_pembayaran()
                break
            else:
                print("Pembayaran gagal. Nomor atm harus memiliki 7 digit dan hanya berisi angka.")

    def bayar_pakai_digital(self):
        print(f"Pasien {self.nama} memilih metode pembayaran melalui Digital.")

        while True:
            nomor_digital = input("Masukkan nomor digital (8 digit): ")

            if nomor_digital.isdigit() and len(nomor_digital) == 8:
                self.tambah_tindakan("Pembayaran via Digital")
                self.tampilkan_bukti_pembayaran()
                break
            else:
                print("Pembayaran gagal. Nomor digital harus memiliki 8 digit dan hanya berisi angka.")

    def tambah_obat(self, nama_obat, daftar_obat):
        if nama_obat in daftar_obat:
            self.harga = daftar_obat[nama_obat]
            self.resep.append((nama_obat, self.harga))
            self.total_harga += self.harga
        else:
            print(f"Obat {nama_obat} tidak ditemukan.")
        
    def menginput_obat(self, input_obat, daftar_obat):
        nama_obat_list = input_obat.split(',')
        for nama_obat in nama_obat_list:
            self.tambah_obat(nama_obat.strip(), daftar_obat)
    
    def tampilkan_bukti_pembayaran(self):
        system("cls")
        total_biaya = self.biaya + self.biaya_obat + self.biaya_vitamin + self.total_harga
        print("-----------------------------------------------------")
        print("                    STRUK PEMBAYARAN                 ")
        print("-----------------------------------------------------")
        print(f"Nama Pasien         : {self.nama}")
        print(f"Nama Dokter         : {self.dokter}")
        print(f"Jam Temu            : {self.jam_temu}")
        print(f"Ruang/Gedung        : {self.ruang}/{self.gedung}")
        
        print("\nUntuk Pembayaran:")
        print(f"Poli {self.departemen}  : Rp. {self.biaya}")
        #print(f"                                : Rp. {self.biaya_obat} (Obat)")
        print(f"                                  Rp. {self.biaya_vitamin} (Vitamin)")
        print(f"Resep Obat                      : ")
        for nama_obat, self.harga in self.resep:
            print(f" - {nama_obat: ^28} : Rp. {self.harga}")

        print("                                 -------------------------- +")
        print(f"Total Pembayaran                : Rp. {total_biaya} ")
        print(f"\nCara Pembayaran                 : {self.metode_pembayaran}")
        #print(f"Status Pembayaran               : {self.lunas}")

        print("\n\n             NOMOR ANTRIAN OBAT ANDA [{}]".format(self.nomor_antrian))
        print("\n       Silahkan ke meja farmasi untuk mengambil obat")
        print("\n\n                                           Cikarang, {}".format(hari.strftime("%d-%m-%y")))

        input("\n(!) Tekan enter untuk kembali ke halaman utama.")
        RumahSakitSemogaSehat.jalankan_program

    
class RumahSakitSemogaSehat:
    def __init__ (self):
        self.pasien_terdaftar = []
        self.antrian_sekarang = 1
        self.riwayat_pasien = [] # List untuk menyimpan riwayat pasien

    def registrasi_pasien_baru(self):
        system('cls')
        print("=====================================================")
        print("{:^55}".format("HALAMAN REGISTRASI"))
        print("{:^55}".format("Tanggal Registrasi {}".format(hari.strftime("%d-%m-%y %H:%M:%S"))))
        print("=====================================================")

        nama = input("Nama Pasien             : ")
        usia = int(input("Masukkan Usia           : "))
        email = input("Masukkan alamat email   : ")
        password = input("Masukkan Password       : ")
        tahun_lahir = int(input("Masukkan tahun lahir    : "))
        bulan_lahir = int(input("Masukkan bulan lahir    : "))
        tanggal_lahir = int(input("Masukkan tanggal lahir  : "))

        try:
            nomor_antrian = self.antrian_sekarang
            pasien = Pasien(nomor_antrian, nama, usia, email, password, tahun_lahir, bulan_lahir, tanggal_lahir)
            pasien.pilih_departemen() # Pilih departemen dan minta keluhan penyakit

            pasien.tambah_tindakan("Registrasi")

            self.pasien_terdaftar.append(pasien)
            self.riwayat_pasien.append(pasien)  # Tambahkan pasien ke riwayat
            self.antrian_sekarang += 1 # Jaga urutan antrian
            print("Registrasi berhasil. Nomor antrian anda: {}. Selamat Bergabung, {}!".format(nomor_antrian, nama))
        except ValueError as e:
            print(str(e)) # Menampilkan pesan kesalahn jika registrasi gagal

    def jalankan_program(self):

        while True:
            system("cls")
            template()
            print("      Selamat datang di Rumah Sakit Semoga Sehat     ")
            print('-----------------------------------------------------')
            print("|1. Registrasi Pasien Baru                          |")
            print("|2. Lakukan Pembayaran                              |")
            print("|3. Lihat Antrian obat                              |")
            print("|4. Lihat Riwayat Pasien                            |")
            print("|5. Pembatalan                                      |")
            print("|6. Exit                                            |")
            print('=====================================================')

            pilihan = input("Pilih Opsi (1/2/3/4/5/6): ")
            
            if pilihan == "1":
                self.registrasi_pasien_baru()

            elif pilihan == "2":
                if not self.pasien_terdaftar:
                    input("Tidak ada pasien yang terdaftar. Silahkan daftar dulu.")
                else:
                    # Memilih pasien untuk pembayaran
                    system('cls')
                    print("Daftar Pasien yang Terdaftar:")
                    for i, pasien in enumerate(self.pasien_terdaftar):
                        print(f"{i+1}. {pasien.nama}")
                    index_pasien = int(input("Pilih pasien untuk pembayaran (nomor): ")) - 1 
                    if 0 <= index_pasien < len(self.pasien_terdaftar):
                        input_obat  = input("Masukkan resep obat: ")
                        pasien.menginput_obat(input_obat, daftar_obat)
                        self.pasien_terdaftar[index_pasien].pilih_metode_pembayaran()
                    else:
                        print("Nomor pasien tidak valid")
                        
            elif pilihan == "3":
                if not self.pasien_terdaftar:
                    input("Tidak ada pasien dalam antrian obat.")
                else:
                    for pasien in self.pasien_terdaftar:
                        if pasien.lunas == "LUNAS":
                            if self.antrian_sekarang:
                                print("Daftar antrian obat saat ini:")
                                for i, pasien in enumerate(self.pasien_terdaftar):
                                    print(f"{i+1}. {pasien.nama}")
                                panggil = input("\nPanggil pasien? [y/n]: ")
                                if panggil == "y":
                                    if self.pasien_terdaftar:
                                            pasien = self.pasien_terdaftar.pop(0)
                                            print(f"{pasien.nama} sedang dipanggil untuk mengambil obat.")
                                    else:
                                            input("Tidak ada pasien dalam antrian.")
                                elif panggil == "n":
                                        self.jalankan_program
                                else:
                                    input("Silahkan pilih yes (y) atau no (n).")
                            else:
                                input("Antrian kosong.")
                        else:
                            input("Pasien belum membayar dan tidak ada di dalam antrian obat.")
   

            elif pilihan == "4":
                if not self.riwayat_pasien:
                    input("Tidak ada riwayat pasien.")
                else:
                    self.tampilan_riwayat()

            elif pilihan == "5":
                print("Daftar Pasien Rumah Sakit Semoga Sehat.")
                for i, pasien in enumerate (self.pasien_terdaftar):
                    print(f"{i+1}. {pasien.nama}")
                if not self.pasien_terdaftar:
                    input("Tidak ada pasien yang terdaftar.")
                else:
                    if pasien.lunas == "LUNAS":
                        print("Pasien tidak bisa melakukan pembatalan karena sudah melakukan pembayaran.")
                    else:

                        for pasien in self.pasien_terdaftar:
                            nama = input("Masukkan Nama pasien yang ingin dibatalkan : ")
                            if pasien.nama == nama:
                                self.pasien_terdaftar.remove(pasien)
                                self.alasan_batal = input("Alasan : ")
                                print(f"Antrian ruangan untuk {nama} telah dibatalkan.")
                                break
                        print(f"{nama} tidak ditemukan dalam antrian ruangan.")
                    
                    input("\n(!) Tekan enter untuk kembali ke halaman utama")
            
            elif pilihan == "6":
                input("Terima kasih telah menggunakan layanan Rumah Sakit Semoga Sehat.")
                break

            else:
                input("Pilihan tidak valid. Silahkan pilih opsi yang benar!")

    def tampilan_riwayat(self):
        if self.riwayat_pasien:
            for i, pasien in enumerate(self.riwayat_pasien, start = 1):
                print("\n DAFTAR RIWAYAT PASIEN {}".format(i))
                print(f"nama                : {pasien.nama}")
                print(f"Usia                : {pasien.usia}")
                print(f"Tanggal Lahir       : {pasien.tanggal_lahir.date()}")
                print(f"Keluhan             : {pasien.keluhan}")
                print(f"Metode Pembayaran   : {pasien.metode_pembayaran}")
        input("\n(!) Tekan enter untuk kembali ke halaman utama.")
        
        RumahSakitSemogaSehat.jalankan_program

def template():
    print('=====================================================')
    print('|              RUMAH SAKIT SEMOGA SEHAT             |')
    print('=====================================================')

# Daftar obat dan harga
daftar_obat = {
            "Paracetamol": 20000,
            "Ibuprofen": 35000,
            "Pseudoephedrine": 40000,
            "Chlroquine": 37000,
            "Primaquine": 45000,
            "Antitoksin": 39000,
            "Antibiotik": 45000,
            "Obat Racik": 50000,
            "Cataflam": 40000,
            "Panadol": 13000
        }
# Menunjukkan jadwal telah terisi
jadwal_terisi = set()

def main():
    rumah_sakit = RumahSakitSemogaSehat()
    rumah_sakit.jalankan_program()

if  __name__ == "__main__":
    main()