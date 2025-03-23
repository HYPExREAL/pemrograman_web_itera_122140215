// Fungsi untuk kalkulator
function hitungKalkulator(angka1, angka2, operasi) {
    let hasil = 0;
    switch (operasi) {
        case "tambah":
            hasil = angka1 + angka2;
            break;
        case "kurang":
            hasil = angka1 - angka2;
            break;
        case "kali":
            hasil = angka1 * angka2;
            break;
        case "bagi":
            if (angka2 === 0) {
                return "Error: Pembagian dengan nol tidak diperbolehkan";
            }
            hasil = angka1 / angka2;
            break;
        case "pangkat":
            hasil = Math.pow(angka1, angka2);
            break;
        case "akar":
            hasil = Math.sqrt(angka1);
            break;
        case "modulus":
            hasil = angka1 % angka2;
            break;
        default:
            return "Operasi tidak valid";
    }
    return hasil;
}

// Event handler untuk tombol operasi matematika
function setupButtonHandler(buttonId, operasi, operatorSymbol) {
    document.getElementById(buttonId).addEventListener("click", function() {
        const angka1 = parseFloat(document.getElementById("angka1").value);
        const angka2 = parseFloat(document.getElementById("angka2").value);
        
        if (isNaN(angka1) || (operasi !== "akar" && isNaN(angka2))) {
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p class="text-red-500">Masukkan angka yang valid!</p>`;
        } else {
            const hasil = hitungKalkulator(angka1, angka2, operasi);
            document.getElementById("hasil-kalkulator").innerHTML = 
                `<p>Hasil: ${angka1} ${operatorSymbol} ${angka2} = ${hasil}</p>`;
        }
    });
}

// Setup event handlers for each button
setupButtonHandler("btn-tambah", "tambah", "+");
setupButtonHandler("btn-kurang", "kurang", "-");
setupButtonHandler("btn-kali", "kali", "×");
setupButtonHandler("btn-bagi", "bagi", "÷");
setupButtonHandler("btn-pangkat", "pangkat", "^");
setupButtonHandler("btn-modulus", "modulus", "%");

// Special case for square root
document.getElementById("btn-akar").addEventListener("click", function() {
    const angka1 = parseFloat(document .getElementById("angka1").value);
    
    if (isNaN(angka1)) {
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p class="text-red-500">Masukkan angka yang valid!</p>`;
    } else {
        const hasil = hitungKalkulator(angka1, null, "akar");
        document.getElementById("hasil-kalkulator").innerHTML = 
            `<p>Hasil: √${angka1} = ${hasil}</p>`;
    }
});