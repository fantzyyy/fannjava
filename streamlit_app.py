import streamlit as st

# Mengatur konfigurasi halaman dengan ikon dan layout lebar
st.set_page_config(page_title="Portofolio Futuristik Miftahul Irfan Al Barqi", layout="wide")

# Menggunakan HTML dan CSS untuk membuat background gradien
st.markdown("""
    <style>
    /* Background gradien yang futuristik */
    .main {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
    }
    /* Memodifikasi tampilan sidebar */
    .sidebar .sidebar-content {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
    }
    /* Kustomisasi judul dan teks */
    h1, h2, h3, h4, h5, h6 {
        color: #00e6e6;
    }
    p, a, ul {
        color: #e6e6e6;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar Navigasi dengan desain futuristik
st.sidebar.title("🚀 Navigasi")
st.sidebar.write("Navigasikan halaman dengan cepat:")
option = st.sidebar.radio("", ["Beranda", "Tentang Saya", "Riwayat Pendidikan", "Pengalaman", "Kontak"])

# Menampilkan konten berdasarkan navigasi
if option == "Beranda":
    # Salam Pembuka dengan emoji
    st.write("# 🌌 Selamat Datang di Portofolio Futuristik Saya!")
    
    # Foto dan Nama dalam dua kolom
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image("images/isagi.jpg", width=200)  # Ganti dengan path foto kamu
    with col2:
        st.title("Miftahul Irfan Al Barqi")
        st.write("### Mahasiswa Informatika")
        st.write("Saya mahasiswa Informatika di UNU Yogyakarta yang tertarik dengan teknologi, terutama Front-end Development.")

elif option == "Tentang Saya":
    # Tentang Saya
    st.write("# Tentang Saya")
    st.write("""
    Hai, saya Miftahul Irfan Al Barqi! Saya adalah mahasiswa baru Informatika di UNU Yogyakarta. 
    Saya selalu tertarik dengan teknologi dan ingin belajar lebih banyak tentang Front-end Development.
    
    Saya sudah mulai belajar bahasa pemrograman HTML dan CSS, meskipun masih dasar, dan berharap dapat 
    mengembangkan keahlian saya lebih lanjut di bidang ini. Saya juga berharap dapat bertemu dengan orang-orang 
    hebat di bidang ini dan belajar dari mereka.
    """)

elif option == "Riwayat Pendidikan":
    # Riwayat Pendidikan
    st.write("# 🎓 Riwayat Pendidikan")
    st.write("""
    - SD Anggarudin 02
    - SD Candigaron 02
    - SMP Albadar
    - MA YPPA Cipulus
    - Yayasan Pondok Pesantren Al-Hikamussalafiyah, Cipulus Wanayasa Purwakarta
    - Sedang kuliah di UNU Yogyakarta
    """)

elif option == "Pengalaman":
    # Pengalaman
    st.write("# 📚 Pengalaman")
    st.write("Mengikuti program kursus Bahasa Inggris di MR. Bob")

elif option == "Kontak":
    # Kontak
    st.write("# 📞 Kontak")
    st.write("Hubungi saya melalui media sosial atau WhatsApp:")
    st.write("Instagram: [irfanalbarqi](https://instagram.com/irfanalbarqi)")
    st.write("WhatsApp: 0895338383577")

# Footer
st.write("---")
st.write("#### Terima kasih telah mengunjungi portofolio saya!")
