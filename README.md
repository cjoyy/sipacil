# sipacil
### Nama  : Calvin Joy Tarigan
### NPM   : 2306244974
### Kelas : PBP C
### Link  : http://calvin-joy-sipacil.pbp.cs.ui.ac.id/
---

# Tugas 3: Implementasi Form dan Data Delivery pada Django

<details>
<summary>Click for more detail</summary>
<br>

1. Data delivery penting dalam pengimplementasian platform karena memungkinkan pertukaran informasi antara client dan server. Tanpa mekanisme ini, aplikasi tidak akan dapat menampilkan atau menerima data secara dinamis, yang sangat penting dalam aplikasi berbasis web yang membutuhkan interaksi terus-menerus dengan server untuk mendapatkan atau mengirimkan informasi.

2. JSON biasanya dianggap lebih baik untuk penggunaan web modern dibandingkan XML karena JSON lebih ringkas, lebih mudah dibaca oleh manusia, dan lebih cepat diproses oleh komputer. JSON juga memiliki struktur yang lebih sederhana dibandingkan XML, yang sering kali membutuhkan tag pembuka dan penutup yang memperbesar ukuran data. Oleh karena itu, JSON lebih populer karena efisiensi dalam pengiriman data dan kemudahan penggunaan dengan bahasa pemrograman modern, termasuk JavaScript.

3. Method is_valid() pada form Django digunakan untuk memvalidasi data yang dimasukkan ke dalam form. Method ini akan memeriksa apakah data yang dimasukkan sesuai dengan aturan validasi yang telah ditentukan (seperti tipe data, panjang karakter, dsb.). Jika data valid, method ini mengembalikan nilai True dan data dapat diproses lebih lanjut. Kita membutuhkan method ini untuk memastikan bahwa data yang dikirimkan ke server tidak mengandung kesalahan atau nilai yang tidak diinginkan, sehingga aplikasi berjalan dengan aman dan sesuai harapan.

4. csrf_token digunakan untuk melindungi aplikasi dari serangan CSRF (Cross-Site Request Forgery). Jika kita tidak menambahkan csrf_token, penyerang dapat mengirimkan permintaan palsu dari situs lain yang seolah-olah berasal dari pengguna yang sah, sehingga memungkinkan penyerang untuk melakukan aksi seperti mengubah data atau melakukan transaksi tanpa sepengetahuan pengguna. Dengan csrf_token, setiap permintaan form harus mengandung token yang hanya valid untuk sesi pengguna tersebut, sehingga serangan CSRF bisa dicegah.

5. Cara saya mengimplementasikan checklist step-by-step,

a. Buat Skeleton Views
- Buat direktori templates dan file base.html.
- Gunakan {% block %} di base.html untuk membuat kerangka umum yang bisa di-extend.
- Ubah file main.html untuk me-extend base.html.
- Sesuaikan settings.py dengan menambahkan templates ke dalam DIRS pada variabel TEMPLATES.

b. Ubah Primary Key menjadi UUID
- Tambahkan baris id = models.UUIDField() di models.py untuk mengganti ID menjadi UUID.
- Jika sudah ada data, hapus database lama (db.sqlite3).
- Jalankan perintah migrasi:
```
python manage.py makemigrations
python manage.py migrate
```

c. Buat Form Input Data
- Buat file forms.py di direktori main dan tambahkan form model ProductEntryForm.
- Tambahkan fungsi create_product_entry di views.py untuk menampilkan form dan menyimpan data yang diinput.
- Ubah fungsi show_main di views.py untuk menampilkan data ProductEntry yang sudah ada.
- Tambahkan URL path di urls.py untuk mengakses form input data

d. Tampilkan Data dalam Format XML dan JSON
- Tambahkan fungsi show_xml dan show_json di views.py untuk menampilkan data dalam format XML dan JSON menggunakan serializers.
- Buat path URL untuk masing-masing format di urls.py:
```
path('xml/', show_xml, name='show_xml'),
path('json/', show_json, name='show_json')
```

e. Tampilkan Data Berdasarkan ID dalam Format XML dan JSON
- Tambahkan fungsi show_xml_by_id dan show_json_by_id di views.py untuk menampilkan data berdasarkan ID.
- Buat path URL untuk mengakses data berdasarkan ID di urls.py:
```
path('xml/<str:id>/', show_xml_by_id, name='show_xml_by_id'),
path('json/<str:id>/', show_json_by_id, name='show_json_by_id'),
```

f. Tes dengan Postman
- Jalankan server Django dengan perintah python manage.py runserver.
- Gunakan Postman untuk mengakses URL /xml/, /json/, /xml/[id], dan /json/[id].
![image](https://github.com/user-attachments/assets/f615f146-a445-469e-8461-74a648f1de12)
![image](https://github.com/user-attachments/assets/2deb2f2d-9f96-48c3-a4b5-4da731629c19)
![image](https://github.com/user-attachments/assets/807d2d84-8401-4db4-bf36-00a676ac1f0a)
![image](https://github.com/user-attachments/assets/bd545733-8451-4fae-91d7-620bf8bb2e0b)

g. Push Otomatis ke PWS Menggunakan GitHub Actions:
- Buat direktori .github/workflows/ di proyek Django.
- Buat file deploy.yml di dalamnya, kemudian isi dengan code yang diberikan asdos di dc
- Membuat Secret di GitHub:
Pergi ke Settings > Secrets and variables > Actions.
Isi Secret dengan format,
```
Name : PWS_URL
Secret : https://<username>:<password>@pbp.cs.ui.ac.id/<username>/<proyek>
```
- Update settings.py, tambahkan CSRF_TRUSTED_ORIGINS = ["https://<URL_PWS_KAMU>"]
  
h. Git Push:
- Lakukan git add, git commit, dan git push ke GitHub.
- GitHub Actions akan otomatis push ke PWS.

</details>

---

# Tugas 2: Implementasi Model-View-Template (MVT) pada Django

<details>
<summary>Click for more detail</summary>
<br>

1. Dengan mengikuti dan memahami contoh ataupun langkah dari tutorial 0 dan 1 kemudian saya implementasikan sesuai kebutuhan yang diminta.
  Ketika terjadi kesalahan, saya cenderung mencari langkah mana yang terlewat ataupun salah, kemudian memulainya lagi dari awal agar dapat lebih ingat lagi langkah demi langkah.

a. Persiapan Awal:
Instalasi Django: Install Django menggunakan pip.
Pembuatan Proyek: Inisialisasi proyek Django baru.
Pembuatan Aplikasi: Buat aplikasi dalam proyek Django.

b. Konfigurasi urls.py:
Definisi URL di Proyek: Tambahkan rute untuk aplikasi dalam konfigurasi URL proyek.
URL Aplikasi: Tentukan rute untuk views dalam aplikasi.

c. Implementasi views.py:
Buat Views: Definisikan fungsi untuk menangani request dan mengembalikan respons yang sesuai.

d. Desain models.py:
Definisikan Model: Buat model untuk merepresentasikan data yang akan disimpan di database.
Migrasi: Terapkan perubahan model ke database.

e. Buat Berkas HTML:
Template HTML: Buat berkas HTML untuk menampilkan data yang dikirim oleh views.

f. Testing:
Jalankan Server: Mulai server pengembangan.
Uji Akses: Akses aplikasi melalui browser untuk memastikan semuanya berfungsi dengan baik.

g. Git:
Add, Commit, Push: Simpan perubahan kode ke repositori versi kontrol dengan Git.

h. Deployment PWS:
Deploy: Push aplikasi ke PWS agar dapat terlihat secara online

3. User mengirimkan request melalui URL, lalu Django mengarahkan permintaan ke View yang memproses logika. Jika perlu data, View berinteraksi dengan Model untuk mengambilnya dari database. Setelah itu, View mengirim data ke Template yang menampilkan hasilnya dalam bentuk HTML. Akhirnya, Django mengirimkan response tersebut kembali ke user sebagai halaman web yang bisa dilihat di browser.
![image](https://github.com/user-attachments/assets/f427b469-1528-49ab-9b4b-df4706ec63bd)

4. Git berfungsi sebagai version control system (vcs) yang sangat berguna dalam pengembangan perangkat lunak. Fungsinya yaitu tracking perubahan, kolaborasi, backup, branching dan merging.
   
5. Django adalah pilihan ideal untuk pemula karena menawarkan kerangka kerja terstruktur dengan fitur lengkap seperti autentikasi, admin panel, dan ORM yang mempercepat pengembangan. Dengan arsitektur Model-View-Template (MVT), Django memisahkan logika bisnis, data, dan tampilan secara jelas, memudahkan pemahaman dan implementasi. Dokumentasi yang lengkap dan komunitas besar juga menyediakan dukungan yang cepat dan akses ke solusi, sehingga proses pembelajaran menjadi lebih mudah.

6. Karena berfungsi untuk memetakan objek Python ke dalam tabel di database. Dengan ORM, pengembang dapat berinteraksi dengan database menggunakan objek Python tanpa perlu menulis query SQL secara langsung.
  Django ORM otomatis menerjemahkan operasi pada objek model menjadi instruksi SQL, sehingga mempermudah manipulasi data dan menjaga kode tetap portable di berbagai jenis database.

</details>
