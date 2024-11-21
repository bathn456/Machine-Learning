import numpy as np
import tkinter as tk
from tkinter import ttk


# Matris çarpımını hesaplayan fonksiyon
def calculate_and_display():
    # Matrisleri tanımla
    matris1 = np.array([[1, 2], [3, 4]])
    matris2 = np.array([[5, 6], [7, 8]])

    # Matris çarpımı
    sonuc = np.dot(matris1, matris2)

    # Sonucu metin alanına yazdır
    result_text = f"Matris 1:\n{matris1}\n\nMatris 2:\n{matris2}\n\nSonuç:\n{sonuc}"
    result_label.config(text=result_text)


# Tkinter pencere oluşturma
window = tk.Tk()
window.title("NumPy Matris Çarpımı")
window.geometry("400x300")

# Açıklama etiketi
description_label = ttk.Label(window, text="Matris Çarpımını Hesapla", font=("Arial", 14))
description_label.pack(pady=10)

# Hesapla butonu
calculate_button = ttk.Button(window, text="Hesapla", command=calculate_and_display)
calculate_button.pack(pady=10)

# Sonuç etiketi
result_label = ttk.Label(window, text="", font=("Courier", 12), justify="left")
result_label.pack(pady=10)

# Pencereyi çalıştır
window.mainloop()
