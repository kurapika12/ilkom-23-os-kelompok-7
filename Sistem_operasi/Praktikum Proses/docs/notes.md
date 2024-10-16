consul agent -server -bootstrap-expect=1 -data-dir=/tmp/consul -node=agent-one -bind=127.0.0.1

<!-- notes -->
-server: Menjalankan sebagai server.
-bootstrap-expect=1: Mengharapkan hanya satu server dalam kluster.
-data-dir: Direktori tempat Consul menyimpan data.
-node: Nama node.
-bind: Alamat IP yang akan diikat oleh agen Consul.

<!--  autostart consul -->

3. Autostart Consul
Jika Anda ingin Consul dimulai otomatis saat boot, Anda dapat membuat layanan systemd.

Buat Unit File systemd:
Buat file di /etc/systemd/system/consul.service dengan konten berikut:
----
[Unit]
Description=Consul Agent
Requires=network-online.target
After=network-online.target

[Service]
ExecStart=/usr/local/bin/consul agent -dev -data-dir=/tmp/consul -node=agent-one -bind=127.0.0.1
Restart=on-failure

[Install]
WantedBy=multi-user.target
----

2. Reload systemd dan Mulai Consul:

sudo systemctl daemon-reload
sudo systemctl start consul
sudo systemctl enable consul


Ini akan memastikan bahwa Consul dimulai secara otomatis pada boot dan berjalan sebagai layanan latar belakang.

Consul sekarang seharusnya berjalan di Ubuntu Anda, dan Anda dapat mengaksesnya melalui antarmuka pengguna atau API.