# Binary Converter Pro

A modern, feature-rich GUI application for converting between different number systems and encoding formats. This comprehensive tool provides conversions for binary, decimal, hexadecimal, octal, and ASCII text with an intuitive tabbed interface.

![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

---

## Features

### 🔢 Number Converter
- **Multi-base conversion**: Convert integers to binary, hexadecimal, and octal simultaneously
- **Two's complement support**: Proper handling of negative numbers using two's complement notation
- **Visual binary breakdown**: Interactive table showing powers of 2 and bit values
- **Copy to clipboard**: One-click copying for all conversion results
- **Input validation**: Real-time validation ensures only valid integers are accepted

### 📝 Text to Binary Converter
- **ASCII encoding**: Convert any text string to binary representation
- **Character breakdown**: Detailed view showing each character's binary, decimal value
- **Export functionality**: Save conversion results to text files
- **Copy to clipboard**: Quick copying of binary output
- **Visual feedback**: Color-coded display for easy reading

### 🔓 Binary Decoder
- **Dual mode decoding**: Decode binary as numbers or ASCII text
- **Signed/unsigned interpretation**: Toggle between signed (two's complement) and unsigned
- **Calculation breakdown**: Shows step-by-step calculation for number conversions
- **Space-separated support**: Handles multi-byte binary strings for text decoding
- **Error handling**: Clear error messages for invalid binary input

### 🎨 Modern UI/UX
- **Tabbed interface**: Clean organization with separate tabs for each converter
- **Responsive design**: Resizable window with adaptive layouts
- **Professional styling**: Modern color scheme with Segoe UI fonts
- **Status bar**: Real-time feedback on operations
- **Keyboard shortcuts**: Press Enter to convert in any input field

---

## Installation

### Prerequisites
- Python 3.7 or higher
- Tkinter (usually included with Python)

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/binary-convertor.git
   cd binary-convertor
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

### Running the Modern App (Recommended)

Run the new unified application with all features:

```bash
python binary_converter_app.py
```

### Legacy Applications

The original separate converters are still available:

**Number to Binary:**
```bash
python number-to-binary.py
```

**ASCII to Binary:**
```bash
python ascii-to-binary.py
```

---

## Examples

### Number Converter
**Input:** `42`

**Output:**
- Binary: `00101010`
- Hexadecimal: `2A`
- Octal: `52`
- Visual table showing: 32 + 8 + 2 = 42

### Text Converter
**Input:** `Hello!`

**Output:**
```
01001000 01100101 01101100 01101100 01101111 00100001
```

**Breakdown:**
```
Char | Binary    | Decimal
------------------------------
 H   | 01001000 | 72
 e   | 01100101 | 101
 l   | 01101100 | 108
 l   | 01101100 | 108
 o   | 01101111 | 111
 !   | 00100001 | 33
```

### Binary Decoder
**Input:** `00101010` (as number)

**Output:**
```
Decimal Value: 42

Calculation:
  2^5 = 32
  2^3 = 8
  2^1 = 2
  --------
  Total = 42
```

**Input:** `01001000 01101001` (as text)

**Output:**
```
Decoded Text:

Hi
```

---

## Project Structure

```
binary-convertor/
├── binary_converter_app.py    # Main unified application (NEW)
├── converter_logic.py          # Core conversion logic (NEW)
├── number-to-binary.py         # Legacy number converter
├── ascii-to-binary.py          # Legacy ASCII converter
├── requirements.txt            # Python dependencies
├── LICENSE.txt                 # MIT License
└── README.md                   # This file
```

---

## Features Comparison

| Feature | Legacy Apps | Binary Converter Pro |
|---------|-------------|---------------------|
| Number to Binary | ✅ | ✅ |
| ASCII to Binary | ✅ | ✅ |
| Binary to Number | ❌ | ✅ |
| Binary to Text | ❌ | ✅ |
| Hexadecimal | ❌ | ✅ |
| Octal | ❌ | ✅ |
| Two's Complement | ❌ | ✅ |
| Copy to Clipboard | ❌ | ✅ |
| Export to File | ❌ | ✅ |
| Modern UI | ❌ | ✅ |
| Tabbed Interface | ❌ | ✅ |
| Calculation Breakdown | ❌ | ✅ |

---

## Technical Details

### Number Systems Supported
- **Binary** (base 2): 0-1
- **Decimal** (base 10): 0-9
- **Hexadecimal** (base 16): 0-9, A-F
- **Octal** (base 8): 0-7

### Two's Complement
Negative numbers are represented using two's complement notation, which is the standard for modern computers:
- `-1` in 8-bit binary: `11111111`
- `-42` in 8-bit binary: `11010110`

### ASCII Encoding
Each character is encoded as an 8-bit binary value (0-255), supporting all standard ASCII characters and extended ASCII.

---

## Keyboard Shortcuts
- **Enter**: Convert current input
- **Tab**: Navigate between input fields
- **Ctrl+C**: Copy selected text

---

## Dependencies
- `pyperclip` (>=1.8.2): Cross-platform clipboard support

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

---

## License

This project is licensed under the MIT License - see the [LICENSE.txt](LICENSE.txt) file for details.

---

## Acknowledgments

- Built with **Python** and **Tkinter**
- Uses **pyperclip** for cross-platform clipboard functionality
- Inspired by the need for a simple, comprehensive binary conversion tool

---

## Roadmap

Future enhancements planned:
- [ ] Support for other encoding formats (UTF-8, UTF-16)
- [ ] Bitwise operation calculator
- [ ] Floating-point binary representation (IEEE 754)
- [ ] Dark mode theme
- [ ] Command-line interface (CLI) version
- [ ] Batch file conversion
- [ ] QR code generation from binary

---

## Support

If you encounter any issues or have questions, please [open an issue](https://github.com/yourusername/binary-convertor/issues) on GitHub.

---