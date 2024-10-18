import threading
import time

# Fungsi yang akan dijalankan di dalam thread
def print_time(thread_name, delay):
    count = 0
    while count < 5:
        time.sleep(delay)
        count += 1
        print(f"{thread_name}: {time.ctime(time.time())}")

# Membuat dua thread
thread1 = threading.Thread(target=print_time, args=("Thread-1", 1))
thread2 = threading.Thread(target=print_time, args=("Thread-2", 2))

# Memulai kedua thread
thread1.start()
thread2.start()

# Tunggu hingga kedua thread selesai
thread1.join()
thread2.join()

print("Program selesai.")