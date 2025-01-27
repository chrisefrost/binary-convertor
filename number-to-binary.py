import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import font as tkfont

# These lines import the necessary tools to create a graphical user interface (GUI).
# tkinter is a library that helps us create windows, buttons, and other things you see on the screen.
# ttk is a part of tkinter that makes things look more modern.
# messagebox is used to show pop-up messages (like error messages).
# font is used to change how text looks (like making it bold or bigger).

class BinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Georges Binary Number Converter")
        self.root.geometry("640x320")  # This sets the size of the window to 640 pixels wide and 320 pixels tall.
        self.root.resizable(True, True)  # This allows the window to be resized by the user.

        # Configure root grid weights
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        # These lines help the window adjust its size properly when you resize it.

        # Configure styles
        self.setup_styles()
        # This calls a method to set up how things will look (like fonts and colors).

        # Create main container with proper padding
        main_frame = ttk.Frame(root, padding="20 20 20 20", style="Main.TFrame")
        main_frame.grid(row=0, column=0, sticky="nsew")
        # This creates a main frame (a big box) inside the window where everything else will go.
        # The padding adds some space around the edges so things don't look squished.

        # Create and pack the input frame
        input_frame = ttk.Frame(main_frame, style="Input.TFrame")
        input_frame.pack(fill="x", pady=(0, 15))
        # This creates a smaller frame inside the main frame for the input section (where you type numbers).

        # Input section with proper layout
        ttk.Label(input_frame, text="Enter Number:", style="Header.TLabel").pack(side="left", padx=(0, 10))
        # This adds a label (a piece of text) that says "Enter Number:" to the input frame.

        # Create validation command
        vcmd = (self.root.register(self.validate_input), '%P')
        # This sets up a rule to check if what you type is a valid number.

        self.number_entry = ttk.Entry(input_frame, width=15, validate='key', validatecommand=vcmd)
        self.number_entry.pack(side="left", padx=(0, 10))
        self.number_entry.bind('<Return>', lambda e: self.convert())
        self.number_entry.focus()  # Set initial focus
        # This creates a box where you can type a number. It also checks if what you type is valid.
        # When you press the Enter key, it will automatically try to convert the number to binary.

        convert_btn = ttk.Button(input_frame, text="Convert", command=self.convert, style="Convert.TButton")
        convert_btn.pack(side="left")
        # This creates a button that says "Convert". When you click it, it will convert the number to binary.

        # Result section
        result_frame = ttk.Frame(main_frame)
        result_frame.pack(fill="x", pady=(0, 20))
        # This creates another frame for showing the result of the conversion.

        ttk.Label(result_frame, text="Binary Result:", style="Header.TLabel").pack(side="left", padx=(0, 10))
        # This adds a label that says "Binary Result:" to the result frame.

        # Use a Text widget for the binary result so it can be copied
        self.result_text = tk.Text(result_frame, height=1, width=20, font=("Consolas", 12), wrap="none")
        self.result_text.insert(tk.END, "00000000")  # Start with the default value
        self.result_text.pack(side="left", padx=(0, 10))
        # This creates a box where the binary result will be shown. You can copy the text from this box.

        # Table frame
        self.table_frame = ttk.Frame(main_frame, style="Table.TFrame")
        self.table_frame.pack(fill="both", expand=True)
        # This creates a frame for a table that will show how the binary number is made.

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(main_frame, textvariable=self.status_var, style="Status.TLabel")
        status_bar.pack(side="bottom", fill="x", pady=(10, 0))
        # This creates a status bar at the bottom of the window that shows messages like "Ready" or "Error".

        # Initialize the table
        self.create_table("00000000")
        # This sets up the table with the starting binary number "00000000".

    def setup_styles(self):
        style = ttk.Style()
        # This sets up the styles for how things will look.

        # Configure modern-looking styles
        style.configure("Header.TLabel", font=("Segoe UI", 10, "bold"))
        style.configure("Status.TLabel", font=("Segoe UI", 9), foreground="#666666")
        style.configure("Convert.TButton", padding=5)
        style.configure("Table.TFrame", padding=5)
        # These lines set the fonts and colors for different parts of the window.

        # Table styles
        self.header_font = tkfont.Font(family="Segoe UI", weight="bold", size=10)
        self.cell_font = tkfont.Font(family="Consolas", size=10)
        # These lines set the fonts for the table headers and cells.

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
        # This method checks if what you type is a valid number. It allows negative numbers and digits.

    def create_table(self, binary):
        # Clear existing table
        for widget in self.table_frame.winfo_children():
            widget.destroy()
        # This clears the table if there's already something in it.

        binary = binary.replace("-", "")
        # This removes the negative sign from the binary number if it's there.

        # Calculate required bits for the number while ensuring minimum of 8 bits
        num_bits = max(8, len(binary))
        cell_width = 45  # Slightly wider cells for better readability
        # This calculates how many bits (0s and 1s) are needed to show the binary number. It always shows at least 8 bits.

        # Create headers (powers of 2)
        for i in range(num_bits):
            power = num_bits - i - 1
            value = str(2 ** power)
            # This creates the headers for the table, which are powers of 2 (like 128, 64, 32, etc.).

            cell_frame = ttk.Frame(self.table_frame, width=cell_width, height=35)
            cell_frame.grid(row=0, column=i, padx=1, pady=1)
            cell_frame.grid_propagate(False)
            # This creates a small box for each header.

            label = ttk.Label(cell_frame, text=value, font=self.header_font, anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")
            # This puts the header text inside the box.

        # Create binary digits row
        for i in range(num_bits):
            digit = binary[i] if i < len(binary) else "0"
            # This gets each digit of the binary number. If there aren't enough digits, it adds a "0".

            cell_frame = ttk.Frame(self.table_frame, width=cell_width, height=35)
            cell_frame.grid(row=1, column=i, padx=1, pady=1)
            cell_frame.grid_propagate(False)
            # This creates a small box for each binary digit.

            label = ttk.Label(cell_frame, text=digit, font=self.cell_font, anchor="center")
            label.place(relx=0.5, rely=0.5, anchor="center")
            # This puts the binary digit inside the box.

        # Add borders
        for i in range(2):
            for j in range(num_bits):
                cell = self.table_frame.grid_slaves(row=i, column=j)[0]
                cell.configure(relief="solid", borderwidth=1)
        # This adds borders around each box in the table to make it look like a grid.

    def convert_to_binary(self, number):
        if number == 0:
            return "00000000"
        # If the number is 0, it returns "00000000" as the binary result.

        binary = ""
        num = abs(number)
        # This starts with an empty string and takes the absolute value of the number (ignores the negative sign).

        while num > 0:
            binary = str(num % 2) + binary
            num //= 2
        # This converts the number to binary by dividing it by 2 and keeping track of the remainders.

        # Changed to zfill(8) for minimum 8 bits
        binary = binary.zfill(8)
        # This makes sure the binary number is at least 8 digits long by adding zeros at the beginning if needed.

        if number < 0:
            binary = "-" + binary
        # If the original number was negative, it adds a negative sign to the binary result.

        return binary

    def convert(self):
        try:
            number = int(self.number_entry.get())
            binary = self.convert_to_binary(number)
            self.result_text.delete(1.0, tk.END)  # Clear the previous result
            self.result_text.insert(tk.END, binary)  # Insert the new binary result
            self.create_table(binary)
            self.status_var.set(f"Converted successfully! {number} in binary is {binary}")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer")
            self.number_entry.delete(0, tk.END)
            self.status_var.set("Error: Invalid input")
        # This method tries to convert the number you typed into binary. If you type something that's not a number, it shows an error message.

def main():
    root = tk.Tk()
    root.tk.call('tk', 'scaling', 1.5)  # Improve resolution on high-DPI displays
    app = BinaryConverterApp(root)
    root.mainloop()
    # This is the main function that starts the program. It creates the window and runs the app.

if __name__ == "__main__":
    main()
    # This line makes sure the program starts when you run the script.