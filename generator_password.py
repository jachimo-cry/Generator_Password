import tkinter as tk
import secrets
import string
import tkinter.messagebox
import pyperclip


class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="#0d3b66")
        self.styles = {
            "title": {"font": ("Trebuchet MS", 16, "bold"), "bg": "#0d3b66", "fg": "white"},
            "label": {"font": ("Trebuchet MS", 12), "bg": "#0d3b66", "fg": "#faf0ca"},
            "entry": {"font": ("Trebuchet MS", 12), "bg": "white", "fg": "#000000"},
            "button": {"font": ("Trebuchet MS", 12), "bg": "#2a9d8f", "fg": "white"},
            "password_label": {"font": ("Trebuchet MS", 14), "bg": "white", "relief": "solid", "fg": "#000000"},
            "copied_label": {"fg": "#1aff1a", "bg": "#0d3b66"}
        }
        self.create_widgets()

    def create_widgets(self):
        self.create_title_label()
        self.create_length_input()
        self.create_generate_button()
        self.create_password_label()
        self.create_copy_button()

    def create_title_label(self):
        title_label = tk.Label(
            self.root, text="Secure Password Generator", **self.styles["title"])
        title_label.pack(pady=10)

    def create_length_input(self):
        length_label = tk.Label(
            self.root, text="Password Length:", **self.styles["label"])
        length_label.pack()

        self.length_entry = tk.Entry(self.root, font=self.styles["entry"])
        self.length_entry.pack()

    def create_generate_button(self):
        generate_button = tk.Button(self.root, text="Generate Password", command=self.generate_password,
                                    **self.styles["button"])
        generate_button.pack(pady=10)

    def create_password_label(self):
        self.password_label = tk.Label(
            self.root, text="", **self.styles["password_label"])
        self.password_label.pack(fill="x", padx=10, pady=10)

    def create_copy_button(self):
        copy_button = tk.Button(self.root, text="Copy Password", command=self.copy_to_clipboard,
                                **self.styles["button"])
        copy_button.pack(pady=10)

    def generate_password(self):
        password_length = self.length_entry.get()
        if not password_length.isdigit():
            self.show_error("Please enter a valid number.")
            return

        password_length = int(password_length)
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(secrets.choice(characters)
                           for _ in range(password_length))
        self.password_label.configure(
            text=password, bg=self.styles["password_label"]["bg"])
        self.generated_password = password

    def copy_to_clipboard(self):
        password = getattr(self, 'generated_password', None)
        if password:
            try:
                pyperclip.copy(password)
                self.show_copy_success()
            except pyperclip.PyperclipException:
                self.show_error("Failed to copy to clipboard")

    def show_copy_success(self):
        copied_label = tk.Label(self.root, text="Copied!",
                                **self.styles["copied_label"])
        copied_label.pack()
        self.root.after(1500, copied_label.destroy)

    def show_error(self, message):
        tkinter.messagebox.showerror("Error", message)

    def on_closing(self):
        if tkinter.messagebox.askokcancel("Exit", "Do you want to exit?"):
            self.root.destroy()


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.protocol("WM_DELETE_WINDOW", app.on_closing)
    root.mainloop()
