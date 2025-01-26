Binary Number Converter
=======================

A simple graphical user interface (GUI) application to convert integers into their binary representation.
It allows users to input an integer and view the result in binary format, displayed in both standard binary form and in a visual table format.

Features
--------
- **Input Validation**: Only integers (positive and negative) are accepted.
- **Binary Conversion**: Converts the input number into binary, ensuring a minimum of 8 bits for readability.
- **Visual Table**: Displays the conversion as a table with binary digits and corresponding powers of 2.
- **Error Handling**: Displays an error message if the input is invalid.

Requirements
------------
- Python 3.x
- Tkinter (usually included with Python installations)

Installation
------------
1. Clone the repository:
   ```git clone https://github.com/yourusername/binary-number-converter.git```
2. Navigate to the project directory:
   ```cd binary-number-converter```

3. Run the application:
   ```python binary.py```

Usage
-----
1. Launch the app.
2. Enter an integer in the input box and click "Convert" or press **Enter**.
3. The binary result will be displayed both as text and in a table format.

Example
-------
For input `10`, the output will be:

- Binary: `00001010`
- Table view showing powers of 2 and corresponding binary digits.

Acknowledgments
---------------
- This application uses Tkinter for the GUI.
- Inspired by basic number conversion algorithms.
