# Materi Lanjutan Python: Perulangan, Logika Bersarang & Studi Kasus

Dokumen ini berisi materi lanjutan dari dasar pemrograman Python, berfokus pada bagaimana cara membuat program melakukan tugas berulang dan menangani logika yang lebih kompleks.

### Daftar Isi
1.  [Perulangan (for, while)](#1-perulangan-for-while)
2.  [Logika Bersarang (Nested Logic)](#2-logika-bersarang-nested-logic)
3.  [Studi Kasus: Game Tebak Angka](#3-studi-kasus-game-tebak-angka)

---

### 1. Perulangan (for, while)

Perulangan (atau *loop*) digunakan untuk menjalankan blok kode yang sama berulang kali. Ini sangat efisien daripada menulis kode yang sama berkali-kali.

#### Perulangan `for`
`for` loop ideal digunakan ketika kita tahu **berapa kali** kita ingin melakukan perulangan. Biasanya untuk mengiterasi sebuah *sequence* (seperti list, string, atau range angka).

Fungsi `range(stop)` akan menghasilkan urutan angka dari 0 hingga `stop-1`.

**Contoh 1: Mencetak Angka 1 sampai 5**
```python
print("Mulai mencetak angka:")
for i in range(1, 6): # range(1, 6) menghasilkan angka 1, 2, 3, 4, 5
    print(f"Angka ke-{i}")
print("Selesai.")
```

#### Perulangan `while`
`while` loop akan terus berjalan selama sebuah kondisi masih bernilai True. Loop ini cocok digunakan ketika kita tidak tahu pasti berapa kali perulangan akan terjadi.

Peringatan: Hati-hati dengan infinite loop (perulangan tak terbatas)! Pastikan kondisi di dalam while pada akhirnya bisa menjadi False.

**Contoh 1: Mencetak Angka 1 sampai 5**
```python
import time # Mengimpor modul time untuk memberi jeda

hitungan_mundur = 5

while hitungan_mundur > 0:
    print(f"{hitungan_mundur}...")
    hitungan_mundur = hitungan_mundur - 1 # atau hitungan_mundur -= 1
    time.sleep(1) # Jeda 1 detik

print("Meluncur!")
```

### 2. Perulangan Bersarang (Nested Logic)

Perulangan (atau *loop*) digunakan untuk menjalankan blok kode yang sama berulang kali. Ini sangat efisien daripada menulis kode yang sama berkali-kali.

#### Perulangan `for`
Kita bisa meletakkan struktur kontrol (seperti if atau for) di dalam struktur kontrol lainnya. Ini disebut nested logic dan sangat umum digunakan untuk menyelesaikan masalah yang lebih kompleks.


**Contoh 1: if di dalam for (Mencari Angka Ganjil/Genap)**
```python
for angka in range(1, 11):
    # Logika IF ada di dalam loop FOR
    if angka % 2 == 0:
        print(f"{angka} adalah bilangan GENAP")
    else:
        print(f"{angka} adalah bilangan GANJIL")
```

**Contoh 2: for di dalam for (Membuat Tabel Perkalian Sederhana)**
```python
# Loop luar untuk angka pertama (1 sampai 3)
for i in range(1, 4):
    # Loop dalam untuk angka kedua (1 sampai 5)
    for j in range(1, 6):
        hasil = i * j
        print(f"{i} x {j} = {hasil}")
    print("---") # Beri pemisah antar baris
```