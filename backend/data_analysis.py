import pandas as pd

# Membaca data dari file CSV
data = pd.read_csv('dataset/data.csv', sep=';')  # Pastikan menggunakan separator yang benar

# Fungsi untuk memprediksi jurusan berdasarkan input
def predict_major(data_input):
    math = int(data_input.get('math', 0))
    science = int(data_input.get('science', 0))
    language = int(data_input.get('language', 0))
    english = int(data_input.get('english', 0))
    social = int(data_input.get('social', 0))
    sports = int(data_input.get('sports', 0))
    arts = int(data_input.get('arts', 0))
    interest = data_input.get('interest', '').lower()

    # Logika prediksi berdasarkan data yang ada
    for index, row in data.iterrows():
        if interest == row['interest'] and math >= row['math'] and science >= row['science'] and language >= row['language'] and english >= row['english'] and social >= row['social'] and sports >= row['sports'] and arts >= row['arts']:
            return row['major']

    # Jika tidak ada kecocokan, kembalikan jurusan umum
    return 'Jurusan Umum'

# Fungsi untuk memberikan rekomendasi jurusan berdasarkan minat
def recommend_major_based_on_interest(interest):
    majors = {
        "sastra": ["Pendidikan Bahasa Indonesia", "Sastra Inggris", "Pendidikan Bahasa Inggris"],
        "pendidikan": ["Pendidikan Guru Sekolah Dasar", "Pendidikan Anak Usia Dini", "Pendidikan Luar Sekolah"],
        "sosial": ["Pendidikan Sejarah", "Pendidikan Geografi"],
        "ekonomi": ["Manajemen", "Akuntansi", "Ekonomi Pembangunan"],
        "kesehatan": ["Pendidikan Jasmani, Kesehatan, dan Rekreasi"],
        "psikologi": ["Bimbingan dan Konseling", "Pendidikan Anak Usia Dini"],
        "olahraga": ["Pendidikan Jasmani, Kesehatan, dan Rekreasi"],
        "seni": ["Musik", "Tari", "Teater dan Drama"],
        "sains": ["Statistika", "Geografi", "Pendidikan Geografi"],
        "teknologi": ["Teknologi Pendidikan", "Teknik Informatika", "Ilmu Komputer"]
    }
    return majors.get(interest, ["Jurusan belum terdefinisi. Silakan konsultasi lebih lanjut."])
