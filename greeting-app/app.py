import tkinter as tk

# initialize a tkinter window
window = tk.Tk()

window.title("Assalamualaikum App")
window.geometry("300x300")

# LABEL
title = tk.Label(text="Assalamualaikum, selamat datang ke aplikasi saya!")
title.grid()

# ENTRY FIELD
entry_field1 = tk.Entry()
entry_field1.grid()

# BUTTON
button1 = tk.Button(text="Klik saya!")
button1.grid()

# makes the frame appear on screen
window.mainloop()