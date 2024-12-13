## Langkah - langkah untuk melakukan bedah container dengan beberapa command seperti berikut :
**1. pastikan container berjalan**

### Perintah 
```
docker start -d -p 8080:80 <nama_image or id_image>
```
### Penjelasan Perintah
1. `docker start`: Perintah ini digunakan untuk memulai container yang sudah ada (yang sebelumnya telah dihentikan). Ini tidak digunakan untuk membuat container baru, hanya untuk menjalankan container yang ada.
2. `-d` (Detached mode): Opsi ini membuat container berjalan di latar belakang (background), tanpa menampilkan output langsung di terminal. Container akan berjalan secara "terpisah" sehingga Anda bisa terus menggunakan terminal Anda.
3. `-p` 8080:80 (Port Mapping): Opsi ini digunakan untuk memetakan port pada host ke port di dalam container.
    - 8080 adalah port di host (komputer Anda).
    - 80 adalah port di dalam container.
Artinya, ketika Anda mengakses port 8080 di host, itu akan diarahkan ke port 80 di dalam container (sering digunakan untuk aplikasi web seperti server HTTP).
4. `<nama_image>`: Ini adalah nama atau ID image Docker yang digunakan untuk membuat container.
Jika Anda belum membuat container sebelumnya, perintah ini akan gagal karena container yang dimaksud belum ada. Anda harus menggunakan perintah docker run untuk membuat container pertama kali.

**2. melihat container sudah berjalan :**
### Perintah
```
docker ps -a
```
**bukti**

<img width="862" alt="{6B97B7C7-68FE-4C8D-A522-6651892282D0}" src="https://github.com/user-attachments/assets/1e590163-1bc2-48a1-a52e-89398b3824ea" />

**Penjelasan**:
1. docker ps -a, Fungsi: Menampilkan semua container yang pernah dibuat (baik yang sedang berjalan maupun yang sudah berhenti).
2. `ps`: memeriksa status yang berjalan
3. `a`:untuk melihat semua status
   
