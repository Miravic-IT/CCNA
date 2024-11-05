import json

def load_notes(filename):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_notes(filename, notes):
    with open(filename, 'w') as f:
        json.dump(notes, f)

def add_note(notes, note):
    notes.append(note)

def delete_note(notes, index):
    if 0 <= index < len(notes):
        notes.pop(index)

# Exemple d'utilisation
notes = load_notes("notes.json")
add_note(notes, "Première note")
save_notes("notes.json", notes)