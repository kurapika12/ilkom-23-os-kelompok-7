## Langkah - langkah untuk melakukan beberapa command dalam container

**1. Masuk ke dalam container secara interaktif:**

### Perintah 
```
docker exec -it caddy-container /bin/sh
```
### Penjelasan Perintah
    1. `docker exec`: Menjalankan perintah di dalam container.
    2. `-it` : Membuat sesi interaktif.
    3. `/bin/sh` : Menggunakan shell untuk masuk ke container.


