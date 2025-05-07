# main.py

# Mengimpor modul secara keseluruhan
import math_operations as mo

# Mengimpor fungsi tertentu dari modul
from math_operations import celsius_ke_fahrenheit, celsius_ke_kelvin

def main():
    print("=== PROGRAM MATEMATIKA PYTHON ===")
    
    # Geometri
    sisi = 5
    panjang = 10
    lebar = 4
    radius = 7
    
    print("\nPerhitungan Geometri:")
    print(f"Luas Persegi (sisi={sisi}): {mo.luas_persegi(sisi)}")
    print(f"Keliling Persegi (sisi={sisi}): {mo.keliling_persegi(sisi)}")
    print(f"Luas Persegi Panjang (panjang={panjang}, lebar={lebar}): {mo.luas_persegi_panjang(panjang, lebar)}")
    print(f"Keliling Persegi Panjang (panjang={panjang}, lebar={lebar}): {mo.keliling_persegi_panjang(panjang, lebar)}")
    print(f"Luas Lingkaran (radius={radius}): {mo.luas_lingkaran(radius):.2f}")
    print(f"Keliling Lingkaran (radius={radius}): {mo.keliling_lingkaran(radius):.2f}")
    
    # Konversi suhu
    celsius = 25
    print("\nKonversi Suhu:")
    print(f"{celsius}°C = {celsius_ke_fahrenheit(celsius):.2f}°F")
    print(f"{celsius}°C = {celsius_ke_kelvin(celsius):.2f}K")

if __name__ == "__main__":
    main()