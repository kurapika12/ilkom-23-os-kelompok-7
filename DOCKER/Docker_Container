# Pengertian Docker Container
Docker Container adalah unit perangkat lunak yang terisolasi yang mencakup semua yang dibutuhkan untuk menjalankan suatu aplikasi, termasuk kode, dependensi, pustaka, dan pengaturan lingkungan. Konsep ini memungkinkan aplikasi berjalan secara konsisten di berbagai lingkungan pengembangan, pengujian, dan produksi.

Docker Container menggunakan teknologi virtualisasi tingkat sistem operasi, yang membuatnya lebih ringan dibandingkan mesin virtual (VM). Setiap container berbagi kernel sistem operasi yang sama tetapi berjalan secara terisolasi satu sama lain.

## Fungsi Docker Container
1. **Isolasi Aplikasi**: Docker Container memungkinkan pengembang untuk mengisolasi aplikasi dan dependensinya, sehingga tidak ada konflik antara aplikasi yang berjalan di lingkungan yang sama.
2. **Portabilitas**: Container dapat dijalankan di berbagai platform, seperti pengembangan lokal, server, atau cloud, tanpa memerlukan konfigurasi ulang.
3. **Efisiensi Sumber Daya**: Berbeda dengan mesin virtual, Docker Container berbagi kernel OS yang sama, sehingga lebih ringan dan efisien dalam penggunaan sumber daya.
4. **Pengelolaan Aplikasi yang Lebih Mudah**: Dengan Docker, pengelolaan aplikasi menjadi lebih mudah karena pengembang dapat membuat, menghapus, atau memindahkan container dengan cepat.
5. **Penyebaran Cepat**: Aplikasi yang dikemas dalam container dapat dipindahkan dari pengembangan ke produksi dengan cepat dan tanpa masalah.

## Perintah Docker Run dan Penjelasannya

Salah satu perintah yang paling umum digunakan adalah `docker run`. Berikut adalah contoh dan penjelasan dari perintah tersebut:

### Perintah Docker Run
```
docker run -d -p 8080:80 <nama_image>
```

### Penjelasan Perintah
1. **`docker run`**: Memerintahkan Docker untuk membuat dan menjalankan container dari image yang disebutkan.
2. **`-d`**: Menjalankan container di mode *detached* (latar belakang), sehingga terminal tetap bisa digunakan untuk perintah lainnya.
3. **`-p 8080:80`**: Memetakan port 80 pada container ke port 8080 pada host. Artinya, ketika kita mengakses `localhost:8080`, sebenarnya kita mengakses port 80 di container.
   - **8080**: Port pada host (komputer lokal).
   - **80**: Port pada container (biasanya digunakan oleh server web).
4. **`<nama_image>`**: Nama dari image Docker yang digunakan untuk membuat container.

### Contoh Perintah
```
docker run -d -p 8080:80 nginx
```
**Penjelasan**:
- Membuat dan menjalankan container dari image `nginx`.
- Container berjalan di latar belakang (`-d`).
- Port 80 pada container dipetakan ke port 8080 pada host, sehingga kita dapat mengaksesnya melalui `http://localhost:8080`.

## Kesimpulan
Docker Container adalah teknologi yang memungkinkan pengemasan aplikasi beserta semua dependensinya agar dapat dijalankan secara konsisten di berbagai lingkungan. Dengan fungsi-fungsi seperti portabilitas, efisiensi, dan pengelolaan aplikasi yang mudah, Docker telah menjadi bagian penting dari pengembangan perangkat lunak modern. Perintah `docker run -d -p 8080:80 <nama_image>` memungkinkan kita menjalankan container di latar belakang dengan port yang dipetakan, membuat pengelolaan layanan web lebih fleksibel dan efisien.
