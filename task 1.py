def caesar_cipher_encrypt(text, shift):
    def transform(text, shift):
        transformed_text = ""
        for char in text:
            if char.isalpha():
                shift_base = 65 if char.isupper() else 97
                transformed_text += chr((ord(char) - shift_base + shift) % 26 + shift_base)
            else:
                transformed_text += char
        return transformed_text
    return transform(text, shift)

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("####****Caesar Cipher (ENCRYPT & DECRYPT MADE EASY****####")
    print("#### by ADHITHYA MANGALAMPETA #####")
    while True:
        choice = input("Type 'encrypt' to encrypt, 'decrypt' to decrypt, or 'quit' to quit: ").lower()
        if choice == 'quit':
            break
        if choice not in ['encrypt', 'decrypt']:
            print("Invalid choice. Please type 'encrypt', 'decrypt', or 'quit'.")
            continue
        
        message = input("Enter your message: ")
        try:
            shift = int(input("Enter the shift value: "))
        except ValueError:
            print("Invalid shift value. Please enter an integer.")
            continue
        
        if choice == 'encrypt':
            encrypted_message = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {encrypted_message}")
        elif choice == 'decrypt':
            decrypted_message = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {decrypted_message}")

if __name__ == "__main__":
    main()
