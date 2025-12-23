ARSITEKTUR MICROSERVICE BERBASIS DOCKER

Kelompok 8 :
Asti Fadhilah (06240701441)
Abi Yuzaki (062430701438)
Nayla Syahfira Ramadhani (062430701454)

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

