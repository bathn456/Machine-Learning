import numpy as np
import tkinter as tk
from tkinter import ttk



def calculate_and_display():

    matris1 = np.array([[1, 2], [3, 4]])
    matris2 = np.array([[5, 6], [7, 8]])


    sonuc = np.dot(matris1, matris2)


    result_text = f"Matris 1:\n{matris1}\n\nMatris 2:\n{matris2}\n\nSonuç:\n{sonuc}"
    result_label.config(text=result_text)



window = tk.Tk()
window.title("NumPy Matris Çarpımı")
window.geometry("400x300")


description_label = ttk.Label(window, text="Matris Çarpımını Hesapla", font=("Arial", 14))
description_label.pack(pady=10)


calculate_button = ttk.Button(window, text="Hesapla", command=calculate_and_display)
calculate_button.pack(pady=10)


result_label = ttk.Label(window, text="", font=("Courier", 12), justify="left")
result_label.pack(pady=10)


window.mainloop()
