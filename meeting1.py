# Pertemuan 1: Pengenalan Dasar Python

# Cara Instalasi Python:
# 1. Unduh Python dari situs resmi: https://www.python.org/downloads/
#    - Pilih versi Python terbaru sesuai dengan sistem operasi Anda (Windows, macOS, atau Linux).
# 2. Instal Python:
#    - Pada Windows: Jalankan file installer yang diunduh dan centang opsi "Add Python to PATH" saat instalasi.
#    - Pada macOS/Linux: Ikuti instruksi yang ditampilkan.
# 3. Cek apakah instalasi berhasil:
#    - Buka terminal atau command prompt, lalu ketik perintah berikut:
#      python --version
#    - Jika berhasil, Anda akan melihat versi Python yang terinstal.
# 4. Menjalankan Python:
#    - Buka terminal/command prompt, ketik `python` untuk masuk ke mode interaktif.
#    - Untuk menjalankan file Python (.py), ketik `python nama_file.py`.

# 1. Sintaks Dasar
# Python menggunakan indentasi (spasi) untuk mendefinisikan blok kode seperti loop, fungsi, dan kondisi
# Berikut adalah program sederhana yang mencetak 'Hello, World!' ke konsol

print("Hello, World!")  # Ini akan menampilkan: Hello, World!

# 2. Tipe Data di Python
# Python memiliki beberapa tipe data bawaan. Beberapa yang umum adalah:
# Integer, Float, String, dan Boolean

# Integer (int): Angka bulat, tanpa titik desimal
umur = 25  # umur adalah integer

# Float: Angka dengan titik desimal
tinggi = 5.9  # tinggi adalah float

# String (str): Urutan karakter yang diapit oleh tanda kutip
nama = "John Doe"  # nama adalah string

# Boolean (bool): Mewakili nilai True atau False
adalah_mahasiswa = True  # adalah_mahasiswa adalah boolean

# 3. Variabel di Python
# Variabel di Python tidak memerlukan deklarasi tipe. Tipe data akan ditentukan berdasarkan nilai yang diberikan.

# Contoh penugasan variabel:
salam = "Halo"  # salam adalah string

# Variabel dapat diubah menjadi tipe data lain (pengetikan dinamis):
salam = 100  # Sekarang, salam adalah integer

# 4. Input dan Output
# Anda bisa menerima input dari pengguna menggunakan fungsi input(), dan menampilkan hasil menggunakan fungsi print().

# Menerima input dari pengguna
nama_pengguna = input("Siapa nama Anda? ")  # Ini akan meminta nama dari pengguna

# Menampilkan nama pengguna
print("Halo, " + nama_pengguna + "!")  # Menggabungkan string dan menampilkan salam
