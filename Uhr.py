import tkinter as tk
import time

# Fenster erstellen
fenster= tk.Tk()
fenster.title("Digital Uhr")
fenster.geometry("400x150")
fenster.configure(bg="black")

# Uhrzeit-Label
label = tk.Label(fenster, font=("Arial", 48), bg="grey", fg="lime")
label.pack(expand=True)

# Funktion zum Aktualisieren der Uhrzeit jede sekunde
def update_time():
    aktuelle_zeit = time.strftime("%H:%M:%S")
    label.config(text=aktuelle_zeit)
    fenster.after(1000, update_time)

# Start
update_time()
fenster.mainloop()

