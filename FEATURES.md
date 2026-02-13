# Feature Guide - Binary Converter Pro

> **Learn by doing! This guide shows you how to use every feature with real examples.**

## Application Overview

Binary Converter Pro is a comprehensive conversion tool with three main tabs that help you understand how computers work with numbers and text:

---

## Tab 1: Number Converter

### Purpose
Convert decimal numbers to Binary, Hexadecimal, and Octal formats simultaneously.

### Features

#### Input
- **Accepts:** Any integer (positive or negative)
- **Examples:** `42`, `-10`, `255`, `-128`
- **Validation:** Real-time - only accepts valid integers

#### Output
Three simultaneous conversions:

1. **Binary**
   - Minimum 8 bits for readability
   - Two's complement for negative numbers
   - Example: `42` → `00101010`

2. **Hexadecimal**
   - Uppercase format
   - Standard 0x prefix omitted for clarity
   - Example: `255` → `FF`

3. **Octal**
   - Standard octal format
   - Example: `42` → `52`

#### Visual Binary Breakdown
- Interactive table showing:
  - Powers of 2 in top row
  - Binary digits in bottom row
  - Color coded: Green for 1, Red for 0
  - Scrollable for large numbers

#### Actions
- **Copy buttons** for each result
- **Clear button** to reset all fields
- **Enter key** to convert

### Examples

**Example 1: Positive Number**
```
Input: 42
Binary:       00101010
Hexadecimal:  2A
Octal:        52

Table:
32 | 16 | 8 | 4 | 2 | 1
0  | 0  | 1 | 0 | 1 | 0
```

**Example 2: Negative Number (Two's Complement)**
```
Input: -42
Binary:       11010110 (8-bit two's complement)
Hexadecimal:  -2A
Octal:        -52
```

**Example 3: Large Number**
```
Input: 1024
Binary:       10000000000
Hexadecimal:  400
Octal:        2000
```

---

## Tab 2: Text Converter

### Purpose
Convert text strings to binary representation (ASCII encoding).

### Features

#### Input
- **Accepts:** Any text (letters, numbers, symbols, spaces)
- **Examples:** `Hello`, `123`, `Hello World!`
- **No length limit**

#### Output

1. **Binary Result**
   - Space-separated 8-bit values
   - One byte per character
   - Scrollable text area
   - Word-wrapped for readability

2. **Character Breakdown Table**
   - Columns: Character | Binary | Decimal
   - Shows each character's encoding
   - Scrollable for long text
   - Special character display (space shown as ␣)

#### Actions
- **Copy Binary** - Copy the binary output
- **Export to File** - Save results to .txt file
  - Includes original text
  - Binary output
  - Full character breakdown
- **Clear button** to reset

### Examples

**Example 1: Word**
```
Input: "Hi"

Binary Result:
01001000 01101001

Character Breakdown:
Char | Binary    | Decimal
------------------------------
 H   | 01001000 | 72
 i   | 01101001 | 105
```

**Example 2: Sentence**
```
Input: "Hello!"

Binary Result:
01001000 01100101 01101100 01101100 01101111 00100001

Character Breakdown:
Char | Binary    | Decimal
------------------------------
 H   | 01001000 | 72
 e   | 01100101 | 101
 l   | 01101100 | 108
 l   | 01101100 | 108
 o   | 01101111 | 111
 !   | 00100001 | 33
```

**Example 3: Numbers**
```
Input: "123"

Binary Result:
00110001 00110010 00110011

Character Breakdown:
Char | Binary    | Decimal
------------------------------
 1   | 00110001 | 49
 2   | 00110010 | 50
 3   | 00110011 | 51
```

---

## Tab 3: Binary Decoder

### Purpose
Decode binary strings back to numbers or text.

### Features

#### Mode Selection
Two decoding modes:

1. **Number Mode**
   - Decodes binary to decimal
   - Shows calculation breakdown
   - Signed/unsigned toggle

2. **Text (ASCII) Mode**
   - Decodes binary to text
   - Requires space-separated values
   - One byte (8 bits) per character

#### Input
- **Number Mode:** Single binary value
  - Example: `101010` or `00101010`
- **Text Mode:** Space-separated binary
  - Example: `01001000 01101001`

#### Options
- **Signed Checkbox:** (Number mode only)
  - Unchecked: Unsigned interpretation
  - Checked: Two's complement interpretation

#### Output
- **Number Mode:**
  - Decimal value
  - Step-by-step calculation
  - Shows which powers of 2 contribute

- **Text Mode:**
  - Decoded text string
  - Direct ASCII interpretation

#### Actions
- **Copy Result** button
- **Clear button** to reset

### Examples

**Example 1: Binary to Unsigned Number**
```
Input: 00101010
Mode: Number
Signed: ☐ (unchecked)

Result:
Decimal Value: 42

Calculation:
  2^5 = 32
  2^3 = 8
  2^1 = 2
  --------
  Total = 42
```

**Example 2: Binary to Signed Number**
```
Input: 11111111
Mode: Number
Signed: ☑ (checked)

Result:
Decimal Value: -1

(Two's complement interpretation)
```

**Example 3: Binary to Unsigned Number (same input)**
```
Input: 11111111
Mode: Number
Signed: ☐ (unchecked)

Result:
Decimal Value: 255

Calculation:
  2^7 = 128
  2^6 = 64
  2^5 = 32
  2^4 = 16
  2^3 = 8
  2^2 = 4
  2^1 = 2
  2^0 = 1
  --------
  Total = 255
```

**Example 4: Binary to Text**
```
Input: 01001000 01100101 01101100 01101100 01101111
Mode: Text (ASCII)

Result:
Decoded Text:

Hello
```

**Example 5: Numbers as Text**
```
Input: 00110001 00110010 00110011
Mode: Text (ASCII)

Result:
Decoded Text:

123
```

---

## Common Workflows

### 1. Encode a Secret Message
1. Go to **Text Converter** tab
2. Enter your message: `Meet at noon`
3. Click **Convert**
4. Click **Copy Binary** or **Export to File**
5. Share the binary with recipient

### 2. Decode a Binary Message
1. Receive binary: `01001000 01101001`
2. Go to **Binary Decoder** tab
3. Select **Text (ASCII)** mode
4. Paste the binary
5. Click **Decode**
6. Read the message: `Hi`

### 3. Convert Decimal to Hex
1. Go to **Number Converter** tab
2. Enter number: `255`
3. Look at Hexadecimal result: `FF`
4. Click **Copy** to use in code

### 4. Understand Binary Structure
1. Go to **Number Converter** tab
2. Enter any number: `42`
3. Look at the visual table
4. See which powers of 2 make up the number

### 5. Check Two's Complement
1. Go to **Number Converter** tab
2. Enter negative number: `-1`
3. See binary: `11111111` (8-bit)
4. Verify in **Binary Decoder** tab:
   - Paste `11111111`
   - Check "signed"
   - Result: `-1` ✓

---

## Tips & Tricks

### Keyboard Shortcuts
- **Enter** - Convert/Decode in current tab
- **Tab** - Navigate between fields
- **Ctrl+C** - Copy selected text

### Understanding Two's Complement
- Leftmost bit is the sign bit
- `0` = positive, `1` = negative
- To negate: Flip all bits and add 1
- Example: `42` → `00101010`
  - Flip: `11010101`
  - Add 1: `11010110` = `-42`

### Binary to Hex Quick Conversion
- Group binary in sets of 4 bits
- Each group = 1 hex digit
- Example: `11111111`
  - `1111` = `F`
  - `1111` = `F`
  - Result: `FF`

### ASCII Ranges
- `0-9`: 48-57 (00110000-00111001)
- `A-Z`: 65-90 (01000001-01011010)
- `a-z`: 97-122 (01100001-01111010)
- Space: 32 (00100000)

### Common Values
| Decimal | Binary   | Hex | Octal |
|---------|----------|-----|-------|
| 0       | 00000000 | 0   | 0     |
| 1       | 00000001 | 1   | 1     |
| 8       | 00001000 | 8   | 10    |
| 16      | 00010000 | 10  | 20    |
| 255     | 11111111 | FF  | 377   |
| 256     | 100000000| 100 | 400   |

---

## Status Bar Messages

The status bar at the bottom provides real-time feedback:

- **"Ready"** - Application started
- **"Converted: X → Binary: Y"** - Successful number conversion
- **"Converted 'text' to binary (N characters)"** - Text conversion complete
- **"Decoded: binary → result"** - Binary decoded successfully
- **"Copied to clipboard!"** - Copy operation successful
- **"Exported to path"** - File save successful
- **"Cleared"** - Fields cleared
- **"Error: ..."** - Problem occurred, check input

---

## Troubleshooting

### "Invalid Input" Error
- **Number Converter:** Enter only integers (whole numbers)
- **Binary Decoder:** Use only 0s and 1s
- **Text Converter:** Should accept all text - report if issues

### Copy Not Working
- Ensure `pyperclip` is installed: `pip install pyperclip`
- Some systems may require additional setup

### Results Look Wrong
- Check if number is negative (two's complement)
- For binary decoder, verify signed/unsigned setting
- Text mode requires space-separated binary

### Window Too Small
- Resize window - interface is responsive
- Minimum size: 800x600
- Recommended: 900x700 or larger

---

## Advanced Use Cases

### Programming
- Convert hex color codes: `0xFF0000` = `255` red
- Debug binary flags: `10110101`
- Understand network byte order

### Education
- Learn binary arithmetic
- Understand ASCII encoding
- Explore number systems

### Data Analysis
- Decode binary data files
- Verify checksums
- Inspect bit patterns

### Security/CTF
- Decode binary messages
- Convert between bases quickly
- Analyze binary flags
