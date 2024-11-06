import streamlit as st

# Salam Pembuka
st.write("Halo, selamat datang di portofolio saya!")

# Foto Profil
st.image("images/isagi.jpg", width=150)  # Ganti dengan path ke foto kamu

# Nama
st.title("Miftahul Irfan Al Barqi")

# Tentang Saya
st.header("Tentang Saya")
st.write("""
Hai, saya Miftahul Irfan Al Barqi! Saya adalah mahasiswa baru Informatika di UNU Yogyakarta. 
Saya selalu tertarik dengan teknologi dan ingin belajar lebih banyak tentang Front-end Development. 
Saya sudah mulai belajar bahasa pemrograman HTML dan CSS, meskipun masih dasar, dan berharap dapat 
mengembangkan keahlian saya lebih lanjut di bidang ini. Saya juga berharap dapat bertemu dengan orang-orang 
hebat di bidang ini dan belajar dari mereka.
""")

# Kontak
st.header("Kontak")
st.write("Instagram: [irfanalbarqi](https://instagram.com/irfanalbarqi)")
st.write("WhatsApp: 0895338383577")

# Riwayat Pendidikan
st.header("Riwayat Pendidikan")
st.write("""
- SD Anggarudin 02
- SD Candigaron 02
- SMP Albadar
- MA YPPA Cipulus
- Yayasan Pondok Pesantren Al-Hikamussalafiyah, Cipulus Wanayasa Purwakarta
- Sedang kuliah di UNU Yogyakarta
""")

# Pengalaman
st.header("Pengalaman")
st.write("Mengikuti program kursus Bahasa Inggris di MR. Bob")

