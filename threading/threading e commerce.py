import threading
import time

def process_payment(order_id):
    print(f'Proses pembayaran untuk pesanan {order_id} dimulai.')
    time.sleep(3)  # Simulasi proses pembayaran
    print(f'Pembayaran untuk pesanan {order_id} berhasil.')

def send_notification(order_id):
    time.sleep(1)  # Simulasi waktu tunggu untuk pengiriman notifikasi
    print(f'Notifikasi pengiriman untuk pesanan {order_id} dikirim.')

order_id = 12345

# Membuat thread untuk proses pembayaran dan pengiriman notifikasi
payment_thread = threading.Thread(target=process_payment, args=(order_id,))
notification_thread = threading.Thread(target=send_notification, args=(order_id,))

# Memulai thread
payment_thread.start()
notification_thread.start()

# Menunggu thread selesai
payment_thread.join()
notification_thread.join()

print('Semua proses selesai.')