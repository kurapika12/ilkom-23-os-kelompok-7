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
**bukti**

<img width="272" alt="{64D9156E-37E5-433D-8470-BE2398F7606D}" src="https://github.com/user-attachments/assets/daafeb63-9fe7-466a-9f9f-7ece1efcb79d" />

**Penjelasan**:
- ls: Perintah ini digunakan untuk menampilkan daftar file dan direktori dalam folder tertentu.
    /etc/caddy: Merujuk pada direktori /etc/caddy di dalam container atau sistem file di host. Direktori ini biasanya digunakan untuk konfigurasi server web Caddy.
    /etc/caddy adalah lokasi default tempat file konfigurasi Caddy disimpan, seperti file Caddyfile yang berisi aturan konfigurasi untuk server web Caddy.
- nama file nya `Caddyfile`

**- lihat isi file:**
### Perintah
```
cat /etc/caddy/Caddyfile
```
**bukti**

<img width="493" alt="{BBD804D4-5FB2-4F6A-BBC7-0F5827B43C68}" src="https://github.com/user-attachments/assets/e5a28243-eed0-4d0f-b6f9-71ba6a74304c" />

**penjelasan**
1. `cat`, Fungsi: melihat isi file konfigurasi Caddyfile yang berada di lokasi /etc/caddy di dalam container.
2. :80: Caddy akan mendengarkan (listening) pada port 80, yang merupakan port standar untuk HTTP. Anda dapat mengganti :80 dengan nama domain Anda, misalnya example.com, jika server Anda sudah memiliki konfigurasi DNS.
3. Opsi ini dikomentari. Jika diaktifkan, Caddy akan bertindak sebagai reverse proxy untuk meneruskan permintaan ke server backend yang berjalan di localhost pada port 8080. Contohnya, jika Anda memiliki aplikasi web berbasis Node.js atau Python Flask
 **- lihat proses yang berjalan:**

### Perintah
```
ps aux
```
**Penjelasan :**
- ps: Perintah ini digunakan untuk menampilkan daftar proses yang sedang berjalan di sistem.
- a: Menampilkan proses dari semua pengguna.
- u: Menampilkan informasi proses dalam format yang lebih user-friendly, termasuk nama pengguna yang menjalankan proses.
- x: Menampilkan proses yang tidak terkait dengan terminal (misalnya, daemon atau proses latar belakang).

**3. Keluar dari container:**
### Perintah
```
exit
```

## Kesimpulan
Docker Container adalah teknologi yang memungkinkan pengemasan aplikasi beserta semua dependensinya agar dapat dijalankan secara konsisten di berbagai lingkungan. Dengan fungsi-fungsi seperti portabilitas, efisiensi, dan pengelolaan aplikasi yang mudah, Docker telah menjadi bagian penting dari pengembangan perangkat lunak modern. Perintah docker exec -it caddy-container /bin/sh memungkinkan kita untuk masuk ke dalam container secara interaktif dan menjalankan perintah Linux, sedangkan ps aux dan ls /etc/caddy berguna untuk memeriksa proses yang berjalan dan konfigurasi dalam container. Dengan cara ini, pengelolaan dan eksplorasi container dapat dilakukan dengan lebih fleksibel dan efisien.

