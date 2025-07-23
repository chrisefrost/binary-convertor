import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Number Converter ✨")
        self.root.geometry("850x550")
        self.root.minsize(width=450, height=400) 
        self.root.resizable(True, True)

        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)

        self.setup_styles()

        main_frame = ttk.Frame(root, padding="20 20 20 20", style="Main.TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")
        
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_rowconfigure(2, weight=1) 

        input_frame = ttk.Frame(main_frame, style="Input.TFrame")
        input_frame.grid(row=0, column=0, sticky="ew", pady=(0, 15))
        
        # --- FIX START: Configure rows and columns for vertical layout ---
        input_frame.grid_rowconfigure(0, weight=0) # For "Enter Number:" label
        input_frame.grid_rowconfigure(1, weight=0) # For text entry
        input_frame.grid_rowconfigure(2, weight=0) # For buttons
        
        input_frame.grid_columnconfigure(0, weight=1) # Allow column 0 to expand for text box and button alignment
        # --- FIX END ---

        ttk.Label(input_frame, text="Type your secret number here:", style="Header.TLabel").grid(row=0, column=0, padx=(0, 10), sticky="w")

        vcmd = (self.root.register(self.validate_input), '%P')

        self.number_entry = ttk.Entry(input_frame, width=15, validate='key', validatecommand=vcmd, font=("Consolas", 14))
        # --- FIX START: Place text box under label ---
        self.number_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10), pady=(5, 10))
        # --- FIX END ---
        self.number_entry.bind('<Return>', lambda e: self.convert())
        self.number_entry.focus()

        button_frame = ttk.Frame(input_frame)
        # --- FIX START: Place button frame below text box ---
        button_frame.grid(row=2, column=0, sticky="w", padx=(0, 10)) # Align to left within its column
        # --- FIX END ---

        convert_btn = ttk.Button(button_frame, text="🔐 Convert It", command=self.convert, style="Convert.TButton")
        convert_btn.pack(side="left", padx=(0, 10)) 

        clear_btn = ttk.Button(button_frame, text="Clear", command=self.clear_fields, style="Clear.TButton")
        clear_btn.pack(side="left") 

        result_frame = ttk.Frame(main_frame, style="Result.TFrame") 
        result_frame.grid(row=1, column=0, sticky="ew", pady=(0, 20)) 
        result_frame.grid_columnconfigure(0, weight=0) 
        result_frame.grid_columnconfigure(1, weight=1) 

        ttk.Label(result_frame, text="Binary Result:", style="Header.TLabel").grid(row=0, column=0, padx=(0, 10), sticky="w")

        self.result_text = tk.Text(result_frame, height=1, font=("Consolas", 16, "bold"), foreground="#CD5C5C", bg="#FFF0F5", relief="sunken", bd=3, wrap="none")
        self.result_text.insert(tk.END, "00000000")
        self.result_text.grid(row=0, column=1, sticky="ew")

        self.table_frame = ttk.Frame(main_frame, style="Table.TFrame")
        self.table_frame.grid(row=2, column=0, sticky="nsew") 
        self.table_frame.grid_columnconfigure(0, weight=1) 
        self.table_frame.grid_rowconfigure(0, weight=1) 

        self.status_var = tk.StringVar()
        self.status_var.set("Ready to convert numbers! 🚀") 
        self.status_bar = ttk.Label(main_frame, textvariable=self.status_var, style="Status.TLabel", anchor="w")
        self.status_bar.grid(row=3, column=0, sticky="ew", pady=(10, 0)) 
        
        self.root.bind("<Configure>", self.on_window_resize)

        self.create_table("00000000")

    def setup_styles(self):
        style = ttk.Style()
        style.theme_use('clam') 

        style.configure("Main.TFrame", background="#FFDAB9") 
        style.configure("Input.TFrame", background="#FFC0CB", borderwidth=5, relief="raised") 
        style.configure("Result.TFrame", background="#FFF0F5", borderwidth=5, relief="ridge") 
        style.configure("Table.TFrame", background="#FFF0F5", padding=5) 

        style.configure("Table.Cell.TFrame", background="#D3D3D3", relief="solid", borderwidth=1)

        style.configure("Header.TLabel", font=("Comic Sans MS", 16, "bold"), foreground="#8B0000") 
        style.configure("Status.TLabel", font=("Comic Sans MS", 12, "italic"), foreground="#800000") 
        
        style.configure("Convert.TButton", font=("Comic Sans MS", 14, "bold"), padding=10, background="#FFA07A", foreground="#A52A2A", relief="raised") 
        style.map("Convert.TButton", background=[('active', '#F08080')], foreground=[('active', '#FFFFFF')]) 

        style.configure("Clear.TButton", font=("Comic Sans MS", 14, "bold"), padding=10, background="#FFD700", foreground="#B8860B", relief="raised") 
        style.map("Clear.TButton", background=[('active', '#DAA520')], foreground=[('active', '#FFFFFF')]) 

        self.header_font = tkfont.Font(family="Consolas", weight="bold", size=11)
        self.cell_font = tkfont.Font(family="Consolas", size=11)

    def validate_input(self, value):
        if value == "" or value == "-":
            return True
        try:
            int(value)
            return True
        except ValueError:
            return False

    def on_window_resize(self, event):
        self.root.after(10, self._update_status_bar_wraplength)

    def _update_status_bar_wraplength(self):
        current_width = self.status_bar.winfo_width()
        if current_width > 0:
            self.status_bar.configure(wraplength=current_width - 30)

    def create_table(self, binary):
        for widget in self.table_frame.winfo_children():
            widget.destroy()

        binary = binary.replace("-", "")

        num_bits = max(8, len(binary))
        
        padded_binary = binary.zfill(num_bits)

        cell_width = 45

        for i in range(num_bits):
            power = num_bits - i - 1
            value = str(2 ** power)

            cell_frame = ttk.Frame(self.table_frame, width=cell_width, height=35, style="Table.Cell.TFrame") 
            cell_frame.grid(row=0, column=i, padx=1, pady=1)
            cell_frame.grid_propagate(False)

            label = ttk.Label(cell_frame, text=value, font=self.header_font, anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(num_bits):
            digit = padded_binary[i]

            cell_frame = ttk.Frame(self.table_frame, width=cell_width, height=35, style="Table.Cell.TFrame")
            cell_frame.grid(row=1, column=i, padx=1, pady=1)
            cell_frame.grid_propagate(False)

            label = ttk.Label(cell_frame, text=digit, font=self.cell_font, anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")

        for i in range(num_bits):
            self.table_frame.grid_columnconfigure(i, weight=1)

    def convert_to_binary(self, number):
        if number == 0:
            return "00000000"

        binary = ""
        num = abs(number)

        while num > 0:
            binary = str(num % 2) + binary
            num //= 2

        binary = binary.zfill(8) 

        if number < 0:
            binary = "-" + binary

        return binary

    def convert(self):
        try:
            number = int(self.number_entry.get())
            binary = self.convert_to_binary(number)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, binary)
            self.create_table(binary)
            self.status_var.set(f"Converted successfully! {number} in binary is {binary} 🎉")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer (e.g., 123, -5).")
            self.number_entry.delete(0, tk.END)
            self.status_var.set("Error: Invalid input 🙁")

    def clear_fields(self):
        self.number_entry.delete(0, tk.END)
        self.result_text.delete(1.0, tk.END)
        self.create_table("00000000") 
        self.status_var.set("Fields cleared! Ready for a new number! 🔢")

def main():
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 1.5) 
    app = BinaryConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()