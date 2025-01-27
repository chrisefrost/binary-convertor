
---

# Binary and ASCII to Binary Converter

A simple graphical user interface (GUI) application to convert **integers** and **ASCII characters/words** into their binary representation. It provides two separate tools:

1. **Binary Number Converter**: Converts integers (positive and negative) into binary.
2. **ASCII to Binary Converter**: Converts ASCII characters or words into their binary representation.

---

## Features

### Binary Number Converter
- **Input Validation**: Only integers (positive and negative) are accepted.
- **Binary Conversion**: Converts the input number into binary, ensuring a minimum of 8 bits for readability.
- **Visual Table**: Displays the conversion as a table with binary digits and corresponding powers of 2.
- **Error Handling**: Displays an error message if the input is invalid.

### ASCII to Binary Converter
- **Input Validation**: Accepts any ASCII characters (letters, numbers, symbols, and spaces).
- **Binary Conversion**: Converts each character into its 8-bit binary representation.
- **Word-Wrapping**: Automatically wraps the binary output if the window is too small.
- **Copyable Output**: The binary result can be easily copied from the output box.

---

## Requirements
- Python 3.x
- Tkinter (usually included with Python installations)

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/binary-number-converter.git
   ```

2. Navigate to the project directory:
   ```bash
   cd binary-number-converter
   ```

---

## Usage

### Binary Number Converter (`binary.py`)
1. Run the application:
   ```bash
   python binary.py
   ```

2. Enter an integer in the input box and click **Convert** or press **Enter**.
3. The binary result will be displayed both as text and in a table format.

**Example**:  
For input `10`, the output will be:
- Binary: `00001010`
- Table view showing powers of 2 and corresponding binary digits.

---

### ASCII to Binary Converter (`ascii-to-binary.py`)
1. Run the application:
   ```bash
   python ascii-to-binary.py
   ```

2. Enter a character or word in the input box and click **Convert** or press **Enter**.
3. The binary result will be displayed in the output box, with each character converted to its 8-bit binary representation.

**Example**:  
For input `Hello!`, the output will be:
```
01001000 01100101 01101100 01101100 01101111 00100001
```

---


## Acknowledgments
- This application uses **Tkinter** for the GUI.
- Inspired by basic number and character conversion algorithms.

---

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE.txt) file for details.

---