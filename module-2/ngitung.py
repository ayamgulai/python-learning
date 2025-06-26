import time # Mengimpor modul time untuk memberi jeda

hitungan_mundur = 5

while hitungan_mundur > 0:
    print(f"{hitungan_mundur}...")
    hitungan_mundur = hitungan_mundur - 1 # atau hitungan_mundur -= 1
    time.sleep(1) # Jeda 1 detik

print("Meluncur!")
print(time.localtime)