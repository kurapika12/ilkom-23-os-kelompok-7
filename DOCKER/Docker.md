# Dokumentasi Penggunaan Docker dengan Web Server Caddy

**Pendahuluan**

**Membangun Image : Menggunakan File Bernama Dockerfile**

Contoh Dockerfile [Dockerfile](/ilkom-23-os-kelompok-7/DOCKER/dockerfile)

Lalu bangun Image dengan perintah :
Docker build -t nama_image .

**Menjalankan Container : Menjalankan aplikasi berbasis image**

Masukkan perintah : Docker run -d -p 8080:80 nama_image


