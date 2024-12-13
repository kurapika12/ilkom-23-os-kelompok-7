# Dokumentasi Penggunaan Docker dengan Web Server Caddy

**Pendahuluan**

## **Membangun Image : Menggunakan File Bernama Dockerfile**
Untuk memulai dengan Docker, langkah pertama adalah inisiasi image. Berikut langkah-langkahnya:
1. Buat sebuah folder untuk menyimpan file Dockerfile dan file index.
2. Di dalam folder tersebut buat **Dockerfile**
Contoh **Dockerfile** [Dockerfile](/ilkom-23-os-kelompok-7/DOCKER/dockerfile)

## **Lalu bangun Image dengan perintah :**
```powershell
Docker build -t nama_image .
```
Berikut Contoh Gambarnya : 

## **Menjalankan Container : Menjalankan web berbasis image**

Masukkan perintah : 
```powershell
Docker run -d -p 8080:80 nama_image
```
Berikut Contoh Gambarnya :

**Mengakses web yang dijalankan pada localhost dengan port 8080 :**

http://localhost:8080

**Cara untuk menghentikan proses container yang sedang berjalan :**

Masukkan Perintah : 
```dockerfile
Docker stop <id_containers or names>
```
Berikut Contoh Gambarnya