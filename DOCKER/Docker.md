# Dokumentasi Penggunaan Docker dengan Web Server Caddy

**Pendahuluan**

**Membangun Image : Menggunakan File Bernama Dockerfile**

Contoh Dockerfile [Dockerfile](/ilkom-23-os-kelompok-7/DOCKER/dockerfile)

Lalu bangun Image dengan perintah :
Docker build -t nama_image .

**Menjalankan Container : Menjalankan web berbasis image**

Masukkan perintah : Docker run -d -p 8080:80 nama_image


**Mengakses web yang dijalankan pada localhost dengan port 8080 :**

http://localhost:8080

**Cara untuk menghentikan proses container yang sedang berjalan :**

Masukkan Perintah : Docker stop id_containers or names

