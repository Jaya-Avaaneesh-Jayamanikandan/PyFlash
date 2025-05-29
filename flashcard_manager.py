# flashcard_manager.py
import json
import os

STACKS_DIR = "data/stacks"

def save_stack(name, flashcards):
    os.makedirs(STACKS_DIR, exist_ok=True)
    path = os.path.join(STACKS_DIR, f"{name}.json")
    with open(path, 'w') as f:
        json.dump(flashcards, f, indent=2)

def load_stack(name):
    path = os.path.join(STACKS_DIR, f"{name}.json")
    if not os.path.exists(path):
        return []
    with open(path, 'r') as f:
        return json.load(f)

def list_stacks():
    os.makedirs(STACKS_DIR, exist_ok=True)
    return [f.replace(".json", "") for f in os.listdir(STACKS_DIR) if f.endswith(".json")]

def delete_stack(name):
    path = os.path.join(STACKS_DIR, f"{name}.json")
    if os.path.exists(path):
        os.remove(path)
        return True
    return False
