## Langkah - langkah untuk melakukan beberapa command dalam container

**1. Masuk ke dalam container secara interaktif:**

### Perintah 
```
docker exec -it caddy-container /bin/sh
```
### Penjelasan Perintah
    1. `docker exec`: Menjalankan perintah di dalam container.
    2. `-it` : Membuat sesi interaktif.
    3. `/bin/sh` : Menggunakan shell untuk masuk ke container.

**2. Lakukan eksplorasi atau menjalankan command Linux:**

    **-Cek file dalam container:**

### Perintah
```
ls /etc/caddy

```
**Penjelasan**:
- ls: Perintah ini digunakan untuk menampilkan daftar file dan direktori dalam folder tertentu.
    /etc/caddy: Merujuk pada direktori /etc/caddy di dalam container atau sistem file di host. Direktori ini biasanya digunakan untuk konfigurasi server web Caddy.
    /etc/caddy adalah lokasi default tempat file konfigurasi Caddy disimpan, seperti file Caddyfile yang berisi aturan konfigurasi untuk server web Caddy.

    **- Cek file dalam container:**

### Perintah
```
ps aux
```
**Penjelasan :**
- ps: Perintah ini digunakan untuk menampilkan daftar proses yang sedang berjalan di sistem.
- a: Menampilkan proses dari semua pengguna.
- u: Menampilkan informasi proses dalam format yang lebih user-friendly, termasuk nama pengguna yang menjalankan proses.
- x: Menampilkan proses yang tidak terkait dengan terminal (misalnya, daemon atau proses latar belakang).


