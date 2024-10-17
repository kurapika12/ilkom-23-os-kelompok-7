Thread adalah unit eksekusi terkecil dalam sebuah program yang dapat dijalankan secara independen. Thread memungkinkan program melakukan beberapa tugas secara bersamaan (parallel atau concurrency) di dalam satu proses, sehingga meningkatkan efisiensi dan kinerja.

Struktur dari sebuah thread meliputi:

Thread ID: Setiap thread memiliki identitas unik yang membedakannya dari thread lain dalam proses yang sama.
Program Counter: Menyimpan alamat instruksi berikutnya yang akan dieksekusi oleh thread.
Register Set: Menyimpan konteks CPU saat thread sedang dieksekusi, termasuk nilai register saat itu.
Stack: Setiap thread memiliki stack-nya sendiri untuk menyimpan variabel lokal, parameter fungsi, dan informasi lainnya yang diperlukan selama eksekusi.
Thread-Specific Data: Beberapa implementasi thread memungkinkan thread memiliki data khusus yang hanya dapat diakses oleh thread tersebut.
State: Status atau kondisi thread (misalnya, running, ready, blocked, atau terminated).

Thread ini bisa berjalan secara bersamaan pada beberapa core (jika prosesor mendukung), dan manajemennya diatur oleh sistem operasi atau pustaka thread seperti pthread pada C atau threading module pada Python.


Single thread adalah ketika sebuah program hanya menggunakan satu thread untuk menjalankan tugasnya. Dalam model ini, program dieksekusi secara sekuensial, yaitu satu tugas selesai sebelum tugas lainnya dimulai.

Keuntungan:

Mudah dikelola: Single thread lebih sederhana karena tidak perlu menangani masalah seperti sinkronisasi dan deadlock.
Lebih stabil: Karena tidak ada banyak bagian dari program yang berjalan bersamaan, peluang terjadinya bug terkait concurrency lebih sedikit.
Lebih efisien pada tugas ringan: Untuk aplikasi yang sederhana atau tidak membutuhkan multitasking, single thread sudah cukup dan lebih ringan dari segi sumber daya.

Multi thread adalah ketika sebuah program menggunakan lebih dari satu thread untuk menjalankan beberapa tugas secara bersamaan (parallel atau concurrency). Setiap thread berjalan independen, tetapi berbagi memori dan sumber daya dalam satu proses.

Keuntungan:

Peningkatan kinerja: Multi thread memungkinkan pemrosesan beberapa tugas secara bersamaan, sehingga meningkatkan kecepatan program, terutama pada komputer dengan beberapa inti (multi-core).
Responsif: Program multi thread dapat lebih responsif karena satu thread dapat menangani operasi latar belakang sementara thread lain menunggu input pengguna atau menangani tugas lainnya.
Efisien dalam pengelolaan sumber daya: Karena thread berbagi memori dan sumber daya yang sama, overhead yang terkait dengan pembuatan proses baru lebih rendah daripada menggunakan multi-process.
Penggunaan lebih baik dari CPU multi-core: Dengan multi-threading, program dapat memanfaatkan sepenuhnya kemampuan prosesor multi-core, meningkatkan kinerja secara keseluruhan.
Namun, multi-threading juga memiliki beberapa tantangan, seperti masalah sinkronisasi, race condition, dan deadlock, di mana thread dapat berkonflik dalam pengaksesan sumber daya bersama.

Perbandingan:
Single Thread cocok untuk program sederhana yang tidak membutuhkan eksekusi paralel.
Multi Thread lebih baik untuk aplikasi yang membutuhkan multitasking atau yang bisa memanfaatkan CPU multi-core seperti aplikasi server, game, atau aplikasi berbasis UI yang membutuhkan responsivitas tinggi.

Perbedaan antara User-Level Threads (ULT) dan Kernel-Supported Threads (KST) (juga dikenal sebagai kernel-level threads atau kernel threads) terletak pada siapa yang mengelola dan menjalankan thread tersebut: apakah di tingkat pengguna (user space) atau di tingkat kernel (kernel space).

User-level threads dikelola oleh pustaka thread di ruang pengguna, sehingga sistem operasi tidak mengetahui keberadaan thread-thread ini. Semua manajemen thread dilakukan oleh aplikasi tanpa melibatkan kernel.
Kernel-supported threads dikelola langsung oleh sistem operasi di ruang kernel. Sistem operasi mengetahui setiap thread yang dijalankan, dan dapat mengelola masing-masing thread secara independen.

Berikut adalah perbedaan singkat antara User-Level Threads (ULT) dan Kernel-Supported Threads (KST):

User-Level Threads (ULT)
Manajemen: Dikelola di ruang pengguna oleh pustaka, tidak melibatkan kernel.
Keuntungan: Lebih cepat dan efisien karena tidak melibatkan kernel, mudah diimplementasikan dan portabel.
Kelemahan: Jika satu thread terblokir, semua thread dalam proses tersebut juga terblokir, tidak bisa memanfaatkan multi-core secara optimal.
Kernel-Supported Threads (KST)
Manajemen: Dikelola langsung oleh sistem operasi (kernel).
Keuntungan: Thread bisa berjalan secara paralel di multi-core, jika satu thread terblokir, thread lain tetap bisa berjalan.
Kelemahan: Pembuatan dan manajemen lebih lambat karena melibatkan kernel, overhead lebih tinggi.
Perbedaan utama adalah siapa yang mengelola thread dan bagaimana mereka menangani blocking dan penggunaan multi-core

Ada tiga model multithreading yang umum digunakan: Many-to-One, One-to-One, dan Many-to-Many. Pada Many-to-One, banyak thread pengguna dipetakan ke satu thread kernel. Model ini cepat dalam pembuatan dan manajemen thread karena dikelola di level pengguna, namun tidak dapat memanfaatkan multi-core, dan jika satu thread terblokir, semua thread terblokir. Pada One-to-One, setiap thread pengguna dipetakan ke satu thread kernel, sehingga memungkinkan thread berjalan paralel pada multi-core dan tetap berjalan meski ada thread yang terblokir, tetapi memiliki overhead yang lebih tinggi karena setiap thread melibatkan kernel. Sementara itu, Many-to-Many memungkinkan banyak thread pengguna dipetakan ke sejumlah thread kernel yang lebih kecil, memanfaatkan pemrosesan paralel dengan overhead yang lebih rendah dibanding One-to-One, meskipun implementasinya lebih kompleks.