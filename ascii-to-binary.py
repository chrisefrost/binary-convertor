import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

class CharToBinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Magic Word Converter! ✨")
        self.root.geometry("850x550")
        self.root.minsize(width=450, height=400) 
        self.root.resizable(True, True)

        # Configure root grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        # Configure styles
        self.setup_styles()

        # Create main container with proper padding and background
        main_frame = ttk.Frame(root, padding="30 30 30 30", style="Main.TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        # Ensure main_frame's columns/rows expand
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(1, weight=1) 

        # Create the input frame (now using grid internally for better control)
        input_frame = ttk.Frame(main_frame, style="Input.TFrame")
        input_frame.grid(row=0, column=0, sticky="ew", pady=(0, 25)) 
        
        # Configure columns within input_frame: only one column, which expands
        input_frame.grid_columnconfigure(0, weight=1) 
        
        # Row 0: "Type your secret message here:" label
        ttk.Label(input_frame, text="Type your secret message here:", style="Header.TLabel").grid(row=0, column=0, padx=(0, 0), pady=(0, 5), sticky="w")

        # Row 1: Entry box
        self.text_entry = ttk.Entry(input_frame, font=("Comic Sans MS", 16))
        self.text_entry.grid(row=1, column=0, padx=(0, 0), pady=(0, 5), sticky="ew") 
        self.text_entry.bind('<Return>', lambda e: self.convert())
        self.text_entry.focus()

        # Row 2: Annotation for number conversion
        ttk.Label(input_frame, text="Note: Multi-digit numbers are converted per digit (e.g., '22' converts '2' then '2').",
                  style="Annotation.TLabel").grid(row=2, column=0, padx=(0, 0), pady=(0, 15), sticky="w")

        # Row 3: Buttons - placed in a sub-frame for better alignment control
        button_frame = ttk.Frame(input_frame)
        button_frame.grid(row=3, column=0, sticky="w") 
        
        convert_btn = ttk.Button(button_frame, text="🤖 Make it Binary!", command=self.convert, style="Convert.TButton")
        convert_btn.pack(side="left", padx=(0, 10)) 

        clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_fields, style="Clear.TButton")
        clear_btn.pack(side="left") 


        # Result section
        result_frame = ttk.Frame(main_frame, style="Result.TFrame")
        result_frame.grid(row=1, column=0, sticky="nsew", pady=(0, 30))
        result_frame.grid_columnconfigure(0, weight=1) 
        result_frame.grid_rowconfigure(1, weight=1) 

        # "Top Secret" label with lock emoji
        top_secret_label = ttk.Label(result_frame, text="🔒 Your message in secret code:", style="Header.TLabel")
        top_secret_label.grid(row=0, column=0, sticky="nw", padx=(0, 10), pady=(0, 5))

        # Use a Text widget for word-wrapping
        self.result_text = tk.Text(result_frame, wrap="word", font=("Consolas", 18, "bold"), foreground="#FF6600", height=6, bg="#E0FFFF", relief="sunken", bd=3)
        self.result_text.grid(row=1, column=0, sticky="nsew", padx=10, pady=10)

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready to convert your words into secret code! 🚀")
        self.status_bar = ttk.Label(main_frame, textvariable=self.status_var, style="Status.TLabel", anchor="w") 
        self.status_bar.grid(row=2, column=0, sticky="ew", pady=(15, 0)) 
        
        # Bind the <Configure> event to the root window to update wraplength on resize
        self.root.bind("<Configure>", self.on_window_resize)


    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam') 

        style.configure("Main.TFrame", background="#B0E0E6") 
        style.configure("Input.TFrame", background="#ADD8E6", borderwidth=5, relief="raised") 
        style.configure("Result.TFrame", background="#E0FFFF", borderwidth=5, relief="ridge") 

        style.configure("Header.TLabel", font=("Comic Sans MS", 18, "bold"), foreground="#483D8B") 
        # Added a new style for the annotation label
        style.configure("Annotation.TLabel", font=("Comic Sans MS", 10, "italic"), foreground="#6A5ACD") # Slate blue
        style.configure("Status.TLabel", font=("Comic Sans MS", 14, "italic"), foreground="#2F4F4F") 
        
        style.configure("Convert.TButton", font=("Comic Sans MS", 16, "bold"), padding=12, background="#90EE90", foreground="#006400", relief="raised") 
        style.map("Convert.TButton", background=[('active', '#3CB371')], foreground=[('active', '#FFFFFF')]) 

        style.configure("Clear.TButton", font=("Comic Sans MS", 14, "bold"), padding=10, background="#FFD700", foreground="#B8860B", relief="raised") 
        style.map("Clear.TButton", background=[('active', '#DAA520')], foreground=[('active', '#FFFFFF')]) 

    def on_window_resize(self, event):
        self.root.after(10, self._update_status_bar_wraplength)

    def _update_status_bar_wraplength(self):
        current_width = self.status_bar.winfo_width()
        if current_width > 0:
            self.status_bar.configure(wraplength=current_width - 30)

    def convert_to_binary(self, text):
        binary_result = []
        for char in text:
            if char.isdigit():
                binary_char = format(int(char), '08b')
            else:
                binary_char = format(ord(char), '08b')
            binary_result.append(binary_char)
        return ' '.join(binary_result)

    def convert(self):
        text = self.text_entry.get()
        if text:
            binary = self.convert_to_binary(text)
            self.result_text.delete(1.0, tk.END)  
            self.result_text.insert(tk.END, binary)  
            self.status_var.set(f"Awesome! '{text}' is now in secret binary code! ✨ Try another word! 🥳")
        else:
            messagebox.showwarning("Oops!", "Please type in some words first! 😊 What about your name?")
            self.status_var.set("Hmm, I need some words to convert! 🧐")

    def clear_fields(self):
        self.text_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.status_var.set("Fields cleared! Ready for a new secret message! 📝")

def main():
    root = tk.Tk()
    app = CharToBinaryConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()