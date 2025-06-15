import tkinter as tk
from tkinter import simpledialog
import simulated_apps.contacts_app as contacts_app
import simulated_apps.notes_app as notes_app
import subprocess
import os
from typing import Optional

def prompt_user_command() -> Optional[str]:
    root = tk.Tk()
    root.withdraw()
    command = simpledialog.askstring("Command", "What would you like me to do?")
    root.destroy()
    return command

def dispatch_action(command: str, screen_text: Optional[str] = None) -> None:
    normalized = command.strip().lower() if command else ""

    if "contact" in normalized:
        print("📇 Opening Contacts App...")
        contacts_app.launch_app()

    elif "note" in normalized or "notepad" in normalized:
        print("📝 Opening Notes App...")
        notes_app.launch_app()

    elif "word" in normalized:
        print("📄 Launching Microsoft Word...")
        subprocess.Popen(["start", "winword"], shell=True)

    elif "excel" in normalized:
        print("📊 Launching Microsoft Excel...")
        subprocess.Popen(["start", "excel"], shell=True)

    elif "powerpoint" in normalized or "ppt" in normalized:
        print("📽️ Launching Microsoft PowerPoint...")
        subprocess.Popen(["start", "powerpnt"], shell=True)

    elif "exit" in normalized or "quit" in normalized or "close agent" in normalized:
        print("👋 Exiting agent... Goodbye!")
        os._exit(0)

    else:
        print(f"❌ Command not recognized: '{command}'")
