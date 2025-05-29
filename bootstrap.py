# bootstrap.py
import tkinter as tk
from settings_manager import settings
from ui import home, create, study
import flashcard_manager

home.create_module = create
home.study_module = study

def main():
    root = tk.Tk()
    root.title("PyFlash")

    size_map = {
        "small": "490x470",
        "medium": "590x570",
        "large": "690x670"
    }
    root.geometry(size_map.get(settings["window_size"], "590x570"))
    root.resizable(False, False)

    app = home.HomeScreen(root)
    app.pack(expand=True, fill='both')
    root.mainloop()

if __name__ == '__main__':
    main()