"""
Modern Binary Converter Application
A unified GUI application for all conversion operations
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import pyperclip
from converter_logic import BinaryConverter, ASCIIConverter, ConversionHelper


class ModernBinaryConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Binary Converter Pro")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)

        # Configure styles
        self.setup_styles()

        # Create notebook (tabbed interface)
        self.notebook = ttk.Notebook(root, style="TNotebook")
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Create tabs
        self.create_number_converter_tab()
        self.create_ascii_converter_tab()
        self.create_binary_decoder_tab()

        # Status bar
        self.status_var = tk.StringVar()
        self.status_var.set("Ready")
        status_bar = ttk.Label(root, textvariable=self.status_var, style="Status.TLabel", relief="sunken", anchor="w")
        status_bar.pack(side="bottom", fill="x", padx=10, pady=(0, 10))

    def setup_styles(self):
        """Configure modern styling"""
        style = ttk.Style()
        style.theme_use('clam')

        # Color scheme - Modern dark/light theme
        bg_main = "#F5F5F5"
        bg_secondary = "#FFFFFF"
        bg_accent = "#2196F3"
        fg_main = "#212121"
        fg_secondary = "#757575"
        fg_accent = "#FFFFFF"

        # Frame styles
        style.configure("Main.TFrame", background=bg_main)
        style.configure("Card.TFrame", background=bg_secondary, relief="flat", borderwidth=1)

        # Label styles
        style.configure("Title.TLabel", font=("Segoe UI", 16, "bold"), foreground=fg_main, background=bg_secondary)
        style.configure("Header.TLabel", font=("Segoe UI", 12, "bold"), foreground=fg_main, background=bg_secondary)
        style.configure("Normal.TLabel", font=("Segoe UI", 10), foreground=fg_main, background=bg_secondary)
        style.configure("Small.TLabel", font=("Segoe UI", 9), foreground=fg_secondary, background=bg_secondary)
        style.configure("Status.TLabel", font=("Segoe UI", 9), foreground=fg_secondary, background=bg_main)

        # Button styles
        style.configure("Accent.TButton", font=("Segoe UI", 10, "bold"), padding=8)
        style.configure("Normal.TButton", font=("Segoe UI", 10), padding=6)
        style.map("Accent.TButton",
                  foreground=[('pressed', fg_accent), ('active', fg_accent)],
                  background=[('pressed', '#1976D2'), ('active', bg_accent)])

        # Notebook style
        style.configure("TNotebook", background=bg_main, borderwidth=0)
        style.configure("TNotebook.Tab", font=("Segoe UI", 10), padding=[20, 10])

    def create_number_converter_tab(self):
        """Create the Number to Binary converter tab"""
        tab = ttk.Frame(self.notebook, style="Main.TFrame")
        self.notebook.add(tab, text="Number Converter")

        # Main container
        container = ttk.Frame(tab, style="Main.TFrame", padding=20)
        container.pack(fill="both", expand=True)

        # Input Card
        input_card = ttk.Frame(container, style="Card.TFrame", padding=20)
        input_card.pack(fill="x", pady=(0, 15))

        ttk.Label(input_card, text="Number to Binary Converter", style="Title.TLabel").pack(anchor="w", pady=(0, 15))

        # Input frame
        input_frame = ttk.Frame(input_card, style="Card.TFrame")
        input_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(input_frame, text="Enter Number:", style="Normal.TLabel").grid(row=0, column=0, sticky="w", pady=(0, 5))

        self.num_entry = ttk.Entry(input_frame, font=("Consolas", 12), width=30)
        self.num_entry.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self.num_entry.bind('<Return>', lambda e: self.convert_number())

        input_frame.grid_columnconfigure(0, weight=1)

        # Buttons
        btn_frame = ttk.Frame(input_card, style="Card.TFrame")
        btn_frame.pack(fill="x", pady=(10, 0))

        ttk.Button(btn_frame, text="Convert", command=self.convert_number, style="Accent.TButton").pack(side="left", padx=(0, 5))
        ttk.Button(btn_frame, text="Clear", command=self.clear_number_fields, style="Normal.TButton").pack(side="left")

        # Results Card
        results_card = ttk.Frame(container, style="Card.TFrame", padding=20)
        results_card.pack(fill="both", expand=True)

        ttk.Label(results_card, text="Results", style="Header.TLabel").pack(anchor="w", pady=(0, 10))

        # Binary result
        self.create_result_row(results_card, "Binary:", "num_binary")

        # Hexadecimal result
        self.create_result_row(results_card, "Hexadecimal:", "num_hex")

        # Octal result
        self.create_result_row(results_card, "Octal:", "num_octal")

        # Binary visualization table
        ttk.Label(results_card, text="Binary Breakdown:", style="Normal.TLabel").pack(anchor="w", pady=(15, 5))

        self.num_table_frame = ttk.Frame(results_card, style="Card.TFrame")
        self.num_table_frame.pack(fill="both", expand=True, pady=(5, 0))

        # Create initial placeholder
        self.create_binary_table(self.num_table_frame, "00000000")

    def create_ascii_converter_tab(self):
        """Create the ASCII to Binary converter tab"""
        tab = ttk.Frame(self.notebook, style="Main.TFrame")
        self.notebook.add(tab, text="Text Converter")

        container = ttk.Frame(tab, style="Main.TFrame", padding=20)
        container.pack(fill="both", expand=True)

        # Input Card
        input_card = ttk.Frame(container, style="Card.TFrame", padding=20)
        input_card.pack(fill="x", pady=(0, 15))

        ttk.Label(input_card, text="Text to Binary Converter", style="Title.TLabel").pack(anchor="w", pady=(0, 15))

        ttk.Label(input_card, text="Enter Text:", style="Normal.TLabel").pack(anchor="w", pady=(0, 5))

        self.text_entry = ttk.Entry(input_card, font=("Segoe UI", 12), width=50)
        self.text_entry.pack(fill="x", pady=(0, 10))
        self.text_entry.bind('<Return>', lambda e: self.convert_text())

        # Buttons
        btn_frame = ttk.Frame(input_card, style="Card.TFrame")
        btn_frame.pack(fill="x")

        ttk.Button(btn_frame, text="Convert", command=self.convert_text, style="Accent.TButton").pack(side="left", padx=(0, 5))
        ttk.Button(btn_frame, text="Clear", command=self.clear_text_fields, style="Normal.TButton").pack(side="left")

        # Results Card
        results_card = ttk.Frame(container, style="Card.TFrame", padding=20)
        results_card.pack(fill="both", expand=True)

        ttk.Label(results_card, text="Results", style="Header.TLabel").pack(anchor="w", pady=(0, 10))

        # Binary result
        result_frame = ttk.Frame(results_card, style="Card.TFrame")
        result_frame.pack(fill="both", expand=True, pady=(0, 10))

        ttk.Label(result_frame, text="Binary:", style="Normal.TLabel").pack(anchor="w", pady=(0, 5))

        text_frame = ttk.Frame(result_frame, style="Card.TFrame")
        text_frame.pack(fill="both", expand=True)

        self.text_binary_result = tk.Text(text_frame, font=("Consolas", 11), height=4, wrap="word", bg="#FAFAFA", relief="solid", borderwidth=1)
        self.text_binary_result.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(text_frame, command=self.text_binary_result.yview)
        scrollbar.pack(side="right", fill="y")
        self.text_binary_result.config(yscrollcommand=scrollbar.set)

        # Copy and Export buttons
        action_frame = ttk.Frame(results_card, style="Card.TFrame")
        action_frame.pack(fill="x", pady=(5, 0))

        ttk.Button(action_frame, text="Copy Binary", command=lambda: self.copy_to_clipboard(self.text_binary_result), style="Normal.TButton").pack(side="left", padx=(0, 5))
        ttk.Button(action_frame, text="Export to File", command=self.export_text_results, style="Normal.TButton").pack(side="left")

        # Character breakdown
        ttk.Label(results_card, text="Character Breakdown:", style="Normal.TLabel").pack(anchor="w", pady=(15, 5))

        breakdown_frame = ttk.Frame(results_card, style="Card.TFrame")
        breakdown_frame.pack(fill="both", expand=True)

        self.text_breakdown = tk.Text(breakdown_frame, font=("Consolas", 10), height=6, wrap="none", bg="#FAFAFA", relief="solid", borderwidth=1)
        self.text_breakdown.pack(side="left", fill="both", expand=True)

        breakdown_scroll = ttk.Scrollbar(breakdown_frame, command=self.text_breakdown.yview)
        breakdown_scroll.pack(side="right", fill="y")
        self.text_breakdown.config(yscrollcommand=breakdown_scroll.set)

    def create_binary_decoder_tab(self):
        """Create the Binary to Decimal/Text decoder tab"""
        tab = ttk.Frame(self.notebook, style="Main.TFrame")
        self.notebook.add(tab, text="Binary Decoder")

        container = ttk.Frame(tab, style="Main.TFrame", padding=20)
        container.pack(fill="both", expand=True)

        # Input Card
        input_card = ttk.Frame(container, style="Card.TFrame", padding=20)
        input_card.pack(fill="x", pady=(0, 15))

        ttk.Label(input_card, text="Binary Decoder", style="Title.TLabel").pack(anchor="w", pady=(0, 15))

        # Mode selection
        mode_frame = ttk.Frame(input_card, style="Card.TFrame")
        mode_frame.pack(fill="x", pady=(0, 10))

        ttk.Label(mode_frame, text="Decode as:", style="Normal.TLabel").pack(side="left", padx=(0, 10))

        self.decode_mode = tk.StringVar(value="number")
        ttk.Radiobutton(mode_frame, text="Number", variable=self.decode_mode, value="number", style="Normal.TRadiobutton").pack(side="left", padx=(0, 10))
        ttk.Radiobutton(mode_frame, text="Text (ASCII)", variable=self.decode_mode, value="text", style="Normal.TRadiobutton").pack(side="left")

        ttk.Label(input_card, text="Enter Binary (space-separated for text):", style="Normal.TLabel").pack(anchor="w", pady=(0, 5))

        self.binary_entry = ttk.Entry(input_card, font=("Consolas", 12))
        self.binary_entry.pack(fill="x", pady=(0, 10))
        self.binary_entry.bind('<Return>', lambda e: self.decode_binary())

        # Signed checkbox for numbers
        self.is_signed = tk.BooleanVar(value=False)
        ttk.Checkbutton(input_card, text="Interpret as signed (two's complement)", variable=self.is_signed, style="Normal.TCheckbutton").pack(anchor="w", pady=(0, 10))

        # Buttons
        btn_frame = ttk.Frame(input_card, style="Card.TFrame")
        btn_frame.pack(fill="x")

        ttk.Button(btn_frame, text="Decode", command=self.decode_binary, style="Accent.TButton").pack(side="left", padx=(0, 5))
        ttk.Button(btn_frame, text="Clear", command=self.clear_decoder_fields, style="Normal.TButton").pack(side="left")

        # Results Card
        results_card = ttk.Frame(container, style="Card.TFrame", padding=20)
        results_card.pack(fill="both", expand=True)

        ttk.Label(results_card, text="Decoded Result", style="Header.TLabel").pack(anchor="w", pady=(0, 10))

        result_frame = ttk.Frame(results_card, style="Card.TFrame")
        result_frame.pack(fill="both", expand=True)

        self.decode_result = tk.Text(result_frame, font=("Consolas", 14), height=8, wrap="word", bg="#FAFAFA", relief="solid", borderwidth=1)
        self.decode_result.pack(fill="both", expand=True)

        # Copy button
        ttk.Button(results_card, text="Copy Result", command=lambda: self.copy_to_clipboard(self.decode_result), style="Normal.TButton").pack(anchor="w", pady=(10, 0))

    def create_result_row(self, parent, label_text, attr_prefix):
        """Helper to create a result row with label, text widget, and copy button"""
        frame = ttk.Frame(parent, style="Card.TFrame")
        frame.pack(fill="x", pady=(0, 10))

        ttk.Label(frame, text=label_text, style="Normal.TLabel", width=15).pack(side="left", padx=(0, 10))

        text_widget = tk.Text(frame, font=("Consolas", 12), height=1, wrap="none", bg="#FAFAFA", relief="solid", borderwidth=1)
        text_widget.pack(side="left", fill="x", expand=True, padx=(0, 5))

        setattr(self, f"{attr_prefix}_text", text_widget)

        ttk.Button(frame, text="Copy", command=lambda: self.copy_to_clipboard(text_widget), style="Normal.TButton").pack(side="left")

    def create_binary_table(self, parent, binary_string):
        """Create visual binary breakdown table"""
        # Clear existing widgets
        for widget in parent.winfo_children():
            widget.destroy()

        table_data = ConversionHelper.get_binary_table_data(binary_string)

        # Create canvas with scrollbar for large numbers
        canvas = tk.Canvas(parent, bg="#FFFFFF", height=80, highlightthickness=0)
        scrollbar = ttk.Scrollbar(parent, orient="horizontal", command=canvas.xview)
        scrollable_frame = ttk.Frame(canvas, style="Card.TFrame")

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(xscrollcommand=scrollbar.set)

        # Headers (powers of 2)
        for i, (power, bit) in enumerate(table_data):
            label = tk.Label(scrollable_frame, text=str(power), font=("Consolas", 9, "bold"),
                           bg="#E3F2FD", relief="solid", borderwidth=1, width=8, height=1)
            label.grid(row=0, column=i, padx=1, pady=1, sticky="ew")

        # Bit values
        for i, (power, bit) in enumerate(table_data):
            bg_color = "#C8E6C9" if bit == "1" else "#FFCDD2"
            label = tk.Label(scrollable_frame, text=bit, font=("Consolas", 11, "bold"),
                           bg=bg_color, relief="solid", borderwidth=1, width=8, height=1)
            label.grid(row=1, column=i, padx=1, pady=1, sticky="ew")

        canvas.pack(fill="both", expand=True)
        scrollbar.pack(fill="x")

    def convert_number(self):
        """Convert number to binary, hex, and octal"""
        try:
            number_str = self.num_entry.get().strip()
            if not number_str:
                messagebox.showwarning("Input Required", "Please enter a number")
                return

            number = int(number_str)

            # Convert to different bases
            binary = BinaryConverter.int_to_binary(number)
            hexadecimal = BinaryConverter.int_to_hex(number)
            octal = BinaryConverter.int_to_octal(number)

            # Update results
            self.update_text_widget(self.num_binary_text, binary)
            self.update_text_widget(self.num_hex_text, hexadecimal)
            self.update_text_widget(self.num_octal_text, octal)

            # Update table
            self.create_binary_table(self.num_table_frame, binary)

            self.status_var.set(f"Converted: {number} → Binary: {binary}")

        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid integer")
            self.status_var.set("Error: Invalid input")

    def convert_text(self):
        """Convert text to binary"""
        text = self.text_entry.get()
        if not text:
            messagebox.showwarning("Input Required", "Please enter some text")
            return

        # Convert to binary
        conversions = ASCIIConverter.text_to_binary(text)

        # Display binary result (space-separated)
        binary_result = ' '.join(binary for char, binary in conversions)
        self.text_binary_result.delete(1.0, tk.END)
        self.text_binary_result.insert(tk.END, binary_result)

        # Display breakdown
        self.text_breakdown.delete(1.0, tk.END)
        breakdown_text = "Char | Binary    | Decimal\n"
        breakdown_text += "-" * 30 + "\n"
        for char, binary in conversions:
            char_display = char if char != ' ' else '␣'  # Use visible space symbol
            decimal = int(binary, 2)
            breakdown_text += f" {char_display}   | {binary} | {decimal}\n"

        self.text_breakdown.insert(tk.END, breakdown_text)

        self.status_var.set(f"Converted '{text}' to binary ({len(text)} characters)")

    def decode_binary(self):
        """Decode binary to number or text"""
        binary_input = self.binary_entry.get().strip()
        if not binary_input:
            messagebox.showwarning("Input Required", "Please enter binary data")
            return

        try:
            mode = self.decode_mode.get()

            if mode == "number":
                # Decode as number
                is_signed = self.is_signed.get()
                result = BinaryConverter.binary_to_int(binary_input, is_signed)

                # Show detailed breakdown
                total, breakdown = ConversionHelper.calculate_decimal_from_binary(binary_input.replace(" ", ""))

                output = f"Decimal Value: {result}\n\n"
                output += "Calculation:\n"
                for bit, power, value in breakdown:
                    output += f"  2^{power} = {value}\n"
                if breakdown:
                    output += f"  --------\n"
                    output += f"  Total = {total}"

                self.decode_result.delete(1.0, tk.END)
                self.decode_result.insert(tk.END, output)

                self.status_var.set(f"Decoded: {binary_input} → {result}")

            else:
                # Decode as text
                result = ASCIIConverter.binary_to_text(binary_input)
                self.decode_result.delete(1.0, tk.END)
                self.decode_result.insert(tk.END, f"Decoded Text:\n\n{result}")

                self.status_var.set(f"Decoded binary to text: '{result}'")

        except ValueError as e:
            messagebox.showerror("Decoding Error", f"Invalid binary input: {str(e)}")
            self.status_var.set("Error: Invalid binary input")

    def update_text_widget(self, widget, text):
        """Helper to update a text widget"""
        widget.delete(1.0, tk.END)
        widget.insert(tk.END, text)

    def copy_to_clipboard(self, text_widget):
        """Copy text widget content to clipboard"""
        try:
            content = text_widget.get(1.0, tk.END).strip()
            pyperclip.copy(content)
            self.status_var.set("Copied to clipboard!")
        except Exception as e:
            messagebox.showerror("Copy Error", f"Failed to copy: {str(e)}")

    def export_text_results(self):
        """Export text conversion results to file"""
        content = self.text_binary_result.get(1.0, tk.END).strip()
        if not content:
            messagebox.showwarning("No Data", "Nothing to export")
            return

        file_path = filedialog.asksaveasfilename(
            defaultextension=".txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )

        if file_path:
            try:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write("Binary Conversion Results\n")
                    f.write("=" * 50 + "\n\n")
                    f.write(f"Original Text: {self.text_entry.get()}\n\n")
                    f.write(f"Binary Output:\n{content}\n\n")
                    f.write("Character Breakdown:\n")
                    f.write(self.text_breakdown.get(1.0, tk.END))

                self.status_var.set(f"Exported to {file_path}")
                messagebox.showinfo("Export Successful", f"Results saved to:\n{file_path}")

            except Exception as e:
                messagebox.showerror("Export Error", f"Failed to save file: {str(e)}")

    def clear_number_fields(self):
        """Clear all number converter fields"""
        self.num_entry.delete(0, tk.END)
        self.update_text_widget(self.num_binary_text, "")
        self.update_text_widget(self.num_hex_text, "")
        self.update_text_widget(self.num_octal_text, "")
        self.create_binary_table(self.num_table_frame, "00000000")
        self.status_var.set("Cleared")

    def clear_text_fields(self):
        """Clear all text converter fields"""
        self.text_entry.delete(0, tk.END)
        self.text_binary_result.delete(1.0, tk.END)
        self.text_breakdown.delete(1.0, tk.END)
        self.status_var.set("Cleared")

    def clear_decoder_fields(self):
        """Clear all decoder fields"""
        self.binary_entry.delete(0, tk.END)
        self.decode_result.delete(1.0, tk.END)
        self.status_var.set("Cleared")


def main():
    root = tk.Tk()
    app = ModernBinaryConverterApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
