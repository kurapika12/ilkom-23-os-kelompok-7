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
Berikut Contoh Gambarnya : ![Contoh Penggunaan DockerImage](/ilkom-23-os-kelompok-7/DOCKER/Bukti%20Gambar/DockerImage.png)

## **Menjalankan Container : Menjalankan web berbasis image**

Masukkan perintah : 
```powershell
Docker run -d -p 1234:80 nama_image
```
Berikut Contoh Gambarnya : ![Contoh Penggunaan DockerContainer](/ilkom-23-os-kelompok-7/DOCKER/Bukti%20Gambar/DockerContainer.png)

**Mengakses web yang dijalankan pada localhost dengan port 8080 :**

http://localhost:1234

Berikut Buktinya : ![BuktiDockerRun](/ilkom-23-os-kelompok-7/DOCKER/Bukti%20Gambar/DockerRun.png)

**Cara untuk menghentikan proses container yang sedang berjalan :**

Masukkan Perintah : 
```dockerfile
Docker stop <id_containers or names>
```
Berikut Contoh Gambarnya : ![DockerStop](/ilkom-23-os-kelompok-7/DOCKER/Bukti%20Gambar/DockerStop.png)