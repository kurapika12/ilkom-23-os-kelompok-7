Docker images adalah sekumpulan file yang dipaketkan bersama untuk menyusun dan mendefinisikan aplikasi, dependensinya, serta lingkungan yang dibutuhkan agar aplikasi dapat berjalan. Docker image adalah komponen inti dalam ekosistem Docker dan menjadi pondasi untuk menjalankan container. Image ini merupakan entitas yang bersifat statis, artinya mereka hanya bisa diubah dengan membuat versi baru dari image tersebut. Ketika sebuah Docker Image dijalankan, ia menjadi container, yang bersifat dinamis dan dapat mengeksekusi perintah.
Fungsi Docker Images
Docker Images memiliki beberapa fungsi utama, antara lain:
1. Menyediakan Template untuk Membuat Container
Docker Images adalah dasar untuk membuat container. Container adalah instans dari image yang berjalan, memungkinkan aplikasi untuk dijalankan di dalam lingkungan yang terisolasi.
2. Meningkatkan Portabilitas Aplikasi
Docker Images memungkinkan pengemasan aplikasi beserta semua dependensinya sehingga dapat dijalankan di berbagai sistem tanpa perlu khawatir tentang kompatibilitas perangkat keras atau perangkat lunak.
3. Mendukung Reusabilitas
Setiap Docker Image terdiri dari beberapa layer, dan layer yang sudah ada dapat digunakan kembali oleh image lainnya. Hal ini menghemat ruang penyimpanan dan mempercepat pembangunan image.
4. Versi dan Distribusi Aplikasi
Docker Images memungkinkan pengelolaan versi aplikasi secara mudah. Setiap image dapat diberi tag (contoh: v1.0, latest) untuk melacak perubahan dan distribusinya melalui Docker Hub atau repositori lainnya.
5. Otomatisasi dan Reproducibility
Dengan Docker Images, pengembang dapat mengotomatisasi pembangunan lingkungan pengembangan dan produksi. Karena image bersifat statis, lingkungan yang sama dapat direproduksi dengan konsistensi tinggi, baik di sistem pengembangan, pengujian, maupun produksi.
6. Isolasi Lingkungan Aplikasi
Docker Images menyediakan semua yang diperlukan aplikasi untuk berjalan tanpa dipengaruhi oleh konfigurasi sistem host. Ini memungkinkan beberapa aplikasi dengan konfigurasi berbeda untuk berjalan secara bersamaan di satu mesin.
7. Mendukung CI/CD (Continuous Integration/Continuous Deployment)
Docker Images memungkinkan pengemasan aplikasi untuk pengujian otomatis, pembuatan pipeline, dan deployment cepat di berbagai lingkungan.
8. Mempermudah Skalabilitas
Docker Images mendukung pengelolaan aplikasi skala besar, terutama dalam sistem berbasis microservices. Dengan mudah, aplikasi dapat di-scale up atau di-scale down hanya dengan menjalankan container baru dari image yang sama.

## Perintah Membuat Docker Image dan Penjelasannya
1. Membuat dockerfile terlebih dahulu yang berisi :

FROM caddy:latest

# salin seluruh file index.html kedalam folder caddy
COPY ./index.html /usr/share/caddy/

Salah satu perintah yang paling umum digunakan adalah `docker build`. Berikut adalah contoh dan penjelasan dari perintah tersebut:

### Perintah 
```
docker buid -t <nama_image> .
```

### Penjelasan Perintah
1. `docker build`: Perintah untuk membuat Docker image dari file konfigurasi yang disebut Dockerfile.
2. `-t <nama_image>`: Memberi nama (tag) pada Docker image yang dibuat.
    - `<nama_image>`: Nama yang ingin Anda berikan pada image, seperti : caddy-server.
3. `.`: Menunjukkan lokasi Dockerfile yang digunakan untuk membangun image. Dalam hal ini, . berarti Dockerfile berada di direktori saat ini.

