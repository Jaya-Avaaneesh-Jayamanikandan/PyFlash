# ui/create.py
import tkinter as tk
from tkinter import messagebox
from flashcard_manager import save_stack
from ui.home import HomeScreen

class CreateFlashcards(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.flashcards = []

        tk.Label(self, text="Create Flashcards").pack(pady=5)

        tk.Label(self, text="Question").pack()
        self.q_entry = tk.Entry(self, width=40)
        self.q_entry.pack(pady=2)

        tk.Label(self, text="Answer").pack()
        self.a_entry = tk.Entry(self, width=40)
        self.a_entry.pack(pady=2)

        # Add Explanation Checkbox
        self.add_expl_var = tk.IntVar()
        self.expl_check = tk.Checkbutton(self, text="Add Explanation (Optional)", variable=self.add_expl_var, command=self.toggle_explanation)
        self.expl_check.pack()

        # Explanation Text (hidden by default)
        self.expl_text = tk.Text(self, width=40, height=4, wrap="word")
        self.expl_text.pack(pady=5)
        self.expl_text.pack_forget()  # hidden initially

        tk.Button(self, text="Add Flashcard", command=self.add_card).pack(pady=5)

        # Stack name and save
        tk.Label(self, text="Stack Name").pack()
        self.stack_name = tk.Entry(self, width=30)
        self.stack_name.insert(0, "stack_name")
        self.stack_name.pack(pady=5)

        tk.Button(self, text="Save Stack", command=self.save_stack).pack(pady=5)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=5)

        self.card_list = tk.Text(self, height=10, width=50)
        self.card_list.pack()

    def toggle_explanation(self):
        if self.add_expl_var.get():
            self.expl_text.pack(pady=5)
        else:
            self.expl_text.pack_forget()

    def add_card(self):
        q = self.q_entry.get().strip()
        a = self.a_entry.get().strip()
        explanation = self.expl_text.get("1.0", "end").strip() if self.add_expl_var.get() else ""

        if not q or not a:
            messagebox.showwarning("Missing Data", "Please enter both question and answer.")
            return

        if len(explanation.split()) > 50:
            messagebox.showwarning("Too Long", "Explanation must be under 50 words.")
            return

        self.flashcards.append({
            'question': q,
            'answer': a,
            'explanation': explanation
        })

        self.card_list.insert(tk.END, f"Q: {q} | A: {a}" + (f" | Expl: {explanation[:30]}..." if explanation else "") + "\n")
        self.q_entry.delete(0, tk.END)
        self.a_entry.delete(0, tk.END)
        self.expl_text.delete("1.0", tk.END)

    def save_stack(self):
        name = self.stack_name.get().strip()
        if name and self.flashcards:
            save_stack(name, self.flashcards)
            messagebox.showinfo("Saved", f"Stack '{name}' saved successfully.")

    def go_back(self):
        from ui.home import HomeScreen
        self.pack_forget()
        HomeScreen(self.master).pack(expand=True, fill='both')