# MoreOnList__PY
Bahan Ajar Fundamental Pemrograman Python - Penggunaan List dan Memanipulasi Data pada List.<br><br>
<img src="https://github.com/RizkyKhapidsyah/MoreOnList__PY/blob/master/results/001.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/MoreOnList__PY/blob/master/results/002.PNG"><br>
<img src="https://github.com/RizkyKhapidsyah/MoreOnList__PY/blob/master/results/003.PNG"><br><br>
- Lihat <a href="https://github.com/RizkyKhapidsyah/MoreOnList__PY/blob/master/MoreOnList__PY.py">Source Code.</a><br><br>

-----
# List Python

Dalam bahasa pemrograman Python, struktur data yang paling dasar adalah urutan atau lists. Setiap elemen-elemen berurutan akan diberi nomor posisi atau indeksnya. Indeks pertama dalam list adalah nol, indeks kedua adalah satu dan seterusnya. Python memiliki enam jenis urutan built-in, namun yang paling umum adalah list dan tuple. Ada beberapa hal yang dapat Anda lakukan dengan semua jenis list. Operasi ini meliputi pengindeksan, pengiris, penambahan, perbanyak, dan pengecekan keanggotaan. Selain itu, Python memiliki fungsi built-in untuk menemukan panjang list dan untuk menemukan elemen terbesar dan terkecilnya.

-----
# Membuat List Python

List adalah tipe data yang paling serbaguna yang tersedia dalam bahasa Python, yang dapat ditulis sebagai daftar nilai yang dipisahkan koma (item) antara tanda kurung siku. Hal penting tentang daftar adalah item dalam list tidak boleh sama jenisnya. Membuat list sangat sederhana, tinggal memasukkan berbagai nilai yang dipisahkan koma di antara tanda kurung siku. Dibawah ini adalah contoh sederhana pembuatan list dalam bahasa Python. Contoh sederhana pembuatan list pada bahasa pemrograman python

      list1 = ['kimia', 'fisika', 1993, 2017]
      list2 = [1, 2, 3, 4, 5 ]
      list3 = ["a", "b", "c", "d"]

-----
# Akses Nilai Dalam List Python

Untuk mengakses nilai dalam list python, gunakan tanda kurung siku untuk mengiris beserta indeks atau indeks untuk mendapatkan nilai yang tersedia pada indeks tersebut. Berikut adalah contoh cara mengakses nilai di dalam list python :

### Cara mengakses nilai di dalam list Python

      list1 = ['fisika', 'kimia', 1993, 2017]
      list2 = [1, 2, 3, 4, 5, 6, 7 ]

      print ("list1[0]: ", list1[0])
      print ("list2[1:5]: ", list2[1:5])

Setelah Anda mengeksekusi kode diatas, hasilnya akan seperti dibawah ini :

      list1[0]: fisika list2[1:5]: [2, 3, 4, 5]

-----
# Update Nilai Dalam List Python

Anda dapat memperbarui satu atau beberapa nilai di dalam list dengan memberikan potongan di sisi kiri operator penugasan, dan Anda dapat menambahkan nilai ke dalam list dengan metode append (). Sebagai contoh :

      list = ['fisika', 'kimia', 1993, 2017]
      print ("Nilai ada pada index 2 : ", list[2])

      list[2] = 2001
      print ("Nilai baru ada pada index 2 : ", list[2])

-----
# Hapus Nilai Dalam List Python

Untuk menghapus nilai di dalam list python, Anda dapat menggunakan salah satu pernyataan del jika Anda tahu persis elemen yang Anda hapus. Anda dapat menggunakan metode remove() jika Anda tidak tahu persis item mana yang akan dihapus. Sebagai contoh :

### Contoh cara menghapus nilai pada list python

      list = ['fisika', 'kimia', 1993, 2017]

      print (list)
      del list[2]
      print ("Setelah dihapus nilai pada index 2 : ", list)

-----
# Operasi Dasar Pada List Python

List Python merespons operator + dan * seperti string; Itu artinya penggabungan dan pengulangan di sini juga berlaku, kecuali hasilnya adalah list baru, bukan sebuah String. Sebenarnya, list merespons semua operasi urutan umum yang kami gunakan pada String di bab sebelumnya. Dibawah ini adalah tabel daftar operasi dasar pada list python.

<table>
  <thead>
    <tr>
      <th>Python Expression</th>
      <th>Hasil</th>
      <th>Penjelasan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">len([1, 2, 3, 4])</code></td>
      <td><code class="language-plaintext highlighter-rouge">4</code></td>
      <td>Length</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">[1, 2, 3] + [4, 5, 6]</code></td>
      <td><code class="language-plaintext highlighter-rouge">[1, 2, 3, 4, 5, 6]</code></td>
      <td>Concatenation</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">['Halo!'] * 4</code></td>
      <td><code class="language-plaintext highlighter-rouge">['Halo!', 'Halo!', 'Halo!', 'Halo!']</code></td>
      <td>Repetition</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">2 in [1, 2, 3]</code></td>
      <td><code class="language-plaintext highlighter-rouge">	True</code></td>
      <td>Membership</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">for x in [1,2,3] : print (x,end = ' ')</code></td>
      <td><code class="language-plaintext highlighter-rouge">1 2 3</code></td>
      <td>Iteration</td>
    </tr>
  </tbody>
</table>

-----
# Indexing, Slicing dan Matrix Pada List Python

Karena list adalah urutan, pengindeksan dan pengiris bekerja dengan cara yang sama untuk list seperti yang mereka lakukan untuk String. Dengan asumsi input berikut :

      L = ['C++'', 'Java', 'Python']

<table>
  <thead>
    <tr>
      <th>Python Expression</th>
      <th>Hasil</th>
      <th>Penjelasan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">L[2]</code></td>
      <td><code class="language-plaintext highlighter-rouge">'Python'</code></td>
      <td>Offset mulai dari nol</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">L[-2]</code></td>
      <td><code class="language-plaintext highlighter-rouge">'Java'</code></td>
      <td>Negatif: hitung dari kanan</td>
    </tr>
    <tr>
      <td><code class="language-plaintext highlighter-rouge">[1:]</code></td>
      <td><code class="language-plaintext highlighter-rouge">['Java', 'Python']</code></td>
      <td>Slicing mengambil bagian</td>
    </tr>
  </tbody>
</table>

-----
# Method dan Fungsi Build-in Pada List Python

Python menyertakan fungsi built-in sebagai berikut :

<table>
  <thead>
    <tr>
      <th>Python Function</th>
      <th>Penjelasan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>cmp(list1, list2)	#</td>
      <td>Tidak lagi tersedia dengan Python 3</td>
    </tr>
    <tr>
      <td>len(list)</td>
      <td>Memberikan total panjang list.</td>
    </tr>
    <tr>
      <td>max(list)</td>
      <td>Mengembalikan item dari list dengan nilai maks.</td>
    </tr>
    <tr>
      <td>min(list)</td>
      <td>Mengembalikan item dari list dengan nilai min.</td>
    </tr>
    <tr>
      <td>list(seq)</td>
      <td>Mengubah tuple menjadi list.</td>
    </tr>
  </tbody>
</table>

### Python menyertakan methods built-in sebagai berikut

<table>
  <thead>
    <tr>
      <th>Python Methods</th>
      <th>Penjelasan</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>list.append(obj)</td>
      <td>Menambahkan objek obj ke list</td>
    </tr>
    <tr>
      <td>list.count(obj)</td>
      <td>Jumlah pengembalian berapa kali obj terjadi dalam list</td>
    </tr>
    <tr>
      <td>list.extend(seq)</td>
      <td>Tambahkan isi seq ke list</td>
    </tr>
    <tr>
      <td>list.index(obj)</td>
      <td>Mengembalikan indeks terendah dalam list yang muncul obj</td>
    </tr>
    <tr>
      <td>list.insert(index, obj)</td>
      <td>Sisipkan objek obj ke dalam list di indeks offset</td>
    </tr>
    <tr>
      <td>list.pop(obj = list[-1])</td>
      <td>Menghapus dan mengembalikan objek atau obj terakhir dari list</td>
    </tr>
    <tr>
      <td>list.remove(obj)</td>
      <td>Removes object obj from list</td>
    </tr>
    <tr>
      <td>list.reverse()</td>
      <td>Membalik list objek di tempat</td>
    </tr>
    <tr>
      <td>list.sort([func])</td>
      <td>Urutkan objek list, gunakan compare func jika diberikan</td>
    </tr>
  </tbody>
</table>

-----
Referensi Artikel: <a href="https://belajarpython.com">BelajarPython</a>. Thanks to: <a href="https://belajarpython.com">BelajarPython</a><br>
Referensi Source Code: <a href="https://www.youtube.com/user/faqihzamukhlish"> Kelas Terbuka </a> dan <a href="https://github.com/kelasterbuka"> Kelas Terbuka (Repository)</a>. Created by <a href="https://github.com/faqihza">Faqihza Mukhlish.</a> Thanks To: <a href="https://www.youtube.com/channel/UCRGHjysoCemh4y7tCJQs30w/about">Faqihza Mukhlish.</a><br>

-----
All Source Code is Modified.
