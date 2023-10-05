import math

def hitung_tinggi_tiang_bendera(sudut, langkah, ukuran_sepatu, tinggi_badan):
    sudut_radian = math.radians(sudut)
    tinggi_tiang_cm = math.tan(sudut_radian) * langkah * ukuran_sepatu + tinggi_badan
    tinggi_tiang_m = tinggi_tiang_cm / 100
    return tinggi_tiang_cm, tinggi_tiang_m

def main():
    sudut = int(input("Masukkan sudut dalam derajat: "))
    langkah = int(input("Masukkan hitungan langkah dari objek pengamatan (cm): "))
    ukuran_sepatu = int(input("Masukkan ukuran sepatu (cm): "))
    tinggi_badan = int(input("Masukkan tinggi badan (cm): "))

    tinggi_tiang_cm, tinggi_tiang_m = hitung_tinggi_tiang_bendera(sudut, langkah, ukuran_sepatu, tinggi_badan)

    print("Tinggi tiang bendera adalah:", tinggi_tiang_cm, "cm atau sekitar:", round(tinggi_tiang_m, 2), "m")

if __name__ == "__main__":
    main()
