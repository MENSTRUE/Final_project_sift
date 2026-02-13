# 🔍 Perbandingan SIFT dan ORB untuk Deteksi dan Pencocokan Fitur

Proyek ini mengimplementasikan dan membandingkan dua algoritma populer dalam Computer Vision:

- **SIFT (Scale-Invariant Feature Transform)**
- **ORB (Oriented FAST and Rotated BRIEF)**

Tujuan dari proyek ini adalah untuk menganalisis perbedaan performa kedua metode berdasarkan:

- Jumlah keypoints yang terdeteksi
- Jumlah good matches
- Inlier ratio menggunakan RANSAC
- Waktu eksekusi

---

## 📌 Latar Belakang

Deteksi fitur merupakan bagian penting dalam berbagai aplikasi Computer Vision seperti:

- Image stitching
- Pembuatan panorama
- Pengenalan objek
- Rekonstruksi 3D

SIFT dikenal memiliki ketahanan terhadap perubahan skala dan rotasi, sedangkan ORB dirancang agar lebih cepat dan efisien untuk kebutuhan komputasi real-time.

Proyek ini melakukan perbandingan secara kuantitatif dan visual terhadap kedua metode tersebut.

---

## 🧠 Metodologi

### 1️⃣ SIFT
- Menggunakan Difference of Gaussian (DoG) untuk deteksi keypoint
- Descriptor berdimensi 128
- Invariant terhadap skala dan rotasi

### 2️⃣ ORB
- Menggunakan FAST sebagai detektor keypoint
- Menggunakan BRIEF sebagai descriptor biner
- Lebih cepat dibandingkan SIFT

### 3️⃣ Feature Matching
- Menggunakan Brute Force Matcher (BFMatcher)
- Menggunakan Lowe’s Ratio Test (threshold 0.75)

### 4️⃣ Estimasi Homografi
- Menggunakan algoritma RANSAC
- Menghitung jumlah inlier
- Menghitung inlier ratio sebagai evaluasi akurasi pencocokan

---

## 📂 Struktur Folder

```
Final_project/
│
├── images/
│   ├── img1.jpeg
│   └── img2.jpeg
│
├── outputs/
│   ├── SIFT_keypoints_img1.png
│   ├── SIFT_keypoints_img2.png
│   ├── SIFT_matching.png
│   ├── ORB_keypoints_img1.png
│   ├── ORB_keypoints_img2.png
│   ├── ORB_matching.png
│   └── comparison_results.csv
│
├── compare_sift_orb.py
└── README.md
```

---

## ⚙️ Instalasi

Pastikan menggunakan Python 3.10.

Install dependensi berikut:

```bash
pip install opencv-contrib-python==4.8.1.78
pip install numpy==1.26.4
pip install pandas
pip install matplotlib
```

---

## ▶️ Cara Menjalankan Program

1. Letakkan dua gambar yang ingin dibandingkan ke dalam folder `images/`.
2. Jalankan perintah berikut:

```bash
python compare_sift_orb.py
```

3. Semua hasil akan otomatis tersimpan di dalam folder `outputs/`.

---

## 📊 Output yang Dihasilkan

Program akan menghasilkan:

- Visualisasi keypoints pada masing-masing gambar
- Visualisasi hasil feature matching
- File CSV berisi hasil evaluasi kuantitatif

Contoh hasil:

| Method | Keypoints Img1 | Keypoints Img2 | Good Matches | Inlier Ratio | Time (s) |
|--------|----------------|----------------|--------------|--------------|----------|
| SIFT   | 1031           | 1368           | 193          | 0.549        | 0.554    |
| ORB    | 1000           | 1000           | 160          | 0.462        | 0.391    |

---

## 📈 Kesimpulan Sementara

- SIFT menghasilkan jumlah good matches dan inlier ratio yang lebih tinggi.
- ORB memiliki waktu eksekusi yang lebih cepat.
- Terdapat trade-off antara ketahanan (robustness) dan efisiensi komputasi.

---

## 📚 Referensi

- D. G. Lowe, “Distinctive Image Features from Scale-Invariant Keypoints,” IJCV, 2004.
- R. Szeliski, *Computer Vision: Algorithms and Applications*, Springer.
- Bradski & Kaehler, *Learning OpenCV*.

---

## 👨‍🎓 Penulis

Wafa Syaefurokhman  
Final Project – Computer Vision  
Universitas Darussalam Gontor
