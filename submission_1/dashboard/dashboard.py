import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import io

# Fungsi untuk visualisasi hubungan antara suhu dan jumlah sewa sepeda berdasarkan musim
def plot_temp_vs_rental(hourly_data):
    plt.figure(figsize=(10, 6))
    sns.scatterplot(data=hourly_data, x='temp', y='cnt', hue='season')
    plt.title('Hubungan antara Suhu dan Jumlah Sewa Sepeda berdasarkan Musim')
    plt.xlabel('Suhu (Celsius)')
    plt.ylabel('Jumlah Sewa Sepeda')
    plt.legend(title='Musim')
    # Simpan gambar ke dalam buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Tampilkan gambar di dalam dashboard
    st.image(buf)

# Fungsi untuk visualisasi pengaruh hari libur terhadap jumlah sewa sepeda
def plot_holiday_vs_rental(hourly_data):
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=hourly_data, x='holiday', y='cnt')
    plt.title('Pengaruh Hari Libur terhadap Jumlah Sewa Sepeda')
    plt.xlabel('Hari Libur')
    plt.ylabel('Jumlah Sewa Sepeda')
    plt.xticks([0, 1], ['Bukan Hari Libur', 'Hari Libur'])
    # Simpan gambar ke dalam buffer
    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    buf.seek(0)
    # Tampilkan gambar di dalam dashboard
    st.image(buf)

# Memuat data
hourly_data = pd.read_csv('hour.csv')
# Ubah kolom 'dteday' menjadi tipe data datetime
hourly_data['dteday'] = pd.to_datetime(hourly_data['dteday'])
# Menghapus baris dengan nilai kosong
hourly_data.dropna(inplace=True)

# Memanggil fungsi-fungsi visualisasi di dalam dashboard
st.title('Dashboard Analisis Sewa Sepeda')
st.header('Visualisasi 1: Hubungan antara Suhu dan Jumlah Sewa Sepeda berdasarkan Musim')
plot_temp_vs_rental(hourly_data)

st.header('Visualisasi 2: Pengaruh Hari Libur terhadap Jumlah Sewa Sepeda')
plot_holiday_vs_rental(hourly_data)
