import tkinter as tk

# initialize a tkinter window
window = tk.Tk()

window.title("Assalamualaikum App")
window.geometry("300x300")

# LABEL
title = tk.Label(text="Assalamualaikum, selamat datang ke aplikasi saya!", font=("Times New Roman", 11))
title.grid(column=0, row=0)

# ENTRY FIELD
entry_field1 = tk.Entry()
entry_field1.grid(column=0, row=1)

# BUTTON
button1 = tk.Button(text="Klik saya!", bg="green")
button1.grid(column=0, row=2)

# TEXT FIELD
text_field1 = tk.Text(master=window, height=10, width=30)
text_field1.grid(column=0, row=3)

# makes the frame appear on screen
window.mainloop()