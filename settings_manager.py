# settings_manager.py
import json
import os

SETTINGS_FILE = "settings.json"

DEFAULTS = {
    "theme": "light",
    "font_size": "medium",
    "font_family": "Arial",
    "window_size": "medium"
}

_font_sizes = {
    "small": 8,
    "medium": 10,
    "large": 12
}

def load_settings():
    if os.path.exists(SETTINGS_FILE):
        try:
            with open(SETTINGS_FILE, 'r') as f:
                return json.load(f)
        except:
            pass
    return DEFAULTS.copy()

def save_settings(settings):
    with open(SETTINGS_FILE, 'w') as f:
        json.dump(settings, f, indent=2)

def reset_settings():
    save_settings(DEFAULTS)

settings = load_settings()

def get_font():
    return (settings["font_family"], _font_sizes[settings["font_size"]])