# ui/settings.py
import tkinter as tk
from tkinter import messagebox
from ui.home import HomeScreen
from settings_manager import settings, save_settings, reset_settings, get_font, DEFAULTS

class SettingsScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.master = master

        tk.Label(self, text="Settings", font=('Arial', 14)).pack(pady=10)

        form = tk.Frame(self)
        form.pack()

        # Theme
        tk.Label(form, text="Theme", font=get_font()).grid(row=0, column=0, sticky="w", padx=5, pady=3)
        self.theme = self.make_dropdown(form, ["light", "dark", "system"], settings["theme"], 0)

        # Font Size
        tk.Label(form, text="Font Size", font=get_font()).grid(row=1, column=0, sticky="w", padx=5, pady=3)
        self.font_size = self.make_dropdown(form, ["small", "medium", "large"], settings["font_size"], 1)

        # Font Family
        tk.Label(form, text="Font Family", font=get_font()).grid(row=2, column=0, sticky="w", padx=5, pady=3)
        self.font_family = self.make_dropdown(form, ["Arial", "Courier", "Helvetica", "Times"], settings["font_family"], 2)

        # Window Size
        tk.Label(form, text="Window Size", font=get_font()).grid(row=3, column=0, sticky="w", padx=5, pady=3)
        self.window_size = self.make_dropdown(form, ["small", "medium", "large"], settings["window_size"], 3)

        # Save & Reset buttons
        tk.Button(self, text="Save Settings", command=self.save).pack(pady=5)
        tk.Button(self, text="Reset to Defaults", command=self.reset).pack(pady=2)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)

    def make_dropdown(self, parent, options, selected, row):
        var = tk.StringVar(value=selected)
        tk.OptionMenu(parent, var, *options).grid(row=row, column=1, padx=5, pady=3)
        return var

    def save(self):
        new_settings = {
            "theme": self.theme.get(),
            "font_size": self.font_size.get(),
            "font_family": self.font_family.get(),
            "window_size": self.window_size.get()
        }
        save_settings(new_settings)
        messagebox.showinfo("Saved", "Settings saved. Restart the app to apply.")

    def reset(self):
        reset_settings()
        messagebox.showinfo("Reset", "Settings reset to default. Restart app to apply.")

    def go_back(self):
        self.pack_forget()
        HomeScreen(self.master).pack(expand=True, fill='both')