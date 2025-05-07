# bmi_calculator.py

def hitung_bmi(berat, tinggi):
    # Rumus BMI: berat / (tinggi * tinggi)
    return berat / (tinggi ** 2)

def kategori_bmi(bmi):
    if bmi < 18.5:
        return "Berat badan kurang"
    elif 18.5 <= bmi < 25:
        return "Berat badan normal"
    elif 25 <= bmi < 30:
        return "Berat badan berlebih"
    else:
        return "Obesitas"

def main():
    print("=== PROGRAM PENGHITUNG BMI ===")
    try:
        berat = float(input("Masukkan berat badan (kg): "))
        tinggi = float(input("Masukkan tinggi badan (m): "))
        
        if berat <= 0 or tinggi <= 0:
            print("Input tidak valid. Berat dan tinggi harus lebih dari 0.")
            return
        
        bmi = hitung_bmi(berat, tinggi)
        kategori = kategori_bmi(bmi)
        
        print("\nHasil Perhitungan:")
        print(f"BMI: {bmi:.2f}")
        print(f"Kategori: {kategori}")
    
    except ValueError:
        print("Input tidak valid. Harap masukkan angka.")

if __name__ == "__main__":
    main()