# PERHITUNGAN TINGGI TIANG BENDERA SEKOLAH MENGGUNAKAN TRIGONOMETRI DAN KOMPUTER

I. Pendahuluan

Tinggi tiang bendera adalah informasi penting dalam berbagai konteks, seperti merencanakan pencahayaan, konstruksi, atau perencanaan acara. Dalam laporan ini, akan dijelaskan metode perhitungan tinggi tiang bendera sekolah dengan memanfaatkan sudut pengamatan, jarak dari pengamatan, dan trigonometri, serta implementasinya dengan bantuan komputer.

II. Tujuan

Tujuan dari laporan ini adalah memberikan pemahaman tentang bagaimana kita dapat menggunakan prinsip-prinsip trigonometri dan perangkat komputer untuk menghitung tinggi tiang bendera sekolah dengan hasil yang mendekati. Saya juga akan memberikan contoh implementasi menggunakan bahasa pemrograman Python.

III. Batasan Masalah

Dalam penentuan tinggi tiang bendera sekolah, saya mempertimbangkan batasan-batasan berikut:

1. Hanya informasi yang tersedia adalah sudut pengamatan (dalam derajat), jarak dari pengamatan (dalam satuan yang sama dengan tinggi badan), dan tinggi badan pengamat (dalam satuan yang sama dengan jarak).

2. Faktor-faktor lain seperti ketinggian tempat atau kemiringan tanah diabaikan dalam perhitungan.

3. Tinggi tiang bendera diukur dari dasar tiang hingga ujung bendera yang berkibar.

4. Perhitungan menggunakan prinsip trigonometri dan bantuan komputer.

IV. Metode Perhitungan

Untuk menghitung tinggi tiang bendera sekolah, kita dapat menggunakan rumus trigonometri berikut:

tinggi_tiang = tan(sudut) * jarak + tinggi_badan

di mana:
- sudut adalah sudut pengamatan (dalam derajat).
- jarak adalah jarak dari pengamatan ke tiang bendera (dalam satuan yang sama dengan tinggi_badan).
- tinggi_badan adalah tinggi badan pengamat (dalam satuan yang sama dengan jarak).

Hasil perhitungan ini akan dalam satuan yang sama dengan tinggi_badan, sehingga biasanya diukur dalam meter.

V. Contoh Perhitungan

Sebagai contoh, mari kita hitung tinggi tiang bendera sekolah dengan informasi berikut:
- Sudut pengamatan (sudut) adalah 49 derajat.
- Jarak dari pengamatan (jarak) adalah 3.75 meter.
- Tinggi badan pengamat (tinggi_badan) adalah 1.6 meter.

Maka perhitungannya adalah sebagai berikut:

tinggi_tiang = tan(49) * 3.75 + 1.6
tinggi_tiang ≈ 6 meter
