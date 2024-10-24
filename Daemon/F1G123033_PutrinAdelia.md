### MENJALANKAN PROSES DAEMON PADA LARAVEL 10

#### Pengantar
Panduan ini menjelaskan langkah-langkah untuk membuat dan menjalankan proses daemon pada server Laravel, yang akan mempermudah dalam memulai dan menghentikan server Laravel.

#### Langkah-langkah

### 1. Mengambil Proyek Laravel
Untuk mengunduh proyek Laravel yang diinginkan, kamu bisa melakukan cloning dari repositori menggunakan perintah:
```bash
git clone <url_repositori_laravel>
```

### 2. Membuat Skrip Daemon

#### a. Membuat File Skrip
Buat file baru bernama `laravel-daemon.sh` di dalam direktori proyek Laravel menggunakan perintah:
```bash
touch laravel-daemon.sh
```

#### b. Mengedit Skrip
Gunakan editor teks favoritmu (seperti `nano` atau `vim`) untuk membuka file tersebut dan menambahkan kode berikut:
```bash
#!/bin/bash

case "$1" in
    start)
        # Memeriksa apakah server sudah berjalan
        if [ -f laravel.pid ]; then
            echo "Server Laravel sudah berjalan."
            exit 1
        fi

        # Menjalankan server dan menyimpan PID
        nohup php artisan serve > /dev/null 2>&1 &
        echo $! > laravel.pid
        echo "Server Laravel telah dimulai."
        ;;
    stop)
        # Memeriksa apakah file PID tersedia
        if [ -f laravel.pid ]; then
            PID=$(cat laravel.pid)
            kill $PID
            rm laravel.pid
            echo "Server Laravel dihentikan."
        else
            echo "Tidak ada server Laravel yang berjalan."
        fi
        ;;
    *)
        echo "Gunakan perintah: $0 {start|stop}"
        exit 1
        ;;
esac
```

#### c. Memberikan Izin Eksekusi
Jangan lupa untuk memberikan izin eksekusi pada skrip yang telah dibuat menggunakan perintah berikut:
```bash
chmod +x laravel-daemon.sh
```

### 3. Menjalankan atau Menghentikan Server

#### a. Memulai Server
Untuk memulai server Laravel, jalankan skrip dengan perintah:
```bash
./laravel-daemon.sh start
```
**Pesan yang ditampilkan:**
```
Server Laravel telah dimulai.
```

#### b. Menghentikan Server
Jika kamu ingin menghentikan server Laravel, gunakan perintah berikut:
```bash
./laravel-daemon.sh stop
```
**Pesan yang ditampilkan:**
```
Server Laravel dihentikan.
```

### 4. Mengakses Aplikasi Laravel
Setelah server berhasil dijalankan, akses aplikasi Laravel melalui URL:
```
http://localhost:8000
```

### 5. Contoh Tampilan

Berikut ini adalah contoh tampilan saat menjalankan skrip daemon:

**Screenshot Proses Menjalankan Skrip**
![Tampilan Proses](https://drive.google.com/uc?export=view&id=14WWAlwB44ioo9qsHfiSzYyoCMEgr8dwL)

**Screenshot Tampilan Aplikasi Laravel**
![Tampilan Web](https://drive.google.com/uc?export=view&id=14USCVCI9dPjyMRFMfEgT6A5FqW0EH7ne)

Dengan skrip ini, kamu bisa dengan mudah mengelola server Laravel secara daemon di latar belakang.

