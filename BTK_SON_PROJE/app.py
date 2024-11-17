import streamlit as st
import pandas as pd
import joblib  # Modeli yüklemek için kullanılır

# Başlık ve açıklama
st.title("Housing Prices Tahmin Uygulaması")
st.write("Bu uygulama, ev özelliklerine göre tahmini fiyatı hesaplar. Özellikleri sol tarafta girin ve sonucu görün.")

# Kullanıcı girdilerini al (Kenar çubuğu)
st.sidebar.header("Ev Özelliklerini Girin:")
GrLivArea = st.sidebar.number_input("GrLivArea (m²):", min_value=500, max_value=5000, step=50, value=1500)
LotArea = st.sidebar.number_input("LotArea (m²):", min_value=1000, max_value=20000, step=100, value=7500)
OverallQual = st.sidebar.slider("OverallQual (Genel Kalite, 1-10):", min_value=1, max_value=10, value=5)
YearBuilt = st.sidebar.number_input("YearBuilt (Yapım Yılı):", min_value=1800, max_value=2024, step=1, value=2000)

# Yeni tahmin için özellikleri bir araya getir
new_data = {
    'GrLivArea': GrLivArea,
    'LotArea': LotArea,
    'OverallQual': OverallQual,
    'YearBuilt': YearBuilt
}
new_data_df = pd.DataFrame([new_data])

# Modeli yükle ve tahmin yap
try:
    # Modeli yükle (modeli kaydettiğin adı burada kullan)
    model = joblib.load('housing_price_model.pkl')

    # Eğitim sırasında kullanılan sütunları yükle
    feature_columns = joblib.load('feature_columns.pkl')
    
    # Yeni veri setini bu sütunlara göre düzenle
    new_data_df = new_data_df.reindex(columns=feature_columns, fill_value=0)
    
    # Tahmin yap
    prediction = model.predict(new_data_df)
    predicted_price = prediction[0]

    # Sonucu göster
    st.subheader("Tahmin Sonuçları")
    st.write(f"Tahmini Ev Fiyatı: ${predicted_price:,.2f}")

except FileNotFoundError:
    st.error("Model dosyası bulunamadı! Lütfen modeli 'housing_price_model.pkl' olarak kaydet ve aynı dizine koy.")
