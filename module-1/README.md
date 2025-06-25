# Pertemuan 1: Fondasi Python

Pada pertemuan ini, kita akan membangun fondasi yang kuat untuk memulai perjalanan Anda dengan Python.

### Tujuan
- Mengerti cara kerja variabel dan tipe data dasar.
- Mampu melakukan operasi matematika sederhana.
- Bisa membuat program yang berinteraksi dengan pengguna melalui input dan output.

### Materi
1.  **Variabel**: Wadah untuk menyimpan nilai.
    ```python
    nama = "Budi"
    umur = 20
    ```
2.  **Tipe Data**: Jenis nilai yang bisa disimpan.
    - `string`: Teks (diapit `"` atau `'`).
    - `integer`: Bilangan bulat (contoh: `10`, `100`).
    - `float`: Bilangan desimal (contoh: `3.14`, `99.5`).
    - `boolean`: Nilai kebenaran (`True` atau `False`).

3.  **Input & Output**: Berkomunikasi dengan program.
    ```python
    # Menampilkan data ke layar
    print("Halo Dunia")

    # Meminta input dari pengguna
    nama_pengguna = input("Masukkan nama Anda: ")
    print("Halo,", nama_pengguna)
    ```
4.  **Operator & Konversi Tipe Data**: Melakukan kalkulasi.
    `input()` selalu menghasilkan `string`. Untuk matematika, kita harus mengubahnya ke `int()` atau `float()`.
    ```python
    angka_str = input("Masukkan angka: ") # Hasilnya string
    angka_int = int(angka_str)            # Diubah menjadi integer
    hasil = angka_int * 2
    print("Hasilnya adalah:", hasil)
    ```

### Latihan & Tugas
- **Demo**: Kita akan membuat [Kalkulator Kasir Sederhana](./demo/kasir_sederhana.py).
