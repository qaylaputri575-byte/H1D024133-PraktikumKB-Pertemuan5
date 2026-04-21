Sistem Pakar Diagnosa Penyakit THT

## Deskripsi Program

Program ini merupakan sistem GUI berbasis Python Tkinter untuk membantu melakukan diagnosa awal penyakit THT berdasarkan gejala yang dipilih oleh pengguna.

Sistem akan membandingkan gejala yang dipilih dengan basis pengetahuan yang terdapat pada modul, kemudian menampilkan:

* hasil diagnosa utama
* persentase kecocokan
* daftar gejala yang cocok
* ranking kemungkinan penyakit lainnya

## Fitur Program

* Menampilkan daftar gejala THT dari G1 sampai G37
* Pengguna dapat memilih lebih dari satu gejala
* Tombol Diagnosa untuk memproses hasil
* Tombol Reset untuk menghapus pilihan
* Menampilkan hasil diagnosa berdasarkan kecocokan gejala
* Menampilkan ranking semua kemungkinan penyakit

## Tools dan Bahasa yang Digunakan

* **Python**
* **Tkinter** sebagai GUI

## Struktur File

```text
NIM-PraktikumKB-Pertemuan5/
├── main.py
└── README.md
```

## Cara Menjalankan Program

1. Pastikan Python sudah terpasang di komputer.
2. Download atau clone repository ini.
3. Jalankan file `main.py` dengan perintah berikut:

```bash
python main.py
```

## Cara Menggunakan

1. Jalankan program.
2. Pilih gejala yang dialami pasien dengan mencentang checkbox.
3. Klik tombol **Diagnosa**.
4. Sistem akan menampilkan hasil penyakit yang paling mungkin beserta persentase kecocokannya.
5. Klik tombol **Reset** jika ingin mengulang diagnosa.

## Metode Diagnosa

Metode yang digunakan pada program ini adalah **pencocokan gejala (rule-based matching)**.

Langkah kerja sistem:

1. Pengguna memilih gejala yang dialami.
2. Sistem membandingkan gejala tersebut dengan data gejala pada setiap penyakit.
3. Sistem menghitung jumlah gejala yang cocok.
4. Sistem menghitung persentase kecocokan dengan rumus:

```text
Persentase Kecocokan = (Jumlah Gejala Cocok / Total Gejala Penyakit) x 100%
```

5. Penyakit dengan nilai kecocokan tertinggi ditampilkan sebagai hasil diagnosa utama.



