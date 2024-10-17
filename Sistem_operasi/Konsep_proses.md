Definisi :
Proses adalah program yan sedang dieksekusi.Eksekusi proses dilakukan secara berurutan.Dalam suatu proses
terdapat program counter,stack dan daerah data

Status Proses :
Pada saat proses dieksekusi, akan terjadi prubahan status.Status proses didefinisikan sebagai bagian dari 
aktivitas proses yang sedang berlangsung saat itu.Status proses terdiri dari :

Running : Status yang dimiliki pada saat instruksi-instruksi dari sebuah proses dieksekusi.
Waiting : Status yang dimiliki pada saat proses menunggu suatu sebuah event seperti proes I/O.
Ready : Status yang dimiliki pada saat proses siap untuk dieksekusi oleh prosesor
New : Status yang dimiliki pada saat proses baru saja dibuat
Terminated : Status yang dimiliki pada saat proses telah selesai dieksekusi


Dalam sistem operasi, state pada proses merujuk pada berbagai tahap yang dilalui oleh sebuah proses selama eksekusi.
Berikut penjelasan pergerakan state dalam diagram proses:

New → Ready: Proses baru dibuat dan dimasukkan ke dalam antrian siap.
Ready → Running: Prosesor memberikan giliran eksekusi kepada proses, sehingga proses pindah ke state Running.
Running → Waiting: Jika proses membutuhkan operasi input/output atau menunggu sumber daya, proses berpindah ke state Waiting.
Running → Ready: Jika proses di-preempt (dihentikan sementara) karena ada proses dengan prioritas lebih tinggi, maka proses akan kembali ke state Ready.
Waiting → Ready: Setelah proses menyelesaikan operasinya (misalnya I/O selesai), proses kembali ke state Ready untuk menunggu giliran eksekusi lagi.
Running → Terminated: Proses selesai dieksekusi dan pindah ke state Terminated.
Proses dapat berpindah antar state ini sampai selesai dieksekusi atau dihentikan. Diagram ini membantu memahami bagaimana proses dikelola oleh sistem operasi dari awal hingga selesai.

