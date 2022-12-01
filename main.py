import streamlit as sl

data = {
    "MPV Cars": {
        "Avanza": 200000,
        "APV": 200000,
        "Innova": 250000,
        "Alphard": 500000  
    },
    "SUV Cars": {
        "Rush": 250000,
        "Fortuner": 350000,
        "HR-V": 250000,
    },
    "Sedan Cars": {
        "Vios": 150000,
        "Camry": 400000,
    }
}

sl.title("Rental Mobil")

nama = sl.text_input("Nama")
alamat = sl.text_area("Alamat")
no_hp = sl.text_input("No. HP")
tgl_pesan = sl.date_input("Tanggal pemesanan")
tgl_kembali = sl.date_input("Tanggal pengembalian")

sl.write("Pilih mobil yang ingin disewa")

select1 = sl.selectbox("Pilih Jenis Mobil", list(data.keys()))
select2 = sl.selectbox("Pilih Mobil", list(data[select1].keys()))
sl.write("Harga Sewa: ", data[select1][select2])

button = sl.button("Pesan")

if button:
    sl.session_state["nama"] = nama
    sl.session_state["alamat"] = alamat
    sl.session_state["no_hp"] = no_hp
    sl.session_state["tgl_pesan"] = tgl_pesan
    sl.session_state["tgl_kembali"] = tgl_kembali
    sl.session_state["jenis"] = select1
    sl.session_state["merk"] = select2
    sl.session_state["harga"] = data[select1][select2]
    sl.session_state["total"] = ((tgl_kembali - tgl_pesan).days + 1) * data[select1][select2]
    
    sl.write("Pemesanan berhasil!")