import tkinter as tk
from tkinter import ttk, messagebox
import requests
import json

class DuckPostman:
    def __init__(self, root):
        self.root = root
        self.root.title("🦆 Duck-Postman")

        # Set window size
        window_width = 900
        window_height = 600

        # Get screen dimensions
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Calculate position coordinates
        center_x = int((screen_width - window_width) / 2)
        center_y = int((screen_height - window_height) / 2)

        # Set window size and position
        self.root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        # Create main frame
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=5)

        # Request section
        self.request_frame = ttk.Frame(self.main_frame)
        self.request_frame.pack(fill=tk.X, pady=5)

        # HTTP Method dropdown
        self.methods = ["GET", "POST", "PUT", "DELETE"]
        self.method_var = tk.StringVar(value=self.methods[0])
        self.method_dropdown = ttk.Combobox(
            self.request_frame,
            textvariable=self.method_var,
            values=self.methods,
            width=10
        )
        self.method_dropdown.pack(side=tk.LEFT, padx=5)

        # URL Entry
        self.url_entry = ttk.Entry(self.request_frame, width=70)
        self.url_entry.pack(side=tk.LEFT, padx=5)
        self.url_entry.insert(0, "https://wtfismyip.com/json")

        # Send Button
        self.send_button = ttk.Button(
            self.request_frame,
            text="Send",
            command=self.send_request
        )
        self.send_button.pack(side=tk.LEFT, padx=5)

        # Response section
        self.response_frame = ttk.LabelFrame(self.main_frame, text="Response")
        self.response_frame.pack(fill=tk.BOTH, expand=True, pady=5)

        # Response text area
        self.response_text = tk.Text(
            self.response_frame,
            wrap=tk.WORD,
            width=70,
            height=20
        )
        self.response_text.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

    def send_request(self):
        try:
            url = self.url_entry.get()
            method = self.method_var.get()

            response = requests.request(method, url)

            # Clear previous response
            self.response_text.delete(1.0, tk.END)

            # Try to format JSON response
            try:
                formatted_response = json.dumps(
                    response.json(),
                    indent=2
                )
            except:
                formatted_response = response.text

            self.response_text.insert(tk.END, formatted_response)

        except Exception as e:
            self.response_text.delete(1.0, tk.END)
            self.response_text.insert(tk.END, f"🦆 Oops! Error: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = DuckPostman(root)
    root.mainloop()
