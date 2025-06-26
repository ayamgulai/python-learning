# Penugasan 1 

Pada penugasan pertemuan pertama terdapat 3 soal yang dapat dikerjakan untuk mengevaluasi pemahaman dan keterampilan kamu dalam membuat program python. 

1.  [Kalkulator Sederhana](#1-kalkulator-sederhana)
2.  [Game Tebak Angka](#2-game-tebak-angka)

## 1. Kalkulator Sederhana

Buatlah kalkulator sederhana yang melakukan operasi dari dua angka sesuai input user. Terdapat 4 operasi yang dijadikan opsi buat user.

* Penjumlahan
* Pengurangan
* Perkalian
* Pembagian (Catatan : Kamu perlu menambahkan kondisi bahwa pengguna tidak dapat membagi bilangan dengan 0)

_Contoh output yang diharapkan_

```
========KALKULATOR SEDERHANA========
Pilih satu aksi untuk dilakukan
1. Penjumlahan
2. Pengurangan
3. Perkalian
4. Pembagian
Pilih berdasarkan angka (1,2,3,4): 
1 
Masukkan Angka Pertama :
5
Masukkan Angka Kedua : 
8
Hasil : 13
```

## 2. Game Tebak Angka

Buatlah permainan sederhana yang membuat pengguna menebak angka random sebagai target tebakan dari 1 - 100. Kemudian program memberikan clue apakah ini lebih besar atau lebih kecil dari angka target.

_Hint Challenge ini_

Untuk mendapatkan nomor random gunakan code di bawah ini
``` python
import random 

target = random.randint(1,100)
```
_Contoh output yang diharapkan_

```
========GAME TEBAK ANGKA========
Tebak angka dari rentang 1-100 : 
78
Tebakan Terlalu Besar!
24
Tebakan Terlalu Kecil!
50
Selamat, Tebakan Anda Benar!
```