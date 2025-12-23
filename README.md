ARSITEKTUR MICROSERVICE BERBASIS DOCKER (PRAKTEK SISTEM OPERASI)

Kelompok 8 :
- Asti Fadhilah (06240701441)
- Abi Yuzaki (062430701438)
- Nayla Syahfira Ramadhani (062430701454)

`Pendahuluan`
Dokumen ini merupakan dokumentasi instalasi dan penggunaan dari proyek Arsitektur Microservices Berbasis Docker. Dokumentasi ini dibuat untuk menjelaskan proses mulai dari persiapan lingkungan, instalasi, hingga penggunaan aplikasi microservices yang telah dibuat. Proyek ini dikembangkan sebagai bagian dari tugas mata kuliah Sistem Operasi dengan tujuan memahami konsep microservices, Docker, Docker Compose, dan REST API.

`Tujuan Projek`
Tujuan dari proyek ini adalah:
- Menerapkan konsep arsitektur microservices
- Menjalankan beberapa service secara terpisah (independen)
- Menggunakan Docker sebagai container
- Menghubungkan antar service menggunakan REST API

`Deskripsi Sistem`
Dalam sistem ini terdiri dari 2 microservice, yaitu :
- user service yang menyediakan data penggunaan dan mengambil data produk dari product service melalui REST API
- product service yang menyediakan data produk berupa nama, harga dan stok
Kedua service ini berjalan secara mandiri di dalam container Docker yang berbeda, namun dapat saling berkomunikasi melalui HTTP request.

`Teknologi yang digunakan`
- Docker Desktop
- Docker Compose
- Python
- Flask (REST API)
- Visual Studio Code

`Struktur Folder Proyek`
microservice-docker/
├── user-service/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
├── product-service/
│ ├── app.py
│ ├── Dockerfile
│ └── requirements.txt
└── docker-compose.yml

`1. Instalasi Docker`
Unduh dan instal Docker Desktop sesuai dengan sistem operasi yang digunakan. Pastikan Docker berhasil dijalankan.
Cek Instalasi Docker melalui terminal dengan perintah :
   docker --versiom
   docker compose version
Jika perintah diatas berhasil menampilkan versi Docker, maka Docker telah terinstal dengan benar.

`2. Menyiapkan Folder Proyek`
- menyiapkan folder proyek dengan nama microservice
- didalam folder microservice tersebut buat folder user service dan product service
- letakkan folder tersebut di direktori lokal komputer
- buka folder menggunakan visual studio code

`3. Instalasi dan menjalankan aplikasi`
a. Masuk ke folder proyek
   Buka terminal pada folder utama proyek : cd microservice-docker
b. Membuat Product Service
   Pada file pertama yaitu file app.py yang berisi REST API untuk menampilkan data produk. Untuk file requirements.txt itu berisikan flask yang mana flask tersebut sudah terinstal didalam visual codenya. Dan yang terakhir didalam file Dockerfile. Isi file file berikut bisa dilihat di Github ini.
c. Membuat User Service
   Pada file pertama yaitu file app.py yang menyediakan data user dan mengambil data produk dari Product Service. Untuk file requirements.txt itu berisikan flask dan requests untuk menghubungkan REST API pada product service. Dan yang terakhir didalam Dockerfile. Isi file berikut bisa dilihat di Github ini.
d. Menjalankan seluruh service
   Untuk menjalankan folder utama proyek ini jalankan perintah berikut :
   docker compose up --build
   Jika berhasil, maka kedua service akan berjalan bersamaan. Untuk menghentikan seluruh container, tekan CTRL+C atau gunakan perintah :
   docker compose down
`Output aplikasi`
Setelah seluruh service berhasil dijalankan menggunakan Docker compose, sistem akan menghasilkan output berupa API yang dapat diakses melalui browser.
- User Service output
  user service berjalan secara mandiri dan dapat diakses melalui browser pada endpoint berikut :
  http://localhost:5001/users
  ketika endpoint tersebut diakses, browser akan menampilkan data dalam format JSON. Output tersebut menunjukkan bahwa user service aktif dan berjalan dengan baik, serta mampu mengembalikan data sesuai dengan endpoint yang disediakan.
- Product Service output
  product service juga berjalan secara mandiri dan dapat diakses melalui browser pada endpoint berikut :
  http://localhost:5002/products
  Output ini menandakan bahwa product service berhasil berjalan secara independen dan mampu menyajikan data produk dalam format JSON.
- Output komunikasi antar service
  sebagai bentuk implementasi API saling terhubung. User service melakukan request ke Product service menggunakan REST API. Endpoint berikut digunakan untuk menguji komunikasi antar service :
  http://localhost:5001/user-with-products
  Output ini membuktikan bahwa setiap service berjalan sendiri, antar service saling terhubung melalui REST API, dan arsitektur microservice berhasil diterapkan.
- Log service
  selain melalui browser, status service juga dapat dilihat melalui terminal saat menjalankan perintah :
  docker compose up
  Jika service berjalan dengan baik, maka akan muncul log seperti :
  * Running in http://127.0.0.1:5000
  Log tersebut menandakan bahwa aplikasi Flask berhasil dijalankan didalam container Docker.

`Kesimpulan`
Berdasarkan hasil implementasi dan pengujian yang telah dilakukan, dapat disimpulkan bahwa arsitektur Microservices berbasis Docker berhasil diterapkan dengan baik pada proyek ini. Sistem dibangun dengan memisahkan aplikasi menjadi beberapa service, yaitu User Service dan Product Service, yang masing-masing berjalan secara mandiri dalam container Docker yang terpisah.
Setiap service memiliki tanggung jawabnya sendiri dan dapat dijalankan, dikembangkan, serta dikelola secara independen tanpa bergantung langsung pada service lain. Komunikasi antar service dilakukan menggunakan REST API, di mana User Service dapat mengambil data dari Product Service melalui endpoint API yang telah disediakan. Hal ini menunjukkan bahwa prinsip dasar microservices, yaitu loose coupling dan service-to-service communication, telah terpenuhi.
Penggunaan Docker Compose mempermudah proses orkestrasi dan manajemen beberapa service secara bersamaan, mulai dari proses build image, pembuatan container, hingga pengaturan jaringan antar service. Dengan demikian, sistem menjadi lebih terstruktur, mudah dijalankan, serta konsisten di berbagai lingkungan.

`Penutup`
Dengan proyek ini diharapkan dapat memberikan pemahaman dasar mengenai konsep arsitektur microservices, penggunaan Docker dan Docker Compose, serta penerapan REST API dalam membangun sistem terdistribusi sederhana. Implementasi ini dapat dijadikan sebagai fondasi untuk mengembangkan sistem yang lebih kompleks dimasa depan, seperti penambahan service baru, integrasi database, maupun penerapan autentikasi dan keamanan API.
Dengan selesainya proyek ini, diharapkan mahasiswa mampu memahami bagaiman sebuah aplikasi dapat dipecah menjadi beberapa service yang saling terhubung namun tetap berjalan secara independen, sesuai dengan konsep microservices yang banyak digunakan pada sistem modern saat ini.
