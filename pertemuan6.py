import tkinter as tk

def hitung_prediksi():
    label_hasil.config(text="Prediksi: Teknologi Informasi")

top = tk.Tk()
top.title("Aplikasi Prediksi Prodi")
top.geometry("400x500")

judul = tk.Label(top, text="Aplikasi Prediksi Prodi Pilihan")
judul.grid(row=0, column=0, columnspan=2, pady=10)
