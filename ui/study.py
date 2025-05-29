# ui/study.py
import tkinter as tk
from tkinter import messagebox
import random
import time
from flashcard_manager import load_stack, list_stacks, delete_stack

class StudyFlashcards(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.cards = []
        self.queue = []
        self.correct_answers = []
        self.wrong_answers = []
        self.current = None
        self.start_time = None

        tk.Label(self, text="Study Flashcards").pack()

        # Load stack names
        stacks = list_stacks()
        self.stack_var = tk.StringVar(self)

        if stacks:
            self.stack_var.set(stacks[0])
        else:
            stacks = ["<no stacks>"]
            self.stack_var.set("<no stacks>")

        tk.OptionMenu(self, self.stack_var, *stacks).pack()

        # Buttons
        self.load_btn = tk.Button(self, text="Load Stack", command=self.load_stack)
        self.load_btn.pack()

        self.delete_btn = tk.Button(self, text="Delete Stack", command=self.delete_stack)
        self.delete_btn.pack()

        # Disable buttons if no real stacks
        if "<no stacks>" in stacks:
            self.load_btn.config(state='disabled')
            self.delete_btn.config(state='disabled')

        self.question_label = tk.Label(self, text="", wraplength=300, font=('Arial', 12))
        self.question_label.pack(pady=10)

        self.answer_label = tk.Label(self, text="", wraplength=300, font=('Arial', 10))
        self.answer_label.pack(pady=5)

        tk.Button(self, text="Show Answer", command=self.show_answer).pack()

        self.btn_frame = tk.Frame(self)
        self.btn_frame.pack(pady=10)

        tk.Button(self.btn_frame, text="Correct", command=self.mark_correct).grid(row=0, column=0, padx=5)
        tk.Button(self.btn_frame, text="Incorrect", command=self.mark_incorrect).grid(row=0, column=1, padx=5)

        tk.Button(self, text="Back", command=self.go_back).pack(pady=10)

        self.btn_frame.pack_forget() 


    def load_stack(self):
        name = self.stack_var.get()
        self.cards = load_stack(name)
        self.queue = self.cards.copy()
        random.shuffle(self.queue)
        self.correct_answers.clear()
        self.wrong_answers.clear()
        self.start_time = time.time()
        self.next_card()

    def show_answer(self):
        if self.current:
            answer = self.current.get('answer', '')
            explanation = self.current.get('explanation', '')
            self.answer_label.config(text=f"Answer: {answer}\n\n" + (f"Explanation: {explanation}" if explanation else ""))
            self.btn_frame.pack(pady=10)

    def next_card(self):
        if self.queue:
            self.current = self.queue.pop(0)
            self.question_label.config(text=self.current['question'])
            self.answer_label.config(text="")
            self.btn_frame.pack_forget()  # Hide correct/incorrect again
        else:
            self.show_summary()


    def mark_correct(self):
        if self.current:
            self.correct_answers.append(self.current)
            self.next_card()

    def mark_incorrect(self):
        if self.current:
            self.wrong_answers.append(self.current)
            self.queue.append(self.current)  # Retry later
            self.next_card()

    def show_summary(self):
        elapsed = int(time.time() - self.start_time)
        total = len(self.correct_answers) + len(self.wrong_answers)
        correct = len(self.correct_answers)
        incorrect = len(self.wrong_answers)
        accuracy = (correct / total * 100) if total else 0

        for widget in self.winfo_children():
            widget.destroy()

        tk.Label(self, text="Session Summary", font=('Arial', 14)).pack(pady=10)
        tk.Label(self, text=f"Correct: {correct}").pack()
        tk.Label(self, text=f"Incorrect: {incorrect}").pack()
        tk.Label(self, text=f"Accuracy: {accuracy:.1f}%").pack()
        tk.Label(self, text=f"Time Spent: {elapsed} seconds").pack(pady=10)

        if self.wrong_answers:
            tk.Button(self, text="Retry Incorrect Cards", command=self.retry_incorrect).pack(pady=5)
        tk.Button(self, text="Back to Home", command=self.go_back).pack(pady=5)

    def retry_incorrect(self):
        self.queue = self.wrong_answers.copy()
        self.wrong_answers.clear()
        self.correct_answers.clear()
        self.start_time = time.time()
        self.next_card()

    def delete_stack(self):
        from tkinter import messagebox
        name = self.stack_var.get()
        confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete '{name}'? THIS ACTION CANNOT BE UNDONE.")
        if confirm and delete_stack(name):
            messagebox.showinfo("Deleted", f"Stack '{name}' deleted.")
            self.destroy()
            new_screen = StudyFlashcards(self.master)
            new_screen.pack(expand=True, fill='both')

        elif not confirm:
            return
        else:
            messagebox.showerror("Error", "Failed to delete stack. Check 'DebugDump.txt' for Error Message.")


    def go_back(self):
        from ui.home import HomeScreen
        self.pack_forget()
        HomeScreen(self.master).pack(expand=True, fill='both')