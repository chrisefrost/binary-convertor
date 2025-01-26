import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Number Converter")
        self.root.geometry("640x320")  # Golden ratio-based dimensions
        self.root.resizable(False, False)  # Lock window size
        
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
        ttk.Label(input_frame, text="Enter Number:", style="Header.TLabel").pack(side="left", padx=(0, 10))
        
        # Create validation command
        vcmd = (self.root.register(self.validate_input), '%P')
        
        self.number_entry = ttk.Entry(input_frame, width=15, validate='key', validatecommand=vcmd)
        self.number_entry.pack(side="left", padx=(0, 10))
        self.number_entry.bind('<Return>', lambda e: self.convert())
        self.number_entry.focus()  # Set initial focus
        
        convert_btn = ttk.Button(input_frame, text="Convert", command=self.convert, style="Convert.TButton")
        convert_btn.pack(side="left")
        
        # Result section
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill="x", pady=(0, 20))
        
        ttk.Label(result_frame, text="Binary Result:", style="Header.TLabel").pack(side="left", padx=(0, 10))
        
        self.result_var = tk.StringVar()
        self.result_var.set("00000000")
        result_label = ttk.Label(result_frame, textvariable=self.result_var, style="Result.TLabel")
        result_label.pack(side="left")
        
        # Table frame
        self.table_frame = ttk.Frame(main_frame, style="Table.TFrame")
        self.table_frame.pack(fill="both", expand=True)
        
        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, style="Status.TLabel")
        status_bar.pack(side="bottom", fill="x", pady=(10, 0))
        
        # Initialize the table
        self.create_table("00000000")
        
    def setup_styles(self):
        style = ttk.Style()
        
        # Configure modern-looking styles
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Result.TLabel", font=("Consolas", 12), foreground="#0066cc")
        style.configure("Status.TLabel", font=("Segoe UI", 9), foreground="#666666")
        style.configure("Convert.TButton", padding=5)
        style.configure("Table.TFrame", padding=5)
        
        # Table styles
        self.header_font = tkfont.Font(family="Segoe UI", weight="bold", size=10)
        self.cell_font = tkfont.Font(family="Consolas", size=10)

    def validate_input(self, value):
        # Allow empty string or negative sign
        if value == "" or value == "-":
            return True
        # Allow negative numbers and digits only
        try:
            int(value)
            return True
        except ValueError:
            return False

    def create_table(self, binary):
        # Clear existing table
        for widget in self.table_frame.winfo_children():
            widget.destroy()
            
        binary = binary.replace("-", "")
        # Calculate required bits for the number while ensuring minimum of 8 bits
        num_bits = max(8, len(binary))
        cell_width = 45  # Slightly wider cells for better readability
        
        # Create headers (powers of 2)
        for i in range(num_bits):
            power = num_bits - i - 1
            value = str(2 ** power)
            
            cell_frame = ttk.Frame(self.table_frame, width=cell_width, height=35)
            cell_frame.grid(row=0, column=i, padx=1, pady=1)
            cell_frame.grid_propagate(False)
            
            label = ttk.Label(cell_frame, text=value, font=self.header_font, anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")
            
        # Create binary digits row
        for i in range(num_bits):
            digit = binary[i] if i < len(binary) else "0"
            
            cell_frame = ttk.Frame(self.table_frame, width=cell_width, height=35)
            cell_frame.grid(row=1, column=i, padx=1, pady=1)
            cell_frame.grid_propagate(False)
            
            label = ttk.Label(cell_frame, text=digit, font=self.cell_font, anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")
            
        # Add borders
        for i in range(2):
            for j in range(num_bits):
                cell = self.table_frame.grid_slaves(row=i, column=j)[0]
                cell.configure(relief="solid", borderwidth=1)
    
    def convert_to_binary(self, number):
        if number == 0:
            return "00000000"
        
        binary = ""
        num = abs(number)
        
        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        
        # Changed to zfill(8) for minimum 8 bits
        binary = binary.zfill(8)
        
        if number < 0:
            binary = "-" + binary
            
        return binary
    
    def convert(self):
        try:
            number = int(self.number_entry.get())
            binary = self.convert_to_binary(number)
            self.result_var.set(binary)
            self.create_table(binary)
            self.status_var.set(f"Converted {number} to binary successfully")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer")
            self.number_entry.delete(0, tk.END)
            self.status_var.set("Error: Invalid input")

def main():
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 1.5)  # Improve resolution on high-DPI displays
    app = BinaryConverterApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
