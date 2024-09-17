from flask import Flask, render_template, request, redirect, url_for, flash
import sqlite3

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'  # Untuk menggunakan flash messages

# Fungsi untuk koneksi ke database
def get_db_connection():
    conn = sqlite3.connect('books.db')
    conn.row_factory = sqlite3.Row
    return conn

# Inisialisasi database dan tabel buku
def init_db():
    conn = get_db_connection()
    conn.execute('''
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER NOT NULL,
            pages INTEGER NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Route untuk halaman utama yang menampilkan koleksi buku
@app.route('/')
def index():
    conn = get_db_connection()
    books = conn.execute('SELECT * FROM books').fetchall()
    conn.close()
    return render_template('index.html', books=books)

# Route untuk menambahkan buku baru
@app.route('/add', methods=('GET', 'POST'))
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        pages = request.form['pages']

        if not title or not author or not year or not pages:
            flash('Semua field wajib diisi!', 'error')
        else:
            conn = get_db_connection()
            conn.execute('INSERT INTO books (title, author, year, pages) VALUES (?, ?, ?, ?)',
                         (title, author, year, pages))
            conn.commit()
            conn.close()
            flash('Buku berhasil ditambahkan!', 'success')
            return redirect(url_for('index'))

    return render_template('add_book.html')

# Route untuk mengedit buku
@app.route('/edit/<int:id>', methods=('GET', 'POST'))
def edit_book(id):
    conn = get_db_connection()
    book = conn.execute('SELECT * FROM books WHERE id = ?', (id,)).fetchone()

    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        year = request.form['year']
        pages = request.form['pages']

        if not title or not author or not year or not pages:
            flash('Semua field wajib diisi!', 'error')
        else:
            conn.execute('UPDATE books SET title = ?, author = ?, year = ?, pages = ? WHERE id = ?',
                         (title, author, year, pages, id))
            conn.commit()
            conn.close()
            flash('Buku berhasil diperbarui!', 'success')
            return redirect(url_for('index'))

    return render_template('edit_book.html', book=book)

# Route untuk menghapus buku
@app.route('/delete/<int:id>', methods=('POST',))
def delete_book(id):
    conn = get_db_connection()
    conn.execute('DELETE FROM books WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    flash('Buku berhasil dihapus!', 'success')
    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Inisialisasi database pada saat server pertama kali berjalan
    app.run(debug=True)
