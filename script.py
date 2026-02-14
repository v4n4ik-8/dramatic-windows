import tkinter as tk
from tkinter import messagebox

lines = []

# LANGUGAGE CONGIG
LANG = {
    "ru": {
        "title": "Windows Lyrics Creator",
        "line": "Строка:",
        "window_title": "Название окна:",
        "add": "Добавить",
        "play": "Запустить",
        "clear": "Очистить",
        "icon": "Тип окна:",
        "empty": "Введите текст"
    },
    "en": {
        "title": "Windows Lyrics Creator",
        "line": "Line:",
        "window_title": "Window title:",
        "add": "Add",
        "play": "Play",
        "clear": "Clear",
        "icon": "Window type:",
        "empty": "Enter text"
    }
}

current_lang = "en"


def tr(key):
    return LANG[current_lang][key]


# MAIN LOGIC
def add_line():
    text = entry.get().strip()
    kind = icon_var.get()

    if not text:
        messagebox.showwarning("!", tr("empty"))
        return

    lines.append((kind, text))
    listbox.insert(tk.END, f"[{kind}] {text}")
    entry.delete(0, tk.END)


def play_windows():
    if not lines:
        return

    title = title_entry.get().strip()
    if not title:
        title = "Message"

    for kind, text in lines:
        temp_root = tk.Tk()
        temp_root.withdraw()

        if kind == "info":
            messagebox.showinfo(title, text, parent=temp_root)
        elif kind == "warning":
            messagebox.showwarning(title, text, parent=temp_root)
        elif kind == "error":
            messagebox.showerror(title, text, parent=temp_root)
        elif kind == "question":
            messagebox.askquestion(title, text, parent=temp_root)

        temp_root.destroy()


def clear_all():
    lines.clear()
    listbox.delete(0, tk.END)


# LANGUAGE
def set_language(lang):
    global current_lang
    current_lang = lang
    refresh_ui()


def refresh_ui():
    root.title(tr("title"))
    label_line.config(text=tr("line"))
    label_title.config(text=tr("window_title"))
    label_icon.config(text=tr("icon"))

    btn_add.config(text=tr("add"))
    btn_play.config(text=tr("play"))
    btn_clear.config(text=tr("clear"))


# UI
root = tk.Tk()
root.geometry("520x430")

lang_frame = tk.Frame(root)
lang_frame.pack(pady=5)

tk.Button(lang_frame, text="RU", command=lambda: set_language("ru")).pack(side="left", padx=5)
tk.Button(lang_frame, text="EN", command=lambda: set_language("en")).pack(side="left", padx=5)

label_title = tk.Label(root)
label_title.pack(anchor="w", padx=10)

title_entry = tk.Entry(root, font=("Segoe UI", 11))
title_entry.insert(0, "go away")
title_entry.pack(fill="x", padx=10, pady=5)

label_line = tk.Label(root)
label_line.pack(anchor="w", padx=10)

entry = tk.Entry(root, font=("Segoe UI", 12))
entry.pack(fill="x", padx=10, pady=5)

label_icon = tk.Label(root)
label_icon.pack(anchor="w", padx=10)

icon_var = tk.StringVar(value="info")
icons_frame = tk.Frame(root)
icons_frame.pack()

for icon in ["info", "warning", "error", "question"]:
    tk.Radiobutton(
        icons_frame,
        text=icon,
        value=icon,
        variable=icon_var
    ).pack(side="left", padx=5)

btn_frame = tk.Frame(root)
btn_frame.pack(pady=10)

btn_add = tk.Button(btn_frame, command=add_line)
btn_add.pack(side="left", padx=5)

btn_play = tk.Button(btn_frame, command=play_windows)
btn_play.pack(side="left", padx=5)

btn_clear = tk.Button(btn_frame, command=clear_all)
btn_clear.pack(side="left", padx=5)

listbox = tk.Listbox(root, font=("Segoe UI", 11))
listbox.pack(fill="both", expand=True, padx=10, pady=10)

refresh_ui()
root.mainloop()
