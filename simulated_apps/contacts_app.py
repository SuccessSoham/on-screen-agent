# simulated_apps/contacts_app.py
import tkinter as tk

def launch_app():
    root = tk.Tk()
    root.title("Contacts App")
    label = tk.Label(root, text="This is a simulated Contacts App!")
    label.pack(padx=20, pady=20)
    # App stays open until user closes it
    root.mainloop()

if __name__ == "__main__":
    launch_app()
