import pandas as pd
import streamlit as st
from PIL import Image

st.set_page_config(layout='centered')
df = pd.read_excel("./all.xls", engine='openpyxl')

st.title("INSIGHTS MENGENAI MEREK DAGANG PDKI")

with st.container():
    st.header("Latar Belakang")
    st.markdown("""
    Tahukah anda mengenai issue yang sedang hangat dibicarakan, **Citayam Fashion Week** ?
    Yap, baru-baru ini sedang ramai karena Baim Wong melalui PT. Tiger Wong Entertainment dan Indigo Aditya Nugroho mengklaim dengan mendaftarkan merek Citayam Fashion Week ke PDKI.
    Hal ini tentu menuai kemarahan publik, walaupun pada akhirya kedua permohonan dicabut kembali.
    """)

    cfwImage = Image.open("./cfw.png")
    st.image(cfwImage, caption="Permohonan untuk Merek Citayam Fashion Week")

    st.markdown("""
    Dari situlah kemudian ide dari jurnal ini bermula. Dengan 50.714 data merek dagang dari PDKI, jurnal ini mencoba memberikan gambaran mengenai analisa terkait data merek dagang PDKI.
    Dan berikut beberapa _insights_ yang berhasil ditemukan.
    """)

with st.container():
    st.header("Analisa Data Permohonan Merek Dagang")
    st.markdown("Berikut data metrix dari keseluruhan total data yang didapatkan")


with st.container():
    st.subheader("Data Metrix")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric(
            label="Total",
            value=df['id'].count()
            )
    with col2:
        st.metric(
            label="Aktif",
            value=df.groupby("sg_grup")['id'].count()['Didaftar']
            )
    with col3:
        st.metric(
            label="Ditolak",
            value=df.groupby("sg_grup")['id'].count()['Ditolak']
            )

with st.container():
    st.subheader("Data Merek Dagang")
    
    trademarkName = st.text_input("Nama Merek / Nomor Permohonan")
    
    filteredQuery = ""
    if trademarkName:
        filteredQuery = "nama_merek.str.contains(@trademarkName, na=False) | nomor_permohonan == @trademarkName"
    
    if(filteredQuery != ""):
        filteredDf = df.query(filteredQuery, engine='python')
    else:
        filteredDf = df
    
    st.dataframe(filteredDf[['nama_merek', 'nomor_permohonan', 'status_permohonan', 'sg_grup', 'owner_name']].head(50))

with st.container():
    dfProvince = pd.read_csv("./per_province.csv")
    st.subheader("Permohonan Per Provinsi")
    st.markdown("""
    Berikut adalah list masing-masing provinsi beserta detail jumlah negara asal pemilik, total permohonan, jumlah merek dagang yang aktif, dan persentase jumlah aktif terhadap keseluruhan jumlah permohonan.
    """)
    
    st.dataframe(dfProvince)

with st.container():
    dfClass = pd.read_csv("./per_class.csv")
    st.subheader("Permohonan Terbanyak Per Status")
    st.markdown("""
    Berikut list class / kategori 3 terbanyak di masing-masing status.
    """)
    
    st.dataframe(dfClass)

with st.container():
    st.header("Kesimpulan")
    st.markdown("""
    Dari analisa ini bisa disimpulkan bahwa angka kesadaran dan inisiatif untuk mendaftarkan merek dagang ke PDKI sudah sangat baik. Dan hal itu diimbangi pula dengan selektifnya pihak PDKI dalam menentukan apakah sebuah merek dagang sudah memenuhi kriteria merek dagang yang baik dan legal atau belum.
    """)