# Python Lanjutan: Struktur Data, Fungsi, OOP, dan Modularisasi

Selamat datang di materi Python tingkat lanjut! Setelah menguasai dasar-dasar, kini saatnya kita mempelajari cara membangun program yang lebih terstruktur, efisien, dan mudah dikelola.

### Daftar Isi
1.  [Fungsi (Function)](#1-fungsi-function)
2.  [Struktur Data Utama](#2-struktur-data-utama)
3.  [Object-Oriented Programming (OOP)](#3-object-oriented-programming-oop)
4.  [Modularisasi](#4-modularisasi)
5.  [Proyek Akhir: Manajemen Kontak](#5-proyek-akhir-manajemen-kontak)

---

### 1. Fungsi (Function)

Fungsi adalah blok kode yang dapat digunakan kembali untuk melakukan tugas tertentu. Menggunakan fungsi membuat kode lebih rapi, mudah dibaca, dan tidak berulang (prinsip DRY: *Don't Repeat Yourself*).

* **Mendefinisikan Fungsi:** Menggunakan kata kunci `def`.
* **Parameter:** Input yang bisa diterima oleh fungsi.
* **`return`:** Kata kunci untuk mengembalikan sebuah nilai dari fungsi.

```python
# Fungsi sederhana tanpa parameter
def sapa_dunia():
    print("Halo, Dunia!")

# Fungsi dengan parameter dan nilai kembali (return)
def hitung_luas_persegi(sisi):
    luas = sisi * sisi
    return luas

# Memanggil fungsi
sapa_dunia() # Output: Halo, Dunia!

panjang_sisi = 10
hasil_luas = hitung_luas_persegi(panjang_sisi)
print(f"Luas persegi dengan sisi {panjang_sisi} adalah {hasil_luas}") # Output: 100
```

## 2. Struktur Data Utama

Struktur data adalah cara menyimpan dan mengorganisir sekumpulan data. Python menyediakan beberapa tipe bawaan yang sangat kuat.

### List

[Lihat selengkapnya di W3Schools](https://www.w3schools.com/python/python_lists.asp)

Kumpulan item yang terurut, dapat diubah (**mutable**), dan memperbolehkan item duplikat. Dibuat dengan kurung siku `[]`.

```python
# List berisi nama-nama buah
buah = ["apel", "jeruk", "mangga", "apel"]

# Mengakses item berdasarkan indeks (dimulai dari 0)
print(f"Buah pertama: {buah[0]}") # Output: apel

# Mengubah item
buah[1] = "anggur"

# Menambah item baru
buah.append("pisang")

print(f"List buah sekarang: {buah}") # Output: ['apel', 'anggur', 'mangga', 'apel', 'pisang']
```

### Dictionary (Dict)

[Lihat selengkapnya di W3Schools](https://www.w3schools.com/python/python_dictionaries.asp)

Kumpulan pasangan `kunci:nilai` (`key:value`) yang tidak terurut (di versi Python lama) dan dapat diubah (mutable). Kunci harus unik. Dibuat dengan kurung kurawal `{}`.

```py
# Dictionary data mahasiswa
mahasiswa = {
    "nama": "Budi Hartono",
    "nim": "12345",
    "jurusan": "Informatika"
}

# Mengakses nilai berdasarkan kunci
print(f"Nama Mahasiswa: {mahasiswa['nama']}") # Output: Budi Hartono

# Menambah atau mengubah data
mahasiswa['semester'] = 3
mahasiswa['nama'] = "Budi H."

print(f"Data mahasiswa sekarang: {mahasiswa}")
```

### Struktur Data Lainnya

* [Tuple](https://www.w3schools.com/python/python_tuples.asp) : Mirip seperti list tapi tidak dapat diubah (immutable). Dibuat dengan kurung biasa (). Cocok untuk data yang tidak seharusnya berubah, seperti koordinat. Contoh: koordinat = (10, -5).
* [Set](https://www.w3schools.com/python/python_sets.asp): Kumpulan item yang unik (tidak ada duplikasi) dan tidak terurut. Dibuat dengan {} tapi tanpa key:value. Berguna untuk operasi himpunan (gabungan, irisan). Contoh: angka_unik = {1, 2, 3, 2, 1} akan menjadi {1, 2, 3}.
* [Array](https://www.w3schools.com/python/python_arrays.asp): Mirip list, tapi hanya bisa menyimpan item dengan tipe data yang sama dan lebih efisien dalam penggunaan memori. Perlu mengimpor dari modul array. Umumnya, list sudah cukup untuk sebagian besar kebutuhan.


## 3. Object-Oriented Programming (OOP)

OOP adalah paradigma pemrograman yang mengorganisir kode dengan membuat "objek". Objek ini memiliki data (atribut) dan perilaku (metode/fungsi).

* Class: Sebuah "cetakan" atau blueprint untuk membuat objek.
* Object: Sebuah instance atau wujud nyata dari sebuah class.
* `__init__`: Metode khusus (konstruktor) yang dijalankan saat sebuah objek dibuat.
* `self`: Merujuk pada objek itu sendiri di dalam class.

Contoh : membuat Class Mobil

```py
# Membuat 'cetakan' mobil
class Mobil:
    # Konstruktor: dijalankan saat objek Mobil dibuat
    def __init__(self, merk, warna, tahun):
        self.merk = merk    # ini adalah atribut
        self.warna = warna  # ini adalah atribut
        self.tahun = tahun  # ini adalah atribut
        self.kecepatan = 0  # kecepatan awal

    # Metode: fungsi yang dimiliki oleh objek
    def percepat(self, tambahan_kecepatan):
        self.kecepatan += tambahan_kecepatan
        print(f"{self.merk} melaju dengan kecepatan {self.kecepatan} km/jam.")

    def info(self):
        print(f"Info Mobil: {self.tahun} {self.merk} berwarna {self.warna}.")

# Membuat dua objek mobil dari class yang sama
mobil_saya = Mobil("Toyota", "Merah", 2022)
mobil_teman = Mobil("Honda", "Hitam", 2023)

# Memanggil metode dari masing-masing objek
mobil_saya.info()
mobil_saya.percepat(60)

mobil_teman.info()
mobil_teman.percepat(80)
```

## 4. Modularisasi

Seiring program menjadi besar, menyimpan semua kode dalam satu file menjadi tidak praktis. Modularisasi adalah praktik memecah kode ke dalam beberapa file (modul) yang logis.

Kita bisa mengimpor fungsi, variabel, atau class dari satu file ke file lainnya menggunakan `import`.

Langkah-langkah:

1. Buat file modul, misalnya `kalkulator.py`:
    ```py
    # File: kalkulator.py
    PI = 3.14159

    def tambah(a, b):
        return a + b

    def kurang(a, b):
        return a - b
    ```

2. Buat file utama yang akan menggunakan modul tersebut, misalnya `main.py`:
    ```py
    # File: main.py

    # Impor seluruh modul kalkulator
    import kalkulator

    # Impor hanya item tertentu dari modul
    from kalkulator import PI

    hasil_tambah = kalkulator.tambah(10, 5)
    print(f"Hasil penjumlahan: {hasil_tambah}")
    print(f"Nilai PI yang diimpor: {PI}")
    ```

## 5. Proyek Akhir: Manajemen Kontak
Untuk menyatukan semua konsep, buatlah sebuah sistem manajemen kontak sederhana.


* Modularisasi: Buat dua file:
    * kontak.py: Berisi class untuk kontak.
    * app.py: Berisi logika utama aplikasi untuk berinteraksi dengan pengguna.

* OOP: Di kontak.py, buat class Kontak yang memiliki atribut nama dan nomor_telepon.

* Struktur Data: Di app.py, gunakan sebuah list untuk menyimpan semua objek Kontak yang telah dibuat.

* Fungsi: Di app.py, buat fungsi-fungsi berikut:
    * `tambah_kontak()`: Meminta input nama dan nomor, membuat objek Kontak baru, lalu menyimpannya ke dalam list.
    * `tampilkan_semua_kontak()`: Melakukan perulangan pada list kontak dan mencetak info setiap kontak.
    * `cari_kontak(nama)`: Mencari kontak berdasarkan nama dan menampilkan detailnya jika ditemukan.

Program utama Anda di app.py akan menjadi menu sederhana yang terus berjalan (menggunakan while loop) dan memanggil fungsi-fungsi di atas berdasarkan input pengguna. 
