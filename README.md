#  Simple Clothing App

Aplikasi **Simple Clothing App** adalah sebuah sistem manajemen stok pakaian berbasis *Command Line Interface* (CLI) yang dirancang untuk melakukan operasi CRUD (Create, Read, Update, Delete) secara efisien. Aplikasi ini dibangun menggunakan **Python 3.12.0** dengan sepenuhnya mengimplementasikan konsep *Object-Oriented Programming* (OOP) seperti *Inheritance* (Pewarisan), *Polymorphism* (Polimorfisme), dan *Encapsulation* (Enkapsulasi).

---

## Fitur Utama

Aplikasi ini dilengkapi dengan fitur-fitur manajemen inventaris yang lengkap dan interaktif:

* **Create Clothing (Tambah Data):** Membuka menu untuk menambahkan pakaian baru. Sistem mendukung dua kategori produk yang merupakan turunan dari entitas pakaian:
    * **Shirt (Kemeja):** Memiliki atribut spesifik berupa Ukuran (`Size`).
    * **Trousers (Celana):** Memiliki atribut spesifik berupa Warna (`Colour`).
* **Read Clothing List (Lihat Semua):** Menampilkan seluruh daftar pakaian yang tersedia di dalam stok lengkap dengan detail kode, nama, harga, dan karakteristik khususnya.
* **Search Clothing (Pencarian Fleksibel):** Membantu pengguna menemukan pakaian tertentu dengan memasukkan kata kunci berdasarkan **Kode** maupun **Nama** pakaian. Pencarian ini bersifat *case-insensitive* (tidak sensitif huruf besar/kecil).
* **Edit Clothing (Update Data):** Memperbarui informasi pakaian yang ada berdasarkan kodenya. Pengguna dapat memilih untuk mengubah nama, harga, atau atribut spesifiknya. Cukup tekan `Enter` jika ingin melewatkan (*skip*) dan mempertahankan data lama.
* **Delete Clothing (Hapus Data):** Menghapus data pakaian dari daftar stok secara permanen berdasarkan kode unik produk.
* **Data Persistence (Penyimpanan Otomatis):** Sistem secara otomatis memuat data lama dari file lokal saat aplikasi pertama kali dijalankan, dan akan menyimpan seluruh perubahan terbaru ke dalam file teks saat pengguna keluar dari aplikasi.
* **Robust Input Validation (Validasi Input):** Dilengkapi penanganan *error* terintegrasi untuk mencegah program *crash* akibat kesalahan ketik pengguna (seperti memasukkan huruf pada kolom harga atau memilih menu yang tidak tersedia).

---

## Struktur File & Arsitektur OOP

Project ini dirancang secara modular dengan membagi kode ke dalam beberapa file terpisah demi menjaga kebersihan struktur kode (*clean code*):

1.  **`main.py`**
    * *Entry point* utama dari aplikasi. Berfungsi untuk menginisialisasi objek aplikasi (`ClothManageApp`) dan mengeksekusi siklus hidup program.
2.  **`app.py`**
    * Berisi *class* `ClothManageApp`. File ini bertanggung jawab penuh atas alur antarmuka pengguna (UI/UX) di terminal, manajemen navigasi menu utama, serta pengumpulan input tekstual dari pengguna.
3.  **`models.py`**
    * Berisi representasi objek data (*Data Entities*). 
    * Mengimplementasikan *Inheritance*: *Class* parent **`Clothing`** mewariskan atribut dasar (`code`, `name`, `price`) ke *class* child **`Shirt`** dan **`Trousers`**.
    * Mengimplementasikan *Polymorphism*: Menggunakan *method* seperti `display_info()`, `edit_info()`, dan `format_for_txt()` dengan perilaku yang disesuaikan pada masing-masing *class* anak.
4.  **`clothing_manager.py`**
    * Berisi *class* `ClothingList` yang menerapkan *Encapsulation*. *Class* ini bertindak sebagai manajer internal/gudang penyimpanan data yang memproses logika bisnis dasar CRUD, pencarian larik objek, serta fungsi I/O file (`save_data` & `load_data`).
5.  **`utils.py`**
    * Modul utilitas mandiri yang menyediakan fungsi validasi data generik (seperti `get_valid_float`, `get_valid_float_edit`, dan `get_valid_option_menu`) menggunakan blok `try-except` untuk memastikan keandalan input numerik dan pilihan menu.
6.  **`data_pakaian.txt`**
    * File teks eksternal yang berfungsi sebagai *flat-file database* sederhana. Menyimpan records pakaian menggunakan format terdelimitasi garis tegak (`|`).

---

## Prasyarat & Cara Menjalankan Program

### Prasyarat Sistem
* Pastikan perangkat Anda sudah terpasang **Python 3.12.0** (atau versi 3.x di atasnya). Anda dapat memeriksa versi Python Anda melalui terminal dengan perintah:
    ```bash
    python --version
    ```

### Langkah-Langkah Menjalankan Aplikasi
1.  Buka aplikasi terminal, *Command Prompt* (CMD), atau PowerShell di komputer Anda.
2.  Arahkan direktori terminal ke dalam folder tempat Anda menyimpan semua file project **Simple Clothing App** menggunakan perintah `cd`. Contoh:
    ```bash
    cd path/to/your/project-folder
    ```
3.  Jalankan aplikasi dengan mengeksekusi file `main.py` menggunakan perintah berikut:
    ```bash
    python main.py
    ```
    *(Catatan: Gunakan perintah `python3 main.py` jika Anda menggunakan sistem operasi Linux atau macOS).*
4.  Aplikasi akan berjalan dan menampilkan menu interaktif. Ikuti petunjuk angka yang tertera di layar terminal Anda untuk mengoperasikan sistem.

---

> **Informasi Tambahan:** Jangan menutup terminal secara paksa menggunakan tombol `Ctrl + C` agar program dapat mengeksekusi fitur penyimpanan data (`save_data()`) dengan sempurna di menu nomor 4 (Exit).