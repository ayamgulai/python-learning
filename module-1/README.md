
# Pertemuan 1: Fondasi Python - Instalasi dan Konsep Dasar

Pada pertemuan ini, kita akan membangun fondasi yang kuat untuk memulai perjalanan Anda dengan Python. Di akhir sesi, Anda akan bisa menulis program sederhana yang berinteraksi dengan pengguna.

### 1. Instalasi Python & Visual Studio Code

Sebelum mulai, kita perlu menyiapkan "alat tempur" kita.

**A. Instalasi Python**
1.  Kunjungi situs resmi Python: [python.org/downloads/](https://www.python.org/downloads/)
2.  Unduh versi Python terbaru.
3.  Jalankan installer. **PENTING:** Pada jendela instalasi pertama, centang kotak yang bertuliskan **"Add Python to PATH"**.
4.  Lanjutkan instalasi hingga selesai.

**B. Instalasi Visual Studio Code (VS Code)**
1.  Kunjungi situs resmi VS Code: [code.visualstudio.com/](https://code.visualstudio.com/)
2.  Unduh dan install VS Code.
3.  Setelah terinstal, buka VS Code, buka menu **Extensions** (ikon balok di sisi kiri), cari dan install ekstensi bernama **"Python"** dari Microsoft.

### 2. Menjalankan Kode Python Pertama Anda
1.  Buat folder baru di komputer Anda untuk menyimpan semua proyek kursus ini.
2.  Buka VS Code, lalu buka folder tersebut melalui `File > Open Folder...`.
3.  Buat file baru dengan nama `hello.py`.
4.  Ketik kode berikut di dalam file `hello.py`:
    ```python
    print("Hello, World!")
    ```
5.  Untuk menjalankannya, buka Terminal di VS Code (`View > Terminal` atau `Ctrl+``), lalu ketik perintah:
    ```bash
    python hello.py
    ```
6.  Anda akan melihat teks `Hello, World!` muncul di terminal.

### 3. Pengenalan Variabel dan Tipe Data
**Variabel** adalah sebuah nama yang kita berikan pada sebuah "wadah" untuk menyimpan data.

Setiap nilai memiliki **Tipe Data** yang menentukan jenisnya:
-   **`String`** (str): Teks. Diapit oleh tanda kutip (`"` atau `'`).
    ```python
    alamat = "Jalan Merdeka No. 17"
    ```
-   **`Integer`** (int): Bilangan bulat.
    ```python
    jumlah_siswa = 30
    ```
-   **`Float`**: Bilangan desimal.
    ```python
    indeks_prestasi = 3.85
    ```
-   **`Boolean`** (bool): Nilai kebenaran, `True` atau `False`.
    ```python
    sedang_hujan = False
    ```

### 4. Operator Aritmatika
Digunakan untuk melakukan operasi matematika.

| Operator | Nama             | Contoh (`a=10`, `b=3`) | Hasil |
| :------: | :--------------- | :-------------------- | :---: |
|   `+`    | Penjumlahan      | `a + b`               | `13`  |
|   `-`    | Pengurangan      | `a - b`               | `7`   |
|   `*`    | Perkalian        | `a * b`               | `30`  |
|   `/`    | Pembagian        | `a / b`               | `3.33`|
|   `%`    | Modulus          | `a % b`               | `1`   |
|   `**`   | Pangkat          | `a ** b`              | `1000`|
|   `//`   | Pembagian Bulat  | `a // b`              | `3`   |

### 5. Fungsi Input dan Output
-   **Output: `print()`**: Menampilkan informasi ke layar.
    ```python
    nama = "Ani"
    print(f"Halo, nama saya adalah {nama}") # f-string direkomendasikan
    ```
-   **Input: `input()`**: Meminta masukan dari pengguna. **PENTING:** `input()` selalu menghasilkan data bertipe `string`!
    ```python
    nama_pengguna = input("Siapa nama Anda? ")
    ```

### 6. Konversi Tipe Data (Type Casting)
Karena `input()` menghasilkan `string`, kita harus mengubahnya jika ingin melakukan operasi matematika.
```python
tahun_lahir_str = input("Tahun berapa Anda lahir? ")
tahun_lahir_int = int(tahun_lahir_str) # Konversi ke integer
umur = 2025 - tahun_lahir_int
print(f"Umur Anda sekarang sekitar {umur} tahun.")
