import tkinter as tk
from tkinter import ttk, messagebox
import requests
import pyttsx3

# Initialize speech engine
engine = pyttsx3.init()

# Language dictionary
languages = {
    "English": "en",
    "Hindi": "hi",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Chinese": "zh-cn"
}

# -------------------------------
# Translate Function (API)
# -------------------------------
def translate_text():
    text = input_text.get("1.0", tk.END).strip()
    src_lang = languages[source_lang.get()]
    dest_lang = languages[target_lang.get()]

    if text == "":
        messagebox.showwarning("Warning", "Please enter text")
        return

    try:
        url = "https://translate.googleapis.com/translate_a/single"

        params = {
            "client": "gtx",
            "sl": src_lang,
            "tl": dest_lang,
            "dt": "t",
            "q": text
        }

        response = requests.get(url, params=params)
        result = response.json()

        translated_text = result[0][0][0]

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated_text)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# -------------------------------
# Copy Function
# -------------------------------
def copy_text():
    text = output_text.get("1.0", tk.END).strip()
    if text == "":
        return
    root.clipboard_clear()
    root.clipboard_append(text)
    messagebox.showinfo("Copied", "Text copied!")

# -------------------------------
# Text-to-Speech Function
# -------------------------------
def speak_text():
    text = output_text.get("1.0", tk.END).strip()
    if text == "":
        return
    engine.say(text)
    engine.runAndWait()

# -------------------------------
# GUI Setup
# -------------------------------
root = tk.Tk()
root.title("Language Translation Tool (API Based)")
root.geometry("600x500")
root.resizable(False, False)

# Source Language
tk.Label(root, text="Source Language", font=("Arial", 12)).pack(pady=5)
source_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
source_lang.set("English")
source_lang.pack()

# Target Language
tk.Label(root, text="Target Language", font=("Arial", 12)).pack(pady=5)
target_lang = ttk.Combobox(root, values=list(languages.keys()), state="readonly")
target_lang.set("Hindi")
target_lang.pack()

# Input Text
tk.Label(root, text="Enter Text", font=("Arial", 12)).pack(pady=5)
input_text = tk.Text(root, height=5, width=60)
input_text.pack()

# Translate Button
tk.Button(root, text="Translate", font=("Arial", 12),
          bg="blue", fg="white", command=translate_text).pack(pady=10)

# Output Text
tk.Label(root, text="Translated Text", font=("Arial", 12)).pack(pady=5)
output_text = tk.Text(root, height=5, width=60)
output_text.pack()

# Buttons Frame
frame = tk.Frame(root)
frame.pack(pady=10)

# Copy Button
tk.Button(frame, text="Copy", width=10, command=copy_text).grid(row=0, column=0, padx=10)

# Speak Button
tk.Button(frame, text="Speak", width=10, command=speak_text).grid(row=0, column=1, padx=10)

# Run app
root.mainloop()