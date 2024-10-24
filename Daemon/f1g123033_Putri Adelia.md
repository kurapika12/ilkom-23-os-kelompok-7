Berikut revisi skrip dengan urutan link yang sesuai:

---

# MENGOPERASIKAN PROSES DAEMON DI LARAVEL 10

## Penjelasan
Dokumentasi ini menguraikan cara membuat dan menggunakan skrip sederhana untuk mengelola server Laravel sebagai proses daemon.

## Langkah-langkah

### 1. Clone Proyek Laravel
Salin proyek Laravel dari repositori lain menggunakan perintah berikut:
```bash
git clone <repositori_anda>
```

### 2. Membuat Skrip Daemon

#### a. Buat File Bash Script
Buat file baru dengan nama `laravel-daemon.sh` menggunakan perintah:
```bash
touch laravel-daemon.sh
```

#### b. Edit Skrip Bash
Buka file `laravel-daemon.sh` di editor teks pilihan Anda (misalnya `nano`, `vim`, atau yang lainnya).

#### c. Salin Kode Skrip
Tempelkan kode berikut ke dalam file:
```bash
#!/bin/bash

case "$1" in
    start)
        # Memeriksa apakah server sudah berjalan
        if [ -f laravel.pid ]; then
            echo "Server Laravel sudah berjalan."
            exit 1
        fi

        # Menjalankan server dan menyimpan PID ke file
        nohup php artisan serve > /dev/null 2>&1 &
        echo $! > laravel.pid
        echo "Server Laravel dimulai."
        ;;
    stop)
        # Memeriksa apakah file PID ada
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
        echo "Gunakan: $0 {start|stop}"
        exit 1
        ;;
esac
```

#### d. Izin Eksekusi
Berikan izin eksekusi untuk skrip dengan menjalankan perintah:
```bash
chmod +x laravel-daemon.sh
```

### 3. Mengelola Server Laravel

#### a. Menjalankan Server
Untuk memulai server Laravel, gunakan perintah berikut:
```bash
./laravel-daemon.sh start
```
**Output yang akan muncul:**
```
Server Laravel dimulai.
```

#### b. Menghentikan Server
Untuk menghentikan server Laravel, gunakan perintah berikut:
```bash
./laravel-daemon.sh stop
```
**Output yang akan muncul:**
```
Server Laravel dihentikan.
```

### 4. Akses Aplikasi Laravel
Setelah server berhasil dijalankan, buka browser dan akses:
```
http://localhost:8000
```

### 5. Screenshots
Berikut adalah tampilan dari proses menjalankan skrip:

#### Proses Menjalankan Skrip
![Menjalankan Skrip](https://drive.google.com/uc?export=view&id=14USCVCI9dPjyMRFMfEgT6A5FqW0EH7ne)

#### Tampilan Web
![Tampilan Web Laravel](https://drive.google.com/uc?export=view&id=14WWAlwB44ioo9qsHfiSzYyoCMEgr8dwL)

---
