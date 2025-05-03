import tkinter as tk
from tkinter import scrolledtext
from tkinter import PhotoImage
import google.generativeai as genai

# ✅ Gemini API Setup
genai.configure(api_key="AIzaSyAaBsxnsbJkVqpbpMpBAtpMAvHP6BO2G1Y")  # 🔐 Replace with your actual API key
model = genai.GenerativeModel("models/gemini-1.5-pro-latest")
chat = model.start_chat()

# ✅ Main window
window = tk.Tk()
window.title("🚀 Chat Assistant By Dilanka")
window.geometry("700x800")
window.configure(bg="#0f111a")

# ✅ Fonts & Colors
FONT = ("Segoe UI", 11)
BG_COLOR = "#0f111a"
INPUT_BG = "#1f212e"
BOT_COLOR = "#4ec9b0"
USER_COLOR = "#9cdcfe"
BORDER_COLOR = "#4e4e50"
BUTTON_BG = "#3b82f6"
BUTTON_HOVER = "#2563eb"

# ✅ Header
header = tk.Label(
    window,
    text="🌟 Chat Assistant By Dilanka",
    bg=BG_COLOR,
    fg="#ffffff",
    font=("Segoe UI Semibold", 18),
    pady=20
)
header.pack()

# ✅ Chat area
chat_frame = tk.Frame(window, bg=BG_COLOR)
chat_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

chat_display = scrolledtext.ScrolledText(
    chat_frame,
    wrap=tk.WORD,
    font=FONT,
    bg=INPUT_BG,
    fg="#ffffff",
    borderwidth=0,
    insertbackground="#ffffff",
    relief=tk.FLAT
)
chat_display.pack(fill=tk.BOTH, expand=True)
chat_display.config(state="disabled")

# ✅ Input area
input_frame = tk.Frame(window, bg=BG_COLOR)
input_frame.pack(padx=20, pady=10, fill=tk.X)

entry_var = tk.StringVar()
user_input = tk.Entry(
    input_frame,
    textvariable=entry_var,
    font=FONT,
    bg=INPUT_BG,
    fg="#ffffff",
    insertbackground="#ffffff",
    relief=tk.FLAT,
    borderwidth=6,
)
user_input.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, ipady=10)

# ✅ Send button
def on_enter(e):
    send_button["bg"] = BUTTON_HOVER

def on_leave(e):
    send_button["bg"] = BUTTON_BG

send_button = tk.Button(
    input_frame,
    text="Send ✉️",
    font=("Segoe UI", 10, "bold"),
    bg=BUTTON_BG,
    fg="#ffffff",
    relief=tk.FLAT,
    padx=20,
    pady=5,
    command=lambda: send_message()
)
send_button.pack(side=tk.RIGHT, padx=(10, 0))
send_button.bind("<Enter>", on_enter)
send_button.bind("<Leave>", on_leave)

# ✅ Send message function
def send_message():
    message = entry_var.get().strip()
    if not message:
        return
    entry_var.set("")

    # Display user's message
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"\n🧑‍💻 You:\n", "user_header")
    chat_display.insert(tk.END, message + "\n", "user_text")
    chat_display.config(state="disabled")
    chat_display.see(tk.END)

    try:
        response = chat.send_message(message)
        bot_reply = response.text
    except Exception as e:
        bot_reply = f"⚠️ Error: {str(e)}"

    # Display bot's response
    chat_display.config(state="normal")
    chat_display.insert(tk.END, f"\n🤖 Gemini:\n", "bot_header")
    chat_display.insert(tk.END, bot_reply + "\n", "bot_text")
    chat_display.config(state="disabled")
    chat_display.see(tk.END)

# ✅ Style tags
chat_display.tag_config("user_header", foreground=USER_COLOR, font=("Segoe UI Semibold", 10))
chat_display.tag_config("bot_header", foreground=BOT_COLOR, font=("Segoe UI Semibold", 10))
chat_display.tag_config("user_text", foreground="#d4d4d4")
chat_display.tag_config("bot_text", foreground="#d4ffd4")

# ✅ Keyboard Enter Key
user_input.bind("<Return>", lambda event: send_message())

# ✅ Run the App
window.mainloop()
