# Cara Kerja Docker
Docker bekerja dengan cara mengemas aplikasi beserta semua dependensinya ke dalam container. Container ini berjalan secara terisolasi di atas Docker Engine, yang memungkinkan aplikasi dapat berjalan dengan konsisten di berbagai lingkungan.

### 1. **Image**
Image adalah cetak biru (blueprint) dari container. Image berisi semua yang diperlukan untuk menjalankan aplikasi, seperti kode sumber, pustaka, dependensi, dan file sistem.

### 2. **Container**
Container adalah instansi dari image yang dapat berjalan secara mandiri. Container dapat dimulai, dihentikan, dihancurkan, dan dibuat ulang dari image kapan saja.

### 3. **Docker Daemon**
Docker Daemon (dockerd) adalah proses yang berjalan di latar belakang pada mesin host dan bertanggung jawab untuk membangun, menjalankan, dan mengelola container.

### 4. **Docker CLI (Command Line Interface)**
Docker CLI memungkinkan pengembang untuk berinteraksi dengan Docker Daemon melalui perintah di terminal, seperti `docker run`, `docker ps`, `docker stop`, dan lainnya.

### 5. **Docker Registry**
Docker Registry, seperti Docker Hub, adalah tempat penyimpanan image yang dapat diunduh dan digunakan kembali di sistem lain. Pengembang dapat mengunggah (push) image mereka ke registry dan mengunduh (pull) image yang sudah tersedia.

### **Alur Kerja Docker**
1. **Membuat Dockerfile**: File ini berisi instruksi untuk membuat image, seperti langkah-langkah untuk menginstal dependensi dan mengatur lingkungan aplikasi.
2. **Membangun Image**: Menggunakan perintah `docker build`, Docker membuat image dari Dockerfile.
3. **Menjalankan Container**: Dari image tersebut, pengembang membuat container menggunakan perintah `docker run`.
4. **Pengelolaan Container**: Pengembang dapat menghentikan (`docker stop`), memulai (`docker start`), atau menghapus (`docker rm`) container kapan saja.

---

# Perbedaan Docker dengan Virtual Machine (VM)
Docker dan Virtual Machine (VM) sama-sama memungkinkan pengembang menjalankan beberapa aplikasi di satu mesin. Namun, ada perbedaan signifikan dalam cara kerja dan efisiensi sumber daya.

| **Aspek**                  | **Docker**                                  | **Virtual Machine (VM)**                         |
|----------------           -|------------------------------------------ --|--------------------------------------------     -|
| **Arsitektur**             | Berjalan di atas Docker Engine              | Berjalan di atas hypervisor                      |
| **Ukuran**                 | Ringan, hanya membutuhkan image             | Berat, membutuhkan satu OS penuh                 |
| **Isolasi**                | Mengisolasi aplikasi di container           | Mengisolasi aplikasi dalam mesin virtual         |
| **Sistem Operasi**         | Menggunakan kernel OS host                  | Memerlukan OS tamu di atas hypervisor            |
| **Startup Time**           | Cepat (dalam hitungan detik)                | Lambat (memerlukan booting OS)                   |
| **Penggunaan Sumber Daya** | Lebih efisien, berbagi kernel dengan host   | Boros sumber daya, setiap VM memiliki OS sendiri |
| **Contoh Penggunaan**      | Menjalankan aplikasi secara terisolasi      | Menjalankan sistem operasi yang berbeda          |

### **Kesimpulan Perbedaan**
- **Docker** lebih ringan dan efisien karena tidak perlu membawa sistem operasi tamu, hanya kontainerisasi aplikasi.
- **Virtual Machine** memberikan isolasi penuh pada tingkat OS, tetapi lebih berat dan membutuhkan lebih banyak sumber daya.

Docker cocok digunakan untuk pengembangan dan pengujian aplikasi yang membutuhkan portabilitas, sedangkan Virtual Machine lebih cocok untuk menjalankan OS yang berbeda secara bersamaan di satu host.

---