# 📚 PyFlash — Flashcard Study App (Desktop, Tkinter)

**PyFlash** is a simple, customizable desktop application that helps students create, organize, and study flashcards effectively. Built with **Python and Tkinter**, it provides an offline, distraction-free learning experience with features for reviewing, tracking progress, and modifying study materials.

---

## ✨ Features

- 🎴 **Create Flashcards**  
  Add questions, answers, and optional explanations. Save sets as reusable stacks.

- 🔁 **Study Mode with Feedback**  
  Practice flashcards interactively. Mark cards as correct or incorrect. Incorrect cards are repeated for reinforcement.

- 📊 **Progress Summary**  
  After each session, view statistics: accuracy, time spent, and which cards were missed.

- 🗃 **Stack Management**  
  View, edit, and delete existing flashcard stacks. Add or remove specific cards.

- ⚙️ **User Settings**  
  Customize:
  - Theme: Light / Dark / System
  - Font size and family
  - Window size  
  Settings persist between sessions.

- 💾 **Offline and Lightweight**  
  No internet required. Flashcards are saved locally in `.json` format.

---

## 🖼️ Interface Preview

> *(You can add screenshots here using Markdown)*  
> Example:  
> `![PyFlash Screenshot](screenshots/settings.png)`

---

## 🚀 Getting Started

### ✅ Requirements
- Python 3.7+
- No external dependencies (uses built-in Tkinter)

### ▶️ Run the App

```bash
python bootstrap.py
```

## 💾 Project Stucture
```bash
pyflash/
├── bootstrap.py           # App entry point
├── flashcard_manager.py   # Logic for saving/loading stacks
├── settings_manager.py    # Settings load/save/reset
├── settings.json          # Saved user preferences
├── data/
│   └── stacks/            # Flashcard stacks (JSON format)
└── ui/
    ├── home.py            # Main menu screen
    ├── create.py          # Flashcard creation screen
    ├── study.py           # Flashcard study mode
    ├── modify.py          # Stack modification screen
    ├── settings.py        # App settings screen
```

**NOTE**: All files which start with an underscore "_" are Github-related files. It is not required to download these....

## 📌 Roadmap / To-Do

Here are some planned or suggested features for future versions of PyFlash:
- Export/import flashcards as CSV or Markdown
- Spaced repetition scheduling for better retention
- Search and filter flashcards by keywords
- Keyboard shortcuts for faster study mode
- Add tagging/categories for organizing flashcards
- Progress tracker or calendar for daily study streaks

## 🤝 Contributions

Pull requests, feature suggestions, and feedback are always welcome!
If you’d like to contribute, feel free to fork the repo, make changes, and submit a PR.
