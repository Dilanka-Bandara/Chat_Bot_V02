
import tkinter as tk
from tkinter import scrolledtext
import google.generativeai as genai

# ✅ Gemini API setup
genai.configure(api_key="AIzaSyAaBsxnsbJkVqpbpMpBAtpMAvHP6BO2G1Y")
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")
chat = model.start_chat()

# ✅ GUI setup
window = tk.Tk()
window.title("Gemini AI Chatbot")
window.geometry("600x700")
window.configure(bg="#1e1e1e")

# ✅ Fonts and colors
FONT = ("Segoe UI", 11)
BG_COLOR = "#1e1e1e"
TEXT_COLOR = "#ffffff"
INPUT_BG = "#2d2d2d"
BUTTON_BG = "#0078D7"
BUTTON_FG = "#ffffff"
ACCENT_COLOR = "#4ec9b0"

# ✅ Chat display
chat_display = scrolledtext.ScrolledText(
    window,
    wrap=tk.WORD,
    font=FONT,
    bg=INPUT_BG,
    fg=TEXT_COLOR,
    borderwidth=0,
    insertbackground=TEXT_COLOR
)
chat_display.pack(padx=20, pady=(20, 10), fill=tk.BOTH, expand=True)
chat_display.config(state="disabled")

# ✅ Input field
input_frame = tk.Frame(window, bg=BG_COLOR)
input_frame.pack(padx=20, pady=10, fill=tk.X)

user_input = tk.Entry(input_frame, font=FONT, bg=INPUT_BG, fg=TEXT_COLOR, insertbackground=TEXT_COLOR, relief=tk.FLAT)
user_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=(0, 10), ipady=10)

# ✅ Send message function
def send_message():
    message = user_input.get().strip()
    if not message:
        return

    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"You: {message}\n", "user")
    chat_display.config(state="disabled")
    chat_display.see(tk.END)
    user_input.delete(0, tk.END)

    try:
        response = chat.send_message(message)
        answer = response.text
    except Exception as e:
        answer = f"⚠️ Error: {e}"

    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"Gemini: {answer}\n\n", "gemini")
    chat_display.config(state="disabled")
    chat_display.see(tk.END)

# ✅ Send button
send_button = tk.Button(
    input_frame,
    text="Send",
    font=FONT,
    bg=BUTTON_BG,
    fg=BUTTON_FG,
    relief=tk.FLAT,
    command=send_message,
    padx=20,
    pady=5
)
send_button.pack(side=tk.RIGHT)

# ✅ Keyboard Enter
def enter_pressed(event):
    send_message()

user_input.bind("<Return>", enter_pressed)

# ✅ Text styles
chat_display.tag_config("user", foreground="#9cdcfe")
chat_display.tag_config("gemini", foreground=ACCENT_COLOR)

# ✅ Start GUI
window.mainloop()
