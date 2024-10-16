# Gunakan image Ubuntu dengan Python
FROM python:3.9-slim

# Setel direktori kerja di dalam container
WORKDIR /app

# Salin file requirements.txt (jika ada) dan install dependencies
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Salin semua file aplikasi ke dalam container
COPY . .

# Expose port yang akan digunakan aplikasi
EXPOSE 8000

# Jalankan aplikasi dengan Uvicorn
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
