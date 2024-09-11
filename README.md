http://calvin-joy-sipacil.pbp.cs.ui.ac.id/

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
