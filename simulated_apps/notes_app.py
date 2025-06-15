# simulated_apps/notes_app.py

import tkinter as tk
from tkinter import filedialog
import tkinter.messagebox as messagebox  # Fully qualified to improve type hints
from typing import Optional


class NotesApp:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Notes App")
        self.root.geometry("600x400")

        self.text_area = tk.Text(self.root, wrap="word", font=("Arial", 12))
        self.text_area.pack(expand=True, fill="both", padx=10, pady=10)

        self._create_menu()

    def _create_menu(self) -> None:
        menu_bar = tk.Menu(self.root)
        self.root.config(menu=menu_bar)

        file_menu = tk.Menu(menu_bar, tearoff=0)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)

        menu_bar.add_cascade(label="File", menu=file_menu)

    def open_file(self) -> None:
        file_path: Optional[str] = filedialog.askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                with open(file_path, "r", encoding="utf-8") as file:
                    content = file.read()
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert(tk.END, content)
            except Exception as e:
                messagebox.showerror("Open Error", f"Could not open file:\n{e}")  # type: ignore

    def save_file(self) -> None:
        file_path: Optional[str] = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if file_path:
            try:
                content: str = self.text_area.get("1.0", tk.END).strip()
                with open(file_path, "w", encoding="utf-8") as file:
                    file.write(content)
                messagebox.showinfo("Saved", "File saved successfully!")  # type: ignore
            except Exception as e:
                messagebox.showerror("Save Error", f"Could not save file:\n{e}")  # type: ignore


def launch_app() -> None:
    root = tk.Tk()
    NotesApp(root)
    root.mainloop()


if __name__ == "__main__":
    launch_app()