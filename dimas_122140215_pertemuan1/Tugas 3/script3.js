document.getElementById("registrationForm").addEventListener("submit", function(event) {
    event.preventDefault(); // Mencegah form dari pengiriman default

    const name = document.getElementById("name").value;
    const email = document.getElementById("email").value;
    const password = document.getElementById("password").value;
    const validationMessage = document.getElementById("validationMessage");

    // Validasi
    const isValid = validateForm(name, email, password);

    if (isValid) {
        validationMessage.innerHTML = "<p class='text-green-500'>Form berhasil divalidasi!</p>";
        // Di sini Anda bisa melanjutkan untuk mengirim data ke server atau melakukan tindakan lain
    } else {
        validationMessage.innerHTML = "<p class='text-red-500'>Terdapat kesalahan dalam form. Silakan periksa kembali.</p>";
    }
});

function validateForm(name, email, password) {
    let isValid = true;

    // Validasi nama
    if (name.length <= 3) {
        isValid = false;
        alert("Nama harus lebih dari 3 karakter.");
    }

    // Validasi email
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!emailPattern.test(email)) {
        isValid = false;
        alert("Email tidak valid.");
    }

    // Validasi password
    if (password.length < 8) {
        isValid = false;
        alert("Password harus minimal 8 karakter.");
    }

    return isValid;
}