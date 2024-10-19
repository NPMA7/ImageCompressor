# Kompresor Gambar

Proyek ini adalah aplikasi web untuk mengompres gambar menggunakan Python dan Flask. Aplikasi ini memungkinkan pengguna untuk mengunggah gambar dan mengompresnya sesuai dengan kualitas yang diinginkan.

## Tata Cara Penggunaan

Berikut adalah langkah-langkah untuk menggunakan aplikasi kompresor gambar:

### 1. Persyaratan

Pastikan Anda memiliki Python 3.x terinstal di sistem Anda. Anda juga perlu menginstal beberapa dependensi yang diperlukan:

```bash
pip install Flask opencv-python
```

### 2. Instalasi

1. **Clone Repositori**

   ```bash
   git clone <URL_REPOSITORI>
   cd <NAMA_FOLDER>

## Menggunakan Aplikasi

### 1. Unggah Gambar

- Klik pada tombol **"Pilih gambar"** untuk membuka dialog file.
- Pilih satu atau beberapa gambar yang ingin Anda kompres.

### 2. Tentukan Kualitas Kompresi

- Di kolom **"Kualitas gambar (1-100)"**, masukkan nilai antara 1 (kualitas rendah) hingga 100 (kualitas tinggi). Nilai default adalah **20**.

### 3. Kompres Gambar

- Klik tombol **"Kompres"** untuk memulai proses kompresi.
- Selama proses berlangsung, animasi pemuatan akan ditampilkan.

### 4. Lihat Hasil

- Setelah kompresi selesai, gambar yang telah dikompres akan ditampilkan di bawah formulir.
- Anda dapat mengklik gambar untuk melihatnya dalam ukuran yang lebih besar.

### 5. Di Mana Hasil Kompres Disimpan?

- Gambar yang telah dikompres disimpan di folder **`result`**, yang berada di dalam direktori proyek Anda.
- Gambar akan memiliki nama yang sama dengan file aslinya, sehingga Anda dapat dengan mudah mengidentifikasi hasil kompresi.
