## Panduan Membuat Daemon dari Aplikasi Flask

**Langkah-langkah:**

1. **Kembangkan Aplikasi Web:**
   * Gunakan kerangka kerja Flask untuk membangun aplikasi web sederhana sesuai kebutuhan Anda.

2. **Siapkan Lingkungan:**
   * Pasang library `python-daemon` yang akan membantu kita mengubah aplikasi menjadi daemon. Gunakan perintah `pip install python-daemon` di terminal.

3. **Transformasi Menjadi Daemon:**
   * Buat file Python baru (misalnya, `daemon_flask.py`) yang berisi kode untuk menjalankan aplikasi Flask dalam mode daemon.
   * Manfaatkan konteks daemon dari library `python-daemon` untuk menjalankan aplikasi di latar belakang sistem.

4. **Jalankan Daemon:**
   * Eksekusi file Python yang telah dibuat dengan perintah `python daemon_flask.py` di terminal. Aplikasi Anda kini akan berjalan terus menerus di latar belakang.

5. **Verifikasi:**
   * Pastikan aplikasi berjalan dengan benar dengan memeriksa log atau menggunakan tool monitoring sistem operasi Anda. Anda juga bisa mengakses aplikasi melalui browser untuk memastikan semua fitur berfungsi sesuai harapan.

**Ilustrasi:**
    ![screenshot apk berjalan](daemon.png)

**Penjelasan Singkat:**

Panduan ini memandu Anda untuk mengubah aplikasi Flask yang biasa menjadi daemon yang berjalan secara terus-menerus di latar belakang sistem. Dengan menjadi daemon, aplikasi Anda tidak akan berhenti meskipun Anda menutup terminal atau me-reboot sistem.