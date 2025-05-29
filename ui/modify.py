# ui/modify.py
import tkinter as tk
from tkinter import messagebox
from flashcard_manager import load_stack, save_stack, list_stacks

class ModifyStackScreen(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.stack_name = None
        self.cards = []
        self.selected_index = None

        tk.Label(self, text="Modify Flashcard Stack").pack(pady=5)

        stacks = list_stacks()
        self.stack_var = tk.StringVar(self)
        if stacks:
            self.stack_var.set(stacks[0])
        else:
            self.stack_var.set("<no stacks>")
            stacks = ["<no stacks>"]

        tk.OptionMenu(self, self.stack_var, *stacks).pack(pady=5)
        tk.Button(self, text="Load Stack", command=self.load_stack).pack(pady=5)

        self.card_list = tk.Listbox(self, width=60)
        self.card_list.pack(pady=5)
        self.card_list.bind("<<ListboxSelect>>", self.select_card)

        tk.Button(self, text="Delete Selected", command=self.delete_selected).pack(pady=5)

        # Add new card form
        tk.Label(self, text="Question").pack()
        self.q_entry = tk.Entry(self, width=40)
        self.q_entry.pack()

        tk.Label(self, text="Answer").pack()
        self.a_entry = tk.Entry(self, width=40)
        self.a_entry.pack()

        self.add_expl_var = tk.IntVar()
        self.expl_check = tk.Checkbutton(self, text="Add Explanation (Optional)", variable=self.add_expl_var, command=self.toggle_expl)
        self.expl_check.pack()

        self.expl_text = tk.Text(self, width=40, height=3, wrap="word")
        self.expl_text.pack()
        self.expl_text.pack_forget()

        tk.Button(self, text="Add Card", command=self.add_card).pack(pady=5)
        tk.Button(self, text="Save Changes", command=self.save_stack).pack(pady=5)
        tk.Button(self, text="Back", command=self.go_back).pack(pady=5)

    def toggle_expl(self):
        if self.add_expl_var.get():
            self.expl_text.pack()
        else:
            self.expl_text.pack_forget()

    def load_stack(self):
        self.stack_name = self.stack_var.get()
        self.cards = load_stack(self.stack_name)
        self.refresh_listbox()

    def refresh_listbox(self):
        self.card_list.delete(0, tk.END)
        for i, card in enumerate(self.cards):
            preview = f"{i+1}. Q: {card['question']} | A: {card['answer']}"
            if card.get('explanation'):
                preview += f" | Expl: {card['explanation'][:30]}..."
            self.card_list.insert(tk.END, preview)

    def select_card(self, event):
        selection = self.card_list.curselection()
        if selection:
            self.selected_index = selection[0]

    def delete_selected(self):
        if self.selected_index is not None and 0 <= self.selected_index < len(self.cards):
            del self.cards[self.selected_index]
            self.selected_index = None
            self.refresh_listbox()

    def add_card(self):
        q = self.q_entry.get().strip()
        a = self.a_entry.get().strip()
        explanation = self.expl_text.get("1.0", "end").strip() if self.add_expl_var.get() else ""

        if not q or not a:
            messagebox.showwarning("Missing", "Question and Answer required.")
            return
        if len(explanation.split()) > 50:
            messagebox.showwarning("Too Long", "Explanation must be under 50 words.")
            return

        self.cards.append({
            'question': q,
            'answer': a,
            'explanation': explanation
        })

        self.q_entry.delete(0, tk.END)
        self.a_entry.delete(0, tk.END)
        self.expl_text.delete("1.0", tk.END)
        self.refresh_listbox()

    def save_stack(self):
        if self.stack_name:
            save_stack(self.stack_name, self.cards)
            messagebox.showinfo("Saved", f"Stack '{self.stack_name}' updated.")

    def go_back(self):
        from ui.home import HomeScreen
        self.pack_forget()
        HomeScreen(self.master).pack(expand=True, fill='both')