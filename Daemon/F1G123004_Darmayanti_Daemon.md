# Panduan pembuatan dameon process
NIM: F1G123026
Nama: Darmayanti

## Buat file .service
masuk sebagai superuser, lalu jalankan perintah
```bash
$ sudo touch /etc/systemd/system/darma.service
```

## Penulisan script konfigurasi .service
```bash
[Unit]
Description=Freyana Daemon

[Service]
User=darmay
Restart=always
WorkingDirectory=/home/darmay/venv/project
Environment="PYTHONPATH=/home/darmay/./lib/python3.12/site-packages"
ExecStart=/home/darmay/venv/bin/uvicorn main:app --reload --port 7080

[Install]
WantedBy=multi-user.target
```

## Penjelasan singkat mengenai  script konfigurasi .service
[Unit]
Description: Deskripsi singkat mengenai service. Dalam contoh ini disebut "Freyana Daemon".

[Service]
User: Menentukan pengguna yang akan menjalankan service ini. Di sini, service dijalankan oleh pengguna darmay.

Restart: Menentukan kebijakan restart. Opsi always memastikan service akan otomatis restart jika terjadi error atau stop.

WorkingDirectory: Direktori kerja di mana aplikasi akan dijalankan (/home/darmay/venv/project).
ExecStart: Perintah untuk menjalankan service. Di sini uvicorn digunakan untuk menjalankan aplikasi dengan konfigurasi reload di port 7080.

[Install]
WantedBy: Menentukan target saat service akan diaktifkan, di sini adalah multi-user.target.

## Buat file .service
masuk sebagai superuser, lalu jalankan perintah
```bash
$ sudo touch /etc/systemd/system/aslam.service
```

## Penulisan script konfigurasi .service
```bash
[Unit]
Description=Freyana Daemon

[Service]
User=hacker_one
Restart=always
WorkingDirectory=/home/hacker_one/venv/project
Environment="PYTHONPATH=/home/hacker_one/./lib/python3.12/site-packages"
ExecStart=/home/hacker_one/venv/bin/uvicorn main:app --reload --port 7080

[Install]
WantedBy=multi-user.target
```

## Penjelasan singkat mengenai  script konfigurasi .service
[Unit]
Description: Menyediakan deskripsi singkat tentang service. Dalam kasus ini, service disebut "Freyana Daemon".

[Service]
User: Menentukan pengguna yang akan menjalankan service ini, yaitu hacker_one.

Restart: Menentukan kebijakan restart service. always berarti service akan selalu restart jika keluar, terlepas dari status keluar.

WorkingDirectory: Menetapkan direktori kerja untuk service. Dalam hal ini, service akan beroperasi di /home/hacker_one/venv/project.

Environment: Menentukan variabel lingkungan. PYTHONPATH diset untuk mencakup path ke package Python yang diperlukan, dalam hal ini di lib/python3.12/site-packages.

ExecStart: Perintah yang dijalankan saat service dimulai. Ini menjalankan uvicorn untuk menjalankan aplikasi FastAPI yang didefinisikan dalam main.py pada port 7080, dengan opsi --reload untuk memuat ulang aplikasi saat ada perubahan kode.

[Install]
WantedBy: Menentukan target di mana service ini akan dimuat. multi-user.target berarti service akan aktif saat sistem berada dalam mode multi-user (umumnya saat booting normal).



## jalankan perintah daemon
```bash
$ sudo systemctl daemon-reload 
$ sudo systemctl enable darma.service 
$ sudo systemctl start darma.service
$ sudo systemctl status darma.service
```





