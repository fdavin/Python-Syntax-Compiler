# NIM/Nama : 16520405/Fransiskus Davin Anwari
# Tanggal : 11 / 18 /2020
# Deskripsi : Program Menentukan Anagram

# Kamus 
# N1 = int
# N2 = int
# A = list
# B = list
# i = int
# j = int
# k = int
# varsama = int

N1 = int(input("Masukkan banyak bilangan A: "))                        # Memasukkan banyak bilangan yang diinginkan untuk elemen A
A = [0 for i in range (N1)]

for j in range (0,N1):
    A[j] = int(input("Masukkan elemen ke-"+ str(j+1) +": "))           # loop memasukkan elemen dari A

N2 = int(input("Masukkan banyak bilangan B: "))                        # Memasukkan banyak bilangan yang diinginkan untuk elemen B
B = [0 for i in range (N2)]

for j in range (0,N2):
    B[j] = int(input("Masukkan elemen ke-"+ str(j+1) +": "))           # loop memasukkan elemen dari A

varsama = 0             # variabel untuk menghitung jika terdapat elemen yang sama

for j in range (0,N1):                          # loop untuk menambah variabel jika terdapat angka yang sama di A dan B
    for k in range (0,N2):
        if A[j] == B[k]:
            varsama += 1

if N1 > 1:                                      # loop untuk mengurangi variabel jika terdapat angka yang sama di A atau B
    for k in range (0,N2):
        for l in range (k+1,N2):
            if B[k] == B[l]:
                varsama -= 1
    for k in range (0,N1):
        for l in range (k+1,N1):
            if A[k] == A[l]:
                varsama -= 1

if N1 != N2:                                    # menentukan hasil dari perhitungan apakah B adalah anagram A
    print("B bukan anagram A")
elif varsama == N1:
    print("B adalah anagram dari A")
else :
    print("B bukan anagram A")
