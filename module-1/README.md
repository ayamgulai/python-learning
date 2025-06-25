# Dasar Pemrograman Python - Pertemuan 1

Selamat datang di pertemuan pertama belajar dasar-dasar pemrograman dengan Python! Di sesi ini, kita akan menyiapkan semua yang dibutuhkan dan mempelajari konsep paling fundamental.

### Daftar Isi
1.  [Instalasi & Setup Lingkungan](#1-instalasi--setup-lingkungan)
2.  [Tipe Data Dasar](#2-tipe-data-dasar)
3.  [Operator dan Ekspresi](#3-operator-dan-ekspresi)
4.  [Input dan Output](#4-input-dan-output)
5.  [Error Umum dan Debugging Dasar](#5-error-umum-dan-debugging-dasar)
6.  [Latihan & Penjelasan Error](#6-latihan--penjelasan-error)
7.  [Penugasan](#7-penugasan)

---

### 1. Instalasi & Setup Lingkungan

Untuk mulai menulis kode Python, kita butuh dua hal: **Python** itu sendiri dan sebuah **editor teks**.

* **Pilihan A (Offline):** Instal **[Python](https://www.python.org/downloads/)** (jangan lupa centang "Add Python to PATH") dan **[Visual Studio Code](https://code.visualstudio.com/)**. Di VS Code, instal ekstensi "Python" dari Microsoft.
* **Pilihan B (Online):** Gunakan **[Replit](https://replit.com/)**. Cukup daftar, buat "Repl" baru, dan pilih template "Python".

---

### 2. Tipe Data Dasar

Tipe data adalah kategori nilai yang bisa disimpan oleh variabel.

| Tipe Data | Nama | Deskripsi | Contoh |
| :--- | :--- | :--- | :--- |
| `int` | Integer | Bilangan bulat | `umur = 25` |
| `float` | Float | Bilangan desimal | `harga = 15000.50` |
| `str` | String | Teks (diapit `" "` atau `' '`) | `nama = "Budi"` |
| `bool` | Boolean | `True` atau `False` | `is_active = True` |

---

### 3. Operator dan Ekspresi

Operator digunakan untuk melakukan operasi pada nilai.

* **Aritmatika:** `+`, `-`, `*`, `/`, `%` (sisa bagi), `**` (pangkat).
* **Perbandingan:** `==` (sama dengan), `!=` (tidak sama dengan), `>`, `<`.
* **Logika:** `and`, `or`.

Sebuah **ekspresi** adalah kombinasi nilai dan operator yang menghasilkan nilai baru. Contoh: `(10 + 5) * 2`.

---

### 4. Input dan Output

* **Output `print()`:** Menampilkan informasi ke layar.
    ```python
    nama = "Siti"
    print(f"Halo, nama saya {nama}") # f-string adalah cara modern dan mudah
    ```

* **Input `input()`:** Menerima masukan dari pengguna. **PENTING:** `input()` selalu menghasilkan data bertipe **string (`str`)**.
    ```python
    # Meminta nama (hasilnya sudah string, tidak perlu diubah)
    nama_pengguna = input("Masukkan nama Anda: ")

    # Meminta usia dan mengubahnya menjadi integer
    usia_pengguna = int(input("Masukkan usia Anda: "))
    ```

---

### 5. Error Umum dan Debugging Dasar

Error adalah hal yang wajar. Kenali tiga jenis error dasar ini:

1.  **`SyntaxError`**: Aturan penulisan kode dilanggar.
    * **Contoh:** Lupa tanda kurung, kutip, atau titik dua.
    * **Kode Salah:** `print("Halo Dunia` (lupa `)`).
    * **Solusi:** Periksa kembali penulisan kode Anda.

2.  **`TypeError`**: Operasi pada tipe data yang tidak cocok.
    * **Contoh:** Menjumlahkan angka dengan teks.
    * **Kode Salah:** `hasil = 20 + " tahun"`
    * **Solusi:** Pastikan tipe data sesuai. Ubah angka ke string dengan `str(20)` atau sebaliknya.

3.  **`NameError`**: Menggunakan variabel yang belum dibuat atau salah ketik.
    * **Contoh:** Variabel `nama` dipanggil dengan `naama`.
    * **Kode Salah:** `print(naama)`
    * **Solusi:** Periksa kembali ejaan nama variabel.

---

### 6. Latihan & Penjelasan Error

Mari praktikkan konsep di atas dengan membuat program kalkulator luas persegi panjang.

#### Latihan: Kalkulator Luas

1.  Buat program yang meminta pengguna memasukkan **panjang**.
2.  Minta pengguna memasukkan **lebar**.
3.  Ubah kedua input menjadi tipe data angka (`int` atau `float`).
4.  Hitung luasnya dengan rumus `panjang * lebar`.
5.  Cetak hasilnya ke layar dengan format yang jelas.

#### 🚨 Analisis Error yang Mungkin Terjadi pada Latihan Ini

Saat mengerjakan latihan, Anda sangat mungkin akan bertemu salah satu dari error berikut. Memahaminya sekarang akan sangat membantu di masa depan.

* **`TypeError`: can't multiply sequence by non-int of type 'str'**
    * **Artinya:** Anda mencoba mengalikan sesuatu yang bukan angka (dalam hal ini, string).
    * **Penyebab:** Ini adalah error paling umum untuk latihan ini. Ini terjadi karena Anda lupa mengubah hasil dari `input()` menjadi angka. Python tidak tahu cara mengalikan teks "10" dengan teks "5".
    * **Contoh Kode yang Salah:**
        ```python
        panjang = input("Masukkan panjang: ") # Hasilnya adalah string "10"
        lebar = input("Masukkan lebar: ")   # Hasilnya adalah string "5"
        luas = panjang * lebar              # ERROR! Python bingung cara mengalikan teks
        ```
    * **Solusi:** Selalu konversi input yang seharusnya angka menjadi `int()` atau `float()` sebelum melakukan operasi matematika.
        ```python
        panjang = int(input("Masukkan panjang: "))
        lebar = int(input("Masukkan lebar: "))
        luas = panjang * lebar # BERHASIL! 10 * 5 dihitung
        ```

* **`ValueError`: invalid literal for int() with base 10: 'sepuluh'**
    * **Artinya:** Nilai yang Anda coba ubah ke `int` tidak valid.
    * **Penyebab:** Kode konversi Anda (`int(...)`) sudah benar, tetapi pengguna memasukkan input yang bukan angka (misalnya mengetik "sepuluh" bukannya "10").
    * **Contoh Kode yang Benar, tapi Input Salah:**
        ```python
        # Kode ini sudah benar
        panjang = int(input("Masukkan panjang: ")) # Pengguna mengetik "sepuluh"
        # ERROR muncul di baris ini!
        ```
    * **Solusi (Untuk Saat Ini):** Cukup pastikan Anda memasukkan angka yang valid saat menguji program. Penanganan input yang salah dari pengguna akan kita pelajari di materi selanjutnya menggunakan `try-except`.

---

### 7. Penugasan

Untuk memantapkan pemahaman, buatlah sebuah program kalkulator yang melakukan 4 operasi dasar.

**Deskripsi Tugas:**
1.  Buat program yang meminta pengguna memasukkan **dua buah angka**.
2.  Gunakan `float()` untuk konversi tipe data agar program bisa menerima angka desimal (contoh: 15.5).
3.  Lakukan operasi penjumlahan (`+`), pengurangan (`-`), perkalian (`*`), dan pembagian (`/`) pada kedua angka tersebut.
4.  Simpan setiap hasil operasi ke dalam variabel yang berbeda (misal: `hasil_tambah`, `hasil_kurang`, dll).
5.  Tampilkan **semua** hasil perhitungan ke layar dengan format yang jelas dan rapi.

**Contoh Output yang Diharapkan:**
