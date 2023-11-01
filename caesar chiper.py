def caesar_cipher(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            # Tentukan apakah karakter adalah huruf besar atau huruf kecil
            is_upper = char.isupper()
            
            # Konversi karakter ke indeks ASCII (0-25) untuk A-Z atau a-z
            char_index = ord(char) - ord('A') if is_upper else ord(char) - ord('a')
            
            # Enkripsi karakter
            encrypted_index = (char_index + shift) % 26
            
            # Konversi indeks terenkripsi ke karakter
            encrypted_char = chr(encrypted_index + ord('A')) if is_upper else chr(encrypted_index + ord('a'))
            
            encrypted_text += encrypted_char
        else:
            # Jika karakter bukan huruf, biarkan seperti itu
            encrypted_text += char
    return encrypted_text

def caesar_decipher(text, shift):
    return caesar_cipher(text, -shift)

def encrypt_student_data(student_data, shift):
    encrypted_data = []
    for student in student_data:
        encrypted_student = {}
        for key, value in student.items():
            encrypted_value = caesar_cipher(str(value), shift)
            encrypted_student[key] = encrypted_value
        encrypted_data.append(encrypted_student)
    return encrypted_data

def decrypt_student_data(encrypted_student_data, shift):
    decrypted_data = []
    for student in encrypted_student_data:
        decrypted_student = {}
        for key, value in student.items():
            decrypted_value = caesar_decipher(str(value), shift)
            decrypted_student[key] = decrypted_value
        decrypted_data.append(decrypted_student)
    return decrypted_data

# Contoh data mahasiswa
student_data = [
    {
        'Nama': 'FACHRUL BUDI',
        'NIM': '12096087',
        'Kelas': 'X-TI',
        'Jenis Kelamin': 'Laki-laki',
        'Pilihan': 'Kandidat 1',
    },
    {
        'Nama': 'PERMANA',
        'NIM': '12098760',
        'Kelas': 'X-TI',
        'Jenis Kelamin': 'Laki-Laki',
        'Pilihan': 'Kandidat 2',
    },
    {
        'Nama': 'HUSNI ANGRIANI',
        'NIM': '12345678',
        'Kelas': 'X-SI',
        'Jenis Kelamin': 'PEREMPUAN',
        'Pilihan': 'Kandidat 3',
    },
]

shift_value = 3  # Ganti nilai ini sesuai dengan shift yang diinginkan

# Enkripsi data mahasiswa
encrypted_student_data = encrypt_student_data(student_data, shift_value)
print("Data mahasiswa terenkripsi:", encrypted_student_data)

# Dekripsi data mahasiswa
decrypted_student_data = decrypt_student_data(encrypted_student_data, shift_value)
print("Data mahasiswa terdekripsi:", decrypted_student_data)
