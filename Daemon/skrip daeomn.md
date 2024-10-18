git commit -m "Menambahkan skrip daemon untuk monitoring log file.

Skrip ini menciptakan daemon sederhana yang berjalan terus-menerus di background.
Daemon ini melakukan pengecekan file log dan mencatat waktu saat setiap 60 detik.
Jika file log belum ada, daemon akan otomatis membuat file log baru di '/var/log/daemon_log.txt'.
Skrip ini bermanfaat untuk memahami dasar pembuatan proses daemon di sistem berbasis Linux.
Selain itu, skrip ini bisa dimodifikasi lebih lanjut untuk berbagai kebutuhan monitoring sistem."