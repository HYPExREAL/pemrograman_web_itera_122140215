# nilai_mahasiswa.py

def hitung_nilai_akhir(uts, uas, tugas):
    # Rumus: 30% UTS + 40% UAS + 30% Tugas
    return (0.3 * uts) + (0.4 * uas) + (0.3 * tugas)

def tentukan_grade(nilai_akhir):
    if nilai_akhir >= 80:
        return "A"
    elif 70 <= nilai_akhir < 80:
        return "B"
    elif 60 <= nilai_akhir < 70:
        return "C"
    elif 50 <= nilai_akhir < 60:
        return "D"
    else:
        return "E"

def tampilkan_data_mahasiswa(data_mahasiswa):
    print("\n=== DATA NILAI MAHASISWA ===")
    print(f"{'No':<5}{'Nama':<15}{'NIM':<10}{'UTS':<5}{'UAS':<5}{'Tugas':<7}{'Nilai Akhir':<12}{'Grade':<6}")
    print("-" * 70)
    
    for i, mahasiswa in enumerate(data_mahasiswa, start=1):
        nama = mahasiswa["nama"]
        nim = mahasiswa["nim"]
        uts = mahasiswa["uts"]
        uas = mahasiswa["uas"]
        tugas = mahasiswa["tugas"]
        nilai_akhir = mahasiswa["nilai_akhir"]
        grade = mahasiswa["grade"]
        
        print(f"{i:<5}{nama:<15}{nim:<10}{uts:<5}{uas:<5}{tugas:<7}{nilai_akhir:<12.2f}{grade:<6}")

def main():
    # Data mahasiswa
    data_mahasiswa = [
        {"nama": "Budi", "nim": "12345", "uts": 80, "uas": 90, "tugas": 75},
        {"nama": "Ani", "nim": "67890", "uts": 70, "uas": 85, "tugas": 80},
        {"nama": "Citra", "nim": "54321", "uts": 60, "uas": 70, "tugas": 65},
        {"nama": "Dodi", "nim": "98765", "uts": 50, "uas": 60, "tugas": 55},
        {"nama": "Eko", "nim": "11223", "uts": 40, "uas": 50, "tugas": 45},
    ]
    
    # Hitung nilai akhir dan grade
    for mahasiswa in data_mahasiswa:
        nilai_akhir = hitung_nilai_akhir(mahasiswa["uts"], mahasiswa["uas"], mahasiswa["tugas"])
        grade = tentukan_grade(nilai_akhir)
        mahasiswa["nilai_akhir"] = nilai_akhir
        mahasiswa["grade"] = grade
    
    # Tampilkan data mahasiswa
    tampilkan_data_mahasiswa(data_mahasiswa)
    
    # Cari mahasiswa dengan nilai tertinggi dan terendah
    nilai_tertinggi = max(data_mahasiswa, key=lambda x: x["nilai_akhir"])
    nilai_terendah = min(data_mahasiswa, key=lambda x: x["nilai_akhir"])
    
    print("\nMahasiswa dengan Nilai Tertinggi:")
    print(f"Nama: {nilai_tertinggi['nama']}, NIM: {nilai_tertinggi['nim']}, Nilai Akhir: {nilai_tertinggi['nilai_akhir']:.2f}")
    
    print("\nMahasiswa dengan Nilai Terendah:")
    print(f"Nama: {nilai_terendah['nama']}, NIM: {nilai_terendah['nim']}, Nilai Akhir: {nilai_terendah['nilai_akhir']:.2f}")

if __name__ == "__main__":
    main()