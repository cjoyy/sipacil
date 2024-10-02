# sipacil
### Nama  : Calvin Joy Tarigan
### NPM   : 2306244974
### Kelas : PBP C
### Link  : http://calvin-joy-sipacil.pbp.cs.ui.ac.id/
---

# Tugas 5: Desain Web menggunakan HTML, CSS dan Framework CSS

<details>
<summary>Click for more detail</summary>
<br>

## 1.  Jika terdapat beberapa CSS selector untuk suatu elemen HTML, jelaskan urutan prioritas pengambilan CSS selector tersebut!
- Inline CSS: CSS yang didefinisikan langsung pada elemen menggunakan atribut style memiliki prioritas tertinggi.

- ID Selector (#id) memiliki tingkat prioritas tertinggi di antara selector lainnya yang ada di dalam file CSS.

- Class, Attribute, dan Pseudo-class Selector (.class, [attribute], :hover) memiliki prioritas di bawah ID selector.

- Tag (Type) Selector (div, p, a) memiliki prioritas paling rendah.

- Universal Selector (*) dan kombinasi atau group selector biasanya memiliki prioritas paling rendah.

- !important: Deklarasi ini mengesampingkan semua aturan di atas, tetapi penggunaannya sebaiknya dihindari karena dapat menyulitkan debugging dan pemeliharaan kode.

Urutan prioritas dihitung berdasarkan kehadiran tipe selector (ID, class, atau tag) di dalam satu rule CSS. Jika dua selector memiliki tingkat spesifisitas yang sama, maka yang muncul terakhir dalam file CSS akan diterapkan.
 
## 2. Mengapa responsive design menjadi konsep yang penting dalam pengembangan aplikasi web? Berikan contoh aplikasi yang sudah dan belum menerapkan responsive design!
Responsive design sangat penting karena memungkinkan aplikasi web beradaptasi dengan berbagai ukuran layar dan perangkat, seperti smartphone, tablet, dan desktop. Ini meningkatkan user experience, memastikan navigasi yang mudah, dan mengoptimalkan SEO, karena mesin pencari seperti Google memprioritaskan situs yang mobile-friendly.

- Contoh aplikasi yang sudah menerapkan responsive design:

Twitter: Desain yang fleksibel dan menyesuaikan tampilan dengan berbagai ukuran layar.

- Contoh aplikasi yang belum menerapkan responsive design:

Craigslist: Tampilan kaku dan sulit diakses dari perangkat mobile, mengharuskan pengguna untuk zoom atau scroll horizontal.

## 3. Jelaskan perbedaan antara margin, border, dan padding, serta cara untuk mengimplementasikan ketiga hal tersebut!
- Margin: Ruang kosong di luar elemen, yang memisahkan elemen dari elemen lain. Margin tidak mempengaruhi ukuran elemen itu sendiri.

- Border: Garis yang mengelilingi elemen, yang berada di antara margin dan padding. Border dapat diatur ketebalan, warna, dan gayanya.

- Padding: Ruang kosong di dalam elemen, antara konten elemen dan border. Padding menambah ruang di dalam elemen tanpa mempengaruhi margin.

Margin, border, dan padding adalah bagian penting dalam mengatur jarak dan tampilan elemen pada halaman web. Margin menambahkan jarak di luar elemen, border adalah garis yang membungkus elemen, dan padding menambah ruang di dalam elemen antara konten dan border. 

Implementasi
```
div {
  margin: 20px; /* Menambah ruang di luar elemen */
  border: 2px solid black; /* Border hitam dengan ketebalan 2px */
  padding: 10px; /* Menambah ruang di dalam elemen, antara konten dan border */
}
```

## 4. Jelaskan konsep flex box dan grid layout beserta kegunaannya!

Flexbox dan Grid Layout adalah dua teknik dalam CSS yang digunakan untuk mengatur tata letak elemen di halaman web, masing-masing dengan karakteristik dan kegunaan yang berbeda.

- Flex box adalah metode tata letak yang dirancang untuk satu dimensi (baik kolom atau baris) dan digunakan untuk mengatur elemen di sepanjang satu sumbu utama (horizontal atau vertikal). 

  Flex box berguna untuk mengatur elemen secara rapi dalam satu baris atau kolom. Cocok untuk tata letak yang lebih sederhana, seperti menyejajarkan item secara horizontal atau vertikal, dan mudah untuk membuat tampilan responsif. Contoh Implementasi Flexbox:
```
.container {
  display: flex; 
  justify-content: center; /* Pusatkan elemen secara horizontal */
  align-items: center; /* Pusatkan elemen secara vertikal */
}
```

- Grid Layout adalah sistem tata letak dua dimensi yang memungkinkan penempatan elemen di dalam baris dan kolom. Berbeda dengan Flexbox yang bekerja pada satu dimensi, Grid Layout memungkinkan pengaturan elemen secara lebih kompleks dalam dua arah (horizontal dan vertikal).

  Grid Layout berguna untuk mengatur elemen dalam baris dan kolom sekaligus. Cocok untuk tata letak yang lebih kompleks, seperti halaman dengan banyak elemen, dan memberikan lebih banyak kontrol dalam membuat tata letak yang terstruktur.
Contoh Implementasi Grid Layout:
```
.container {
  display: grid; 
  grid-template-columns: 1fr 1fr; /* Membuat dua kolom dengan ukuran yang sama */
  grid-gap: 10px; /* Menambahkan jarak antar kolom */
}
```
 
## 5. Jelaskan bagaimana cara kamu mengimplementasikan checklist di atas secara step-by-step (bukan hanya sekadar mengikuti tutorial)!

a. Tambahkan Meta Viewport untuk Responsivitas:
- Tambahkan tag meta viewport di dalam tag `<head>`.
- Sesuaikan pengaturan viewport untuk mendukung tampilan responsif.

b. Integrasikan Tailwind CSS:
- Tambahkan script CDN Tailwind di bagian `<head>`.
- Pastikan CDN dihubungkan dengan benar untuk menggunakan class Tailwind.

c. Buat Navbar dengan Tailwind:
- Buat file navbar.html dengan struktur HTML menggunakan class Tailwind.
- Sertakan navbar di halaman seperti main.html, edit_product.html, dan create_product_entry.html dengan {% include 'navbar.html' %}.

d. Buat Fitur Edit (Update):
- Tambahkan fungsi edit_product di views.py untuk menangani edit data.
- Buat form di edit_product.html dengan metode POST untuk menyimpan perubahan.
- Tambahkan URL path untuk edit di urls.py.
- Tambahkan tombol "Edit" di main.html untuk setiap product entry.

e. Buat Fitur Hapus (Delete):
- Tambahkan fungsi delete_product di views.py untuk menghapus data.
- Tambahkan URL path untuk delete di urls.py.
- Tambahkan tombol "Delete" di main.html untuk setiap product entry.

f. Testing:
- Jalankan aplikasi dengan python manage.py runserver.
- Uji fitur edit dan delete untuk memastikan berfungsi tanpa error.

g. Git Push:
- Lakukan git add, git commit, dan git push ke GitHub.
- GitHub Actions akan otomatis push ke PWS.

</details>

---

# Tugas 4: Implementasi Autentikasi, Session, dan Cookies pada Django

<details>
<summary>Click for more detail</summary>
<br>

1. Perbedaan antara `HttpResponseRedirect()` dan `redirect()`:
- `HttpResponseRedirect()`: Class yang digunakan untuk mengarahkan pengguna ke URL lain. Dalam penggunaannya, kita harus secara manual memberikan URL tujuan sebagai argumen.
- `redirect()`: Shortcut yang disediakan oleh Django untuk mempermudah pembuatan `HttpResponseRedirect`. Fungsi ini bisa menerima argumen berupa URL, nama view, atau object model.
Perbedaan utamanya adalah `redirect()` lebih fleksibel dan merupakan shorthand untuk `HttpResponseRedirect`.

2. Untuk menghubungkan model Product dengan User, biasanya digunakan relasi ForeignKey atau ManyToManyField. ForeignKey digunakan jika setiap produk hanya dimiliki oleh satu pengguna, sedangkan ManyToManyField digunakan jika sebuah produk bisa dimiliki oleh banyak pengguna, dan setiap pengguna juga bisa memiliki banyak produk. Dengan ForeignKey, setiap objek di model Product terhubung ke satu pengguna saja, menunjukkan hubungan satu-ke-banyak. Sebaliknya, ManyToManyField memungkinkan hubungan banyak-ke-banyak, di mana satu produk dapat dimiliki oleh banyak pengguna, dan setiap pengguna dapat memiliki banyak produk.
```python
# Implementasi pada models.py yang ada pada subdirektori main
...
from django.contrib.auth.models import User
...
class ProductEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE) # Penghubung dengan model User
    ...
```

3. Perbedaan antara authentication dan authorization:
- Authentication: Proses verifikasi identitas pengguna (misalnya, apakah username dan password benar?). Ini terjadi ketika pengguna login.
- Authorization: Setelah pengguna terautentikasi, authorization menentukan hak akses pengguna terhadap sumber daya tertentu (misalnya, apakah pengguna ini boleh mengakses halaman admin?).

Implementasi di Django:
- Authentication: Django menggunakan `django.contrib.auth` untuk mengautentikasi pengguna. Ketika pengguna memasukkan kredensial mereka, Django memverifikasi melalui model User. Jika kredensial cocok, pengguna dianggap terautentikasi.
- Authorization: Django menyediakan decorators seperti `@login_required` dan permission system untuk mengontrol akses ke views tertentu berdasarkan status autentikasi atau hak akses pengguna.

4. Django menggunakan session untuk mengingat pengguna yang telah login. Saat pengguna berhasil login, Django menyimpan session ID pengguna dalam sebuah cookie di browser. Informasi detail mengenai pengguna disimpan di server dalam database session.

Cookies adalah file kecil yang disimpan di browser pengguna, digunakan untuk menyimpan data sesi, preferensi pengguna, dll.
Cookies juga dapat digunakan untuk menyimpan preferensi bahasa, keranjang belanja, atau untuk tracking analitik.
Tidak semua cookies aman. Beberapa cookies (seperti cookies yang digunakan untuk login session) harus ditandai dengan flag HttpOnly dan Secure untuk mencegah akses dari JavaScript dan memastikan hanya dikirim melalui koneksi HTTPS.

5. Cara saya mengimplementasikan checklist step-by-step,

a. Membuat Fungsi Registrasi:
- Impor `UserCreationForm` dan `messages` di views.py.
- Tambahkan fungsi `register()` untuk menangani pembuatan akun pengguna. Fungsi ini menggunakan `UserCreationForm` untuk menampilkan dan memvalidasi form registrasi.
- Jika form valid, data pengguna disimpan, dan pesan sukses ditampilkan menggunakan messages.success. Pengguna kemudian diarahkan ke halaman login setelah registrasi berhasil.

b. Membuat Template HTML untuk Registrasi:
Buat file register.html yang memuat form pendaftaran dengan menggunakan `{{ form.as_table }}` untuk menampilkan form dalam bentuk tabel. Pastikan juga untuk menyertakan CSRF token untuk keamanan.

c. Menghubungkan Fungsi ke URL:
Di urls.py, impor fungsi `register()` dan tambahkan ke dalam urlpatterns untuk menghubungkan URL /register/ dengan fungsi registrasi.

d. Membuat Fungsi Login:
- Impor AuthenticationForm, authenticate, dan login di views.py.
- Tambahkan fungsi `login_user()` untuk menangani autentikasi pengguna. Fungsi ini mengecek apakah form login valid dan melakukan login jika data benar.
- Setelah berhasil login, pengguna diarahkan ke halaman utama (main).

e. Membuat Template HTML untuk Login:
Buat file login.html untuk menampilkan form login. Tambahkan juga link ke halaman registrasi jika pengguna belum memiliki akun.

f. Menghubungkan Login ke URL:
Di urls.py, impor fungsi login_user() dan tambahkan URL /login/ ke dalam urlpatterns.

g. Menambahkan Logout dan Restriksi Akses:
- Tambahkan fungsi `logout_user()` di views.py untuk menghapus sesi pengguna dan mengarahkan mereka kembali ke halaman login setelah logout.
- Gunakan dekorator  `@login_required` pada fungsi show_main() untuk membatasi akses hanya kepada pengguna yang sudah login.

h. Menambahkan Fitur Cookies untuk Last Login:
- Pada fungsi `login_user()`, tambahkan cookie last_login setelah login berhasil menggunakan response.set_cookie(). Di halaman utama, cookie ini ditampilkan untuk menunjukkan kapan terakhir kali pengguna login.
- Pada fungsi logout, hapus cookie last_login menggunakan `response.delete_cookie()`.

i. Menghubungkan Model ProductEntry dengan User:
- Tambahkan ForeignKey ke model ProductEntry untuk mengaitkan product entry dengan pengguna yang membuatnya. Gunakan request.user untuk menetapkan pengguna saat product entry disimpan.
- Ubah query di fungsi show_main() untuk hanya menampilkan product entries milik pengguna yang sedang login dengan memfilter berdasarkan user=request.user.

j. Menerapkan Migrasi:
Jalankan `python manage.py makemigrations` dan `python manage.py migrate` untuk menerapkan perubahan model ke database, termasuk penambahan relasi ForeignKey.

k. Git Push:
- Lakukan git add, git commit, dan git push ke GitHub.
- GitHub Actions akan otomatis push ke PWS.


</details>

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
