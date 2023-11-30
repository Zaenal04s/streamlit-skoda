import pickle
import streamlit as st

model = pickle.load(open('estimasi_mobil_skoda.sav', 'rb'))

st.title('Estimasi Harga Mobil Bekas')

year = st.number_input('Input Tahun Mobil')
mileage = st.number_input('Input Kilometer Mobil')
tax = st.number_input('Input Pajak Mobil')
mpg = st.number_input('Input Konsumsi BBM Mobil')
engineSize = st.number_input('Input engineSize')

predict = ''

if st.button('Estimasi Harga'):
    predict = model.predict(
        [[year, mileage, tax, mpg, engineSize]]
    )
    st.write ('Estimasi harga mobil bekas dalam ponds : ', predict)
    st.write ('Estimasi harga mobil bekas dalam IDR (Juta) : ', predict*19000)
    
# How to run streamlit in file terminal: streamlit run namaFile.py