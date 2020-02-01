import random
import tkinter as tk

# initialize a tkinter window
window = tk.Tk()

window.title("Assalamualaikum ______")
window.geometry("400x400")

#----FUNCTIONS----
def phrase_generator():
	phrases = ["Assalamualaikum ", "Hello ", "Annahaesaeyong ", "Olla "]
	
	name = str(entry1.get())

	return phrases[random.randint(0,3)] + name

def phrase_display():
	greeting = phrase_generator()

	# createa the text field
	greeting_display = tk.Text(master=window, height=10, width=30)
	greeting_display.grid(column=0, row=3)

	greeting_display.insert(tk.END, greeting)

#----LABELS----
label1 = tk.Label(text="Selamat datang ke aplikasi saya!", font=("Times New Roman", 11))
label1.grid(column=0, row=0)

label2 = tk.Label(text="Siapakah nama kamu?")
label2.grid(column=0, row=1)

#----ENTRIES----
entry1 = tk.Entry()
entry1.grid(column=1, row=1)

#----BUTTONS----
button1 = tk.Button(text="KLIK SAYA!", command=phrase_display)
button1.grid(column=0, row=2)

# makes the frame appear on screen
window.mainloop()