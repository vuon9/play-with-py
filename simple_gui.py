import tkinter as tk
from tkinter import ttk, messagebox

class LoginApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Duck Login 🦆")
        self.geometry("300x400")

        # Center the window
        self.center_window()

        # Create main frame
        main_frame = ttk.Frame(self, padding="20")
        main_frame.pack(expand=True, fill='both')

        # Duck logo (using text as placeholder)
        ttk.Label(main_frame, text="🦆", font=('Arial', 48)).pack(pady=20)
        ttk.Label(main_frame, text="Welcome to DuckAuth!", font=('Arial', 14)).pack(pady=10)

        # Username
        ttk.Label(main_frame, text="Username:").pack(pady=5)
        self.username = ttk.Entry(main_frame, width=30)
        self.username.pack(pady=5)

        # Password
        ttk.Label(main_frame, text="Password:").pack(pady=5)
        self.password = ttk.Entry(main_frame, show="*", width=30)  # show="*" masks the password
        self.password.pack(pady=5)

        # Remember me checkbox
        self.remember = tk.BooleanVar()
        ttk.Checkbutton(main_frame, text="Remember me", variable=self.remember).pack(pady=10)

        # Login button
        ttk.Button(main_frame, text="Login", command=self.login, width=20).pack(pady=10)

        # Forgot password link
        ttk.Label(main_frame, text="Forgot Password?", foreground="blue", cursor="hand2").pack(pady=5)

    def center_window(self):
        self.update_idletasks()
        width = self.winfo_width()
        height = self.winfo_height()
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() // 2) - (height // 2)
        self.geometry(f'+{x}+{y}')

    def login(self):
        # Super secure credentials! 😉
        if self.username.get() == "duck" and self.password.get() == "quack":
            messagebox.showinfo("Success", "Quack! Login successful! 🦆")
        else:
            messagebox.showerror("Error", "Invalid credentials! Quack harder! 🦆")

if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()
