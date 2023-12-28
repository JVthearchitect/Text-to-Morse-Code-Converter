# Morse Code Converter

This Python script converts alphanumeric text to Morse code. It utilizes a predefined Morse code dictionary (`morse_code_dict`) to perform the conversion.

## Usage

1. Clone the repository or download the script.
2. Make sure you have the `morse_code` module with the `morse_code_dict` dictionary.
3. Run the script:

    ```bash
    python morse_code_converter.py
    ```

4. Enter the text you would like to convert when prompted.
5. The script will output the corresponding Morse code for the entered text.

## Morse Code Dictionary

The Morse code dictionary (`morse_code_dict`) maps each alphanumeric character to its Morse code representation. You can customize or extend this dictionary based on your requirements.

```python
# Example Morse Code Dictionary
morse_code_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.',
    's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-',
    'y': '-.--', 'z': '--..',
    # Add more characters as needed
}
```
