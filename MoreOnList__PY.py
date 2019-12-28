
print('=' * 3, "CONTOH 1", '=' * 3)
Negara = ['Indonesia', 'Amerika', 'Inggris', 'Belanda']
print(Negara)

# Beberapa Method Yang Bisa Digunakan Untuk Memanipulasi List Di Atas
Negara.append('Rusia') # menambah data ke dalam list dan meletakkannya ke urutan paling belakang
print(Negara)

Negara.extend('Maroko') # menambah data ke dalam list dan meletakkannya ke urutan paling belakang namun dengan menampilkan per karakter
print(Negara)

Negara.insert(2, 'Sudan') # Menyisipkan data ke dalam list dan meletakkannya ke index urutan tertentu (contoh dalam hal ini adalah urusan ke 3 (index ke 2 dari array)
print(Negara)

Negara.remove('Amerika') # Menghapus Data tertentu (dalam hal ini contoh: menghapus data Amerika dari list)
print(Negara)

Negara.reverse() # Membalikkan urutan data (termasuk data yang di extend)
print(Negara)

# Method Untuk Menghitung Jumlah Data Tertentu
JumlahDataTertentu = Negara.count('Inggris')
print("Jumlah Data Yang Dimaksud ada di dalam list sebanyak : ", JumlahDataTertentu, 'buah data')

print('\n')

print('=' * 3, "CONTOH 2", '=' * 3)
A = Negara.copy()
A.append('Spanyol')
print(A)
print(Negara)

print('\n')

print('=' * 3, "CONTOH 3", '=' * 3)
Nama = "Rizky Khapidsyah"
print(Nama[7] + '\n')

for i in Nama:
    print(i)
    print(Nama[7])



