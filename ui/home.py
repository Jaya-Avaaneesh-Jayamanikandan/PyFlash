# ui/home.py
import tkinter as tk
import json

create_module = None  # to be injected by bootstrap
study_module = None

class HomeScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        tk.Label(self, text="PyFlash", font=('Arial', 20)).pack(pady=20)
        tk.Button(self, text="Create Flashcards", command=self.go_create).pack(pady=5)
        tk.Button(self, text="Study Flashcards", command=self.go_study).pack(pady=5)
        tk.Button(self, text="Modify Stack", command=self.go_modify).pack(pady=5)
        tk.Button(self, text="Settings", command=self.go_settings).pack(pady=5)
        tk.Button(self, text="Exit", command=master.quit).pack(pady=5)

    def go_create(self):
        from ui.create import CreateFlashcards
        self.pack_forget()
        CreateFlashcards(self.master).pack(expand=True, fill='both')

    def go_study(self):
        from ui.study import StudyFlashcards
        self.pack_forget()
        StudyFlashcards(self.master).pack(expand=True, fill='both')

    def go_modify(self):
        from ui.modify import ModifyStackScreen
        self.pack_forget()
        ModifyStackScreen(self.master).pack(expand=True, fill='both')

    def go_settings(self):
        from ui.settings import SettingsScreen
        self.pack_forget()
        SettingsScreen(self.master).pack(expand=True, fill='both')

