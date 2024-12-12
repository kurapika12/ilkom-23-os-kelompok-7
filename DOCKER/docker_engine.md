# Pengertian Docker Engine
Docker Engine adalah platform perangkat lunak yang memungkinkan pengembang untuk membangun, menjalankan, dan mengelola container. Docker Engine bertindak sebagai mesin runtime untuk membuat dan menjalankan container di atas sistem operasi host. Dengan Docker Engine, pengembang dapat membuat aplikasi yang ringan, portabel, dan dapat dijalankan secara konsisten di berbagai lingkungan.

Docker Engine terdiri dari tiga komponen utama:
1. **Server (Docker Daemon)**: Ini adalah proses latar belakang yang bertanggung jawab untuk membuat, menjalankan, dan mengelola container Docker.
2. **REST API**: API yang memungkinkan aplikasi untuk berkomunikasi dengan daemon Docker dan mengeluarkan perintah.
3. **CLI (Command Line Interface)**: Alat baris perintah yang memungkinkan pengembang untuk berinteraksi dengan Docker melalui terminal.

---

## Fungsi Docker Engine
1. **Pembuatan Container**: Docker Engine memungkinkan pembuatan container dari image Docker yang telah ditentukan.
2. **Pengelolaan Container**: Docker Engine memungkinkan pengelolaan container yang berjalan, seperti memulai, menghentikan, atau menghapus container.
3. **Portabilitas Aplikasi**: Aplikasi yang dikemas dalam container dapat berjalan di berbagai lingkungan tanpa perlu penyesuaian tambahan.
4. **Pengelolaan Image**: Docker Engine memungkinkan pengunduhan (pull) dan pengunggahan (push) image ke dan dari Docker Hub atau registry pribadi.
5. **Pengelolaan Volume dan Jaringan**: Docker Engine memungkinkan pengelolaan volume penyimpanan dan jaringan untuk container agar aplikasi dapat berbagi data atau berkomunikasi satu sama lain.

---

## Tujuan Docker Engine
1. **Portabilitas**: Membuat aplikasi dapat berjalan di berbagai lingkungan tanpa memerlukan konfigurasi tambahan.
2. **Isolasi**: Setiap container berjalan secara terisolasi dari satu sama lain dan dari host, memungkinkan pengelolaan sumber daya yang lebih baik.
3. **Efisiensi**: Memanfaatkan sumber daya sistem secara efisien dibandingkan dengan mesin virtual.
4. **Kemudahan Pengembangan**: Mempercepat pengembangan dan pengujian aplikasi dengan menyediakan lingkungan yang konsisten.
5. **Otomatisasi**: Mendukung otomatisasi pembuatan, pengujian, dan penyebaran aplikasi.

---

## Contoh Perintah Docker Engine dan Penjelasannya
Berikut beberapa perintah umum Docker Engine beserta penjelasannya:

### 1. **Perintah Menjalankan Container**
```
docker run -d -p 8080:80 nginx
```
**Penjelasan:**
- **`docker run`**: Perintah untuk membuat dan menjalankan container dari image Docker.
- **`-d`**: Menjalankan container dalam mode *detached* (latar belakang), sehingga terminal tetap dapat digunakan.
- **`-p 8080:80`**: Memetakan port 80 pada container ke port 8080 di host. Ini memungkinkan akses ke aplikasi di container melalui `http://localhost:8080`.
- **`nginx`**: Nama image yang digunakan untuk membuat container.

### 2. **Perintah Melihat Container yang Sedang Berjalan**
```
docker ps
```
**Penjelasan:**
- **`docker ps`**: Menampilkan daftar container yang sedang berjalan beserta informasi seperti ID container, image, waktu mulai, dan port yang digunakan.

### 3. **Perintah Menghentikan Container**
```
docker stop <container_id>
```
**Penjelasan:**
- **`docker stop`**: Menghentikan container yang sedang berjalan.
- **`<container_id>`**: ID unik dari container yang ingin dihentikan. ID ini dapat ditemukan dengan perintah `docker ps`.

### 4. **Perintah Menghapus Container**
```
docker rm <container_id>
```
**Penjelasan:**
- **`docker rm`**: Menghapus container yang telah dihentikan dari sistem.
- **`<container_id>`**: ID unik dari container yang ingin dihapus. ID ini bisa diperoleh dari `docker ps -a`.

### 5. **Perintah Mengunduh Image dari Docker Hub**
```
docker pull nginx
```
**Penjelasan:**
- **`docker pull`**: Mengunduh image Docker dari Docker Hub atau registry lain.
- **`nginx`**: Nama image yang diunduh.

### 6. **Perintah Melihat Image yang Ada di Host**
```
docker images
```
**Penjelasan:**
- **`docker images`**: Menampilkan daftar image Docker yang telah diunduh ke sistem.

### 7. **Perintah Menghapus Image**
```
docker rmi nginx
```
**Penjelasan:**
- **`docker rmi`**: Menghapus image Docker dari sistem.
- **`nginx`**: Nama atau ID dari image yang ingin dihapus.

### 8. **Perintah Melihat Log dari Container**
```
docker logs <container_id>
```
**Penjelasan:**
- **`docker logs`**: Menampilkan log yang dihasilkan oleh container.
- **`<container_id>`**: ID unik dari container yang ingin dilihat lognya.

### 9. **Perintah Mengeksekusi Perintah di Dalam Container**
```
docker exec -it <container_id> bash
```
**Penjelasan:**
- **`docker exec`**: Mengeksekusi perintah di dalam container yang sedang berjalan.
- **`-it`**: Memberikan akses ke terminal interaktif (interactive terminal).
- **`<container_id>`**: ID dari container tempat kita ingin menjalankan perintah.
- **`bash`**: Memulai shell bash di dalam container.

---

## Kesimpulan
Docker Engine adalah mesin runtime yang memungkinkan pembuatan dan pengelolaan container secara efisien. Dengan menggunakan perintah Docker Engine, pengembang dapat membuat, menjalankan, menghentikan, dan mengelola container dengan mudah. Docker Engine memainkan peran penting dalam pengembangan perangkat lunak modern dengan menyediakan isolasi aplikasi, portabilitas, dan efisiensi penggunaan sumber daya.
