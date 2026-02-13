# Quick Start Guide - Binary Converter Pro

## Installation

1. **Install Python** (3.7 or higher) if you haven't already
   - Download from: https://www.python.org/downloads/
   - Make sure to check "Add Python to PATH" during installation

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## Running the Application

Simply run:
```bash
python binary_converter_app.py
```

## Quick Tutorial

### Tab 1: Number Converter
1. Type any integer (e.g., `42`, `-10`, `255`)
2. Press Enter or click "Convert"
3. See results in Binary, Hexadecimal, and Octal
4. View the visual breakdown table
5. Click "Copy" to copy any result

### Tab 2: Text Converter
1. Type any text (e.g., `Hello World`)
2. Press Enter or click "Convert"
3. See binary representation of each character
4. View the character breakdown table
5. Click "Copy Binary" or "Export to File"

### Tab 3: Binary Decoder
1. Choose mode: "Number" or "Text (ASCII)"
2. Enter binary:
   - For numbers: `101010` or `00101010`
   - For text: `01001000 01101001` (space-separated)
3. For numbers, check "signed" if using two's complement
4. Press Enter or click "Decode"
5. View the decoded result with calculation breakdown

## Tips

- Press **Enter** in any input field to convert
- Use **Copy** buttons for quick clipboard access
- The visual table helps understand binary structure
- Export text conversions to save results
- Signed mode interprets negative numbers correctly

## Common Use Cases

**1. Convert a decimal number to binary:**
- Go to "Number Converter" tab
- Enter: `255`
- Result: `11111111` (Binary), `FF` (Hex), `377` (Octal)

**2. Encode a message:**
- Go to "Text Converter" tab
- Enter: `Secret`
- Export the binary output to share

**3. Decode a binary number:**
- Go to "Binary Decoder" tab
- Select "Number" mode
- Enter: `11111111`
- Uncheck "signed": Result = 255
- Check "signed": Result = -1 (two's complement)

**4. Decode a binary message:**
- Go to "Binary Decoder" tab
- Select "Text (ASCII)" mode
- Enter: `01001000 01100101 01101100 01101100 01101111`
- Result: `Hello`

## Troubleshooting

**App won't start:**
- Make sure Python 3.7+ is installed
- Run `pip install -r requirements.txt`

**Copy button doesn't work:**
- Make sure pyperclip is installed: `pip install pyperclip`

**Numbers look wrong:**
- For negative numbers, make sure you understand two's complement
- Toggle the "signed" checkbox in Binary Decoder

## Need Help?

Check the full [README.md](README.md) for detailed documentation or open an issue on GitHub.
