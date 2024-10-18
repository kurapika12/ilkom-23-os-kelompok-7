#!/bin/bash

# Daemon sederhana untuk memantau log file

LOG_FILE="/var/log/daemon_log.txt"

# Jika file log tidak ada, buat file tersebut
if [ ! -f "$LOG_FILE" ]; then
    touch "$LOG_FILE"
    echo "File log telah dibuat: $LOG_FILE"
fi

echo "Daemon dimulai. Memantau setiap 60 detik..."
echo "Daemon dimulai pada $(date)" >> $LOG_FILE

# Daemon berjalan tanpa henti
while true; do
    # Menulis waktu saat ini ke file log
    echo "Proses berjalan pada $(date)" >> $LOG_FILE
    echo "Log dicatat ke $LOG_FILE"
    sleep 60  # Tunggu 60 detik sebelum menulis log berikutnya
done