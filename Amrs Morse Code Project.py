# Morse code
morse_code = {
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.',
    '0': '-----',
    ' ': ' '
}

# Function to encrypt a phrase using Morse code
def encrypt_morse_code(phrase):
    encrypted_phrase = ''
    for char in phrase.upper():
        if char in morse_code:
            encrypted_phrase += morse_code[char] + ' '
        else:
            encrypted_phrase += char + ' '
    return encrypted_phrase.strip()

# Function to decrypt a phrase from Morse code
def decrypt_morse_code(morse_code_phrase):
    decrypted_phrase = ''
    morse_code_words = morse_code_phrase.split(' ')
    for morse_code_word in morse_code_words:
        if morse_code_word in morse_code.values():
            decrypted_phrase += list(morse_code.keys())[list(morse_code.values()).index(morse_code_word)]
        elif morse_code_word == '':
            decrypted_phrase += ' '
    return decrypted_phrase.strip()

# Main program
def main():
    # Get input from the user
    phrase = input("Enter a phrase to encrypt or decrypt: ")

    # Check if the user wants to encrypt or decrypt
    operation = input("Do you want to encrypt (1) or decrypt (2) the phrase? ")

    if operation == "1":
        encrypted_phrase = encrypt_morse_code(phrase)
        print("Encrypted phrase:", encrypted_phrase)
    elif operation == "2":
        decrypted_phrase = decrypt_morse_code(phrase)
        print("Decrypted phrase:", decrypted_phrase)
    else:
        print("Invalid operation. Please choose 1 for encrypt or 2 for decrypt.")

# Testing
if __name__ == "__main__":
    main()
