import threading
import time

def process_payment(order_id):
    print(f'Proses pembayaran untuk pesanan {order_id} dimulai.')
    time.sleep(3)  # Simulasi proses pembayaran
    print(f'Pembayaran untuk pesanan {order_id} berhasil.')
    return True  # Mengembalikan status pembayaran sukses

def send_email(order_id):
    print(f'Mengirim email untuk pesanan {order_id}...')
    time.sleep(2)  # Simulasi waktu pengiriman email
    print(f'Email untuk pesanan {order_id} telah dikirim.')

def handle_order(order_id):
    # Memproses pembayaran
    if process_payment(order_id):
        # Mengirim email di thread terpisah
        email_thread = threading.Thread(target=send_email, args=(order_id,))
        email_thread.start()  # Memulai pengiriman email di thread terpisah
        email_thread.join()   # Menunggu email dikirim sebelum melanjutkan

# ID pesanan yang akan diproses
order_id = 12345
handle_order(order_id)

print('Semua proses selesai.')