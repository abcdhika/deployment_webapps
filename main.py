import streamlit as st
import pandas as pd
import numpy as np

st.title ("APLIKASI PERHITUNGAN MOLARITAS")

bobot = st.number_input ('Masukan Nilai Bobot')
volume = st.number_input ('Masukan Nilai Volume')
mr = st.number_input ('Masukan Nilai Mr')

tombol = st.button ('Hitung Nilai Molaritas')

if tombol :
    nilai_molaritas = bobot/(mr*volume)
    st.success (f'Nilai Molaritas adalah {nilai_molaritas}')