# Panduan pembuatan dameon process
NIM: F1G123026
Nama: Muhammad Ihram Syahputra

dalam hal ini saya akan memaparkan tahapan pembuatan daemon process.Pada studi kasus kali saya menjalankan website PHP Warung makan sederhana yang berjalan didaemon proses 

## 1. Buat directori untuk script
masuk sebagai superuser, lalu jalankan perintah
```bash
$ sudo nano /etc/systemd/system/iamsyh.service
```
## 2. Isi file.service (iamsyh.service) dengan konfigurasi web PHP berikut :
```bash
[Unit]
Description=PHP Web Application dengan Apache
After=network.target apache2.service
Requires=apache2.service

[Service]
User=www-data
Group=www-data
WorkingDirectory=/var/www/html/RPL-kelompok-11

# Environment untuk PHP
Environment=PHP_ENV=production
Environment=DB_HOST=localhost
Environment=DB_USER=root
Environment=DB_PASS=""
Environment=DB_NAME=db_warung

ExecStart=/usr/bin/php -S localhost:8000
Restart=always
RestartSec=3
```

## 3. jalankan perintah daemon 
```bash
$ sudo systemctl daemon-reload 
$ sudo systemctl enable iamsyh.service 
$ sudo systemctl start iamsyh.service
```

## 4. Bukti file service telah berjalan sebagai daemon
```bash
$ sudo systemctl status iamsyh.service
```
![Bukti_daemon](/Bukti_gambar/proof-iamdaemon.png)