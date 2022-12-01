import streamlit as sl
try:
    sl.write("Nama: ", sl.session_state["nama"])
    sl.write("Alamat: ", sl.session_state["alamat"])
    sl.write("No. HP: ", sl.session_state["no_hp"])
    sl.write("Tanggal pemesanan: ", sl.session_state["tgl_pesan"])
    sl.write("Tanggal pengembalian: ", sl.session_state["tgl_kembali"])
    sl.write("Mobil yang disewa: ", sl.session_state["jenis"], sl.session_state["merk"])
    sl.write("Harga sewa: ", sl.session_state["harga"])
    sl.write("Total harga: ", sl.session_state["total"])
except:
    sl.write("Anda belum memesan mobil")