import streamlit as st
import pandas as pd
import numpy as np

# Judul aplikasi
st.title("Menggunakan Obrolan di Streamlit dengan Dataset Spine")
st.write("Saya menggunakan Streamlit untuk menampilkan grafik dari dataset spine")

# Menggunakan st.file_uploader untuk upload file CSV
uploaded_file = st.file_uploader("Pilih file CSV untuk diunggah", type=["csv"])

# Cek apakah ada file yang diunggah
if uploaded_file is not None:
    # Membaca file CSV
    df_spine = pd.read_csv(uploaded_file, encoding="iso-8859-1")
    
    # Menampilkan informasi dasar tentang dataframe
    st.write("Statistik data:")
    st.write(df_spine.describe())
    
    # Mendapatkan unique diagnosis atau jenis penyakit (misalkan kolomnya 'DIAGNOSIS')
    diagnosis = df_spine["DIAGNOSIS"].unique()
    
    # Membuat DataFrame dengan TanggalKunjungan sebagai index dan diagnosis sebagai kolom
    # Misalnya, kolom TanggalKunjungan dan JumlahPasien
    df_diagnosis_data = df_spine.pivot_table(values='JUMLAHPASIEN', index='TANGGALKUNJUNGAN', columns='DIAGNOSIS', fill_value=0)
    
    # Membuat Area Chart
    st.title("Area Chart")
    st.area_chart(df_diagnosis_data)
    
    # Membuat Line Chart
    st.title("Line Chart")
    st.line_chart(df_diagnosis_data)
    
    # Membuat Bar Chart
    st.title("Bar Chart")
    st.bar_chart(df_diagnosis_data)
    
else:
    st.write("Silakan unggah file CSV untuk melihat isi dan statistiknya.")

# Tambahkan footer atau pemisah
st.markdown("---")
