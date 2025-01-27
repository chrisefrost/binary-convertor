import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

class CharToBinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Character to Binary Converter")
        self.root.geometry("640x320")
        self.root.resizable(True, True)

        # Configure root grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Configure styles
        self.setup_styles()

        # Create main container with proper padding
        main_frame = ttk.Frame(root, padding="20 20 20 20", style="Main.TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")

        # Create and pack the input frame
        input_frame = ttk.Frame(main_frame, style="Input.TFrame")
        input_frame.pack(fill="x", pady=(0, 15))

        # Input section with proper layout
        ttk.Label(input_frame, text="Enter Text:", style="Header.TLabel").pack(side="left", padx=(0, 10))

        self.text_entry = ttk.Entry(input_frame, width=30)
        self.text_entry.pack(side="left", padx=(0, 10))
        self.text_entry.bind('<Return>', lambda e: self.convert())
        self.text_entry.focus()  # Set initial focus

        convert_btn = ttk.Button(input_frame, text="Convert", command=self.convert, style="Convert.TButton")
        convert_btn.pack(side="left")

        # Result section
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill="both", expand=True, pady=(0, 20))

        ttk.Label(result_frame, text="Binary Result:", style="Header.TLabel").pack(side="top", anchor="w", padx=(0, 10))

        # Use a Text widget for word-wrapping
        self.result_text = tk.Text(result_frame, wrap="word", font=("Consolas", 12), foreground="#0066cc", height=5)
        self.result_text.pack(fill="both", expand=True)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, style="Status.TLabel")
        status_bar.pack(side="bottom", fill="x", pady=(10, 0))

    def setup_styles(self):
        style = ttk.Style()

        # Configure modern-looking styles
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Status.TLabel", font=("Segoe UI", 9), foreground="#666666")
        style.configure("Convert.TButton", padding=5)

    def convert_to_binary(self, text):
        binary_result = []
        for char in text:
            binary_char = ''.join(format(ord(char), '08b'))
            binary_result.append(binary_char)
        return ' '.join(binary_result)

    def convert(self):
        text = self.text_entry.get()
        if text:
            binary = self.convert_to_binary(text)
            self.result_text.delete(1.0, tk.END)  # Clear previous content
            self.result_text.insert(tk.END, binary)  # Insert new binary result
            self.status_var.set(f"Successfully converted '{text}' to binary")
        else:
            messagebox.showerror("Invalid Input", "Please enter some text")
            self.status_var.set("Error: No input provided")

def main():
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 1.5)  # Improve resolution on high-DPI displays
    app = CharToBinaryConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()