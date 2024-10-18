# Menggunakan image Node.js sebagai base
FROM node:14

# Membuat direktori kerja di dalam container
WORKDIR /app

# Menyalin file package.json ke dalam container
COPY package.json .

# Menginstall dependensi
RUN npm install

# Menyalin semua file ke dalam container
COPY . .

# Menjalankan aplikasi di port 3000
EXPOSE 3000
CMD ["npm", "start"]