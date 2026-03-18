import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# ---------------- FAQ DATA ----------------
faq_responses = {
    "hello": "Hi there! How can I help you?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I'm just a bot, but I'm doing great!",
    "what is your name": "I'm a Tkinter Chatbot.",
    "bye": "Goodbye! Have a nice day!",
    "help": "You can ask me basic questions like greetings or my name."
}

# ---------------- BOT LOGIC ----------------
def get_bot_response(user_input):
    user_input = user_input.lower()
    for key in faq_responses:
        if key in user_input:
            return faq_responses[key]
    return "Sorry, I don't understand that yet."

# ---------------- GUI CLASS ----------------
class ChatbotApp:
    def __init__(self, root):
        self.root = root
        self.root.title("FAQ Chatbot")
        self.root.geometry("400x500")

        # Chat display area
        self.chat_area = scrolledtext.ScrolledText(
            root,
            wrap=tk.WORD,
            state='disabled',
            bg="#f5f5f5",
            font=("Arial", 10)
        )
        self.chat_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Input field
        self.entry = tk.Entry(root, font=("Arial", 12))
        self.entry.pack(padx=10, pady=(0, 5), fill=tk.X)
        self.entry.bind("<Return>", self.send_message)

        # Send button
        self.send_button = tk.Button(root, text="Send", command=self.send_message)
        self.send_button.pack(pady=(0, 10))

        # Styling (chat bubbles)
        self.chat_area.tag_config(
            "user",
            background="#dcf8c6",
            foreground="black",
            justify='right',
            lmargin1=50, lmargin2=50,
            rmargin=10,
            spacing3=5
        )

        self.chat_area.tag_config(
            "bot",
            background="#ffffff",
            foreground="black",
            justify='left',
            lmargin1=10, lmargin2=10,
            rmargin=50,
            spacing3=5
        )

        self.chat_area.tag_config(
            "time",
            foreground="gray",
            font=("Arial", 8)
        )

    # Add message to chat
    def add_message(self, message, sender):
        self.chat_area.configure(state='normal')

        timestamp = datetime.now().strftime("%H:%M")

        if sender == "user":
            self.chat_area.insert(tk.END, f"\n{message}\n", "user")
        else:
            self.chat_area.insert(tk.END, f"\n{message}\n", "bot")

        self.chat_area.insert(tk.END, f"{timestamp}\n", "time")

        self.chat_area.configure(state='disabled')
        self.chat_area.yview(tk.END)

    # Handle sending message
    def send_message(self, event=None):
        user_text = self.entry.get().strip()

        if user_text == "":
            return

        self.add_message(user_text, "user")
        self.entry.delete(0, tk.END)

        response = get_bot_response(user_text)
        self.add_message(response, "bot")


# ---------------- RUN APP ----------------
if __name__ == "__main__":
    root = tk.Tk()
    app = ChatbotApp(root)
    root.mainloop()