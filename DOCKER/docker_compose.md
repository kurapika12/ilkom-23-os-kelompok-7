## Perintah Docker Compose dan Penjelasannya

Docker Compose adalah alat yang memungkinkan pengembang untuk mendefinisikan dan menjalankan aplikasi multi-container. Docker Compose menggunakan file `docker-compose.yml` untuk mengonfigurasi layanan, jaringan, dan volume container dalam satu file terpusat.

### Contoh File `docker-compose.yml`
```yaml
version: '3'
services:
  web:
    image: nginx
    ports:
      - "8080:80"
```

### Penjelasan File `docker-compose.yml`
1. **`version: '3'`**: Menentukan versi file Docker Compose yang digunakan.
2. **`services`**: Bagian ini mendefinisikan layanan yang akan dijalankan.
3. **`web`**: Nama layanan. Layanan ini akan diberi nama `web` di dalam lingkungan Docker.
4. **`image: nginx`**: Menentukan image yang akan digunakan, dalam hal ini image `nginx`.
5. **`ports: "8080:80"`**: Memetakan port 80 pada container ke port 8080 pada host. Sama seperti perintah `docker run -p 8080:80`, bagian ini memungkinkan kita mengakses layanan pada `http://localhost:8080`.

### Perintah Docker Compose
Setelah membuat file `docker-compose.yml`, kita dapat menjalankan semua layanan yang didefinisikan dalam file tersebut dengan perintah berikut:
```
docker-compose up -d
```

### Penjelasan Perintah
1. **`docker-compose up`**: Membuat dan menjalankan semua container yang didefinisikan dalam file `docker-compose.yml`.
2. **`-d`**: Menjalankan container di mode *detached* (latar belakang), sehingga terminal tetap bisa digunakan.

Untuk menghentikan dan menghapus semua container yang berjalan melalui Docker Compose, gunakan perintah berikut:
```
docker-compose down
```

### Kesimpulan
Docker Container adalah teknologi yang memungkinkan pengemasan aplikasi beserta semua dependensinya agar dapat dijalankan secara konsisten di berbagai lingkungan. Dengan fungsi-fungsi seperti portabilitas, efisiensi, dan pengelolaan aplikasi yang mudah, Docker telah menjadi bagian penting dari pengembangan perangkat lunak modern. Perintah `docker run -d -p 8080:80 <nama_image>` memungkinkan kita menjalankan container di latar belakang dengan port yang dipetakan, sementara Docker Compose memungkinkan pengelolaan aplikasi multi-container menggunakan file konfigurasi `docker-compose.yml` yang lebih terorganisir dan mudah diatur.
