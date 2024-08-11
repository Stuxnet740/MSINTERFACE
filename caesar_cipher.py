def caesar_cipher(text, shift, operation):
    result = ""
    
    # Iterate through each character in the text
    for char in text:
        # Check if the character is a letter
        if char.isalpha():
            # Determine if the letter is uppercase or lowercase
            ascii_offset = 65 if char.isupper() else 97
            
            # Calculate the new character based on the operation (encryption/decryption)
            if operation == 'encrypt':
                new_char = chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
            elif operation == 'decrypt':
                new_char = chr((ord(char) - ascii_offset - shift) % 26 + ascii_offset)
            
            # Add the new character to the result
            result += new_char
        else:
            # If it's not a letter, just add the original character
            result += char
            
    return result

def main():
    while True:
        print("Caesar Cipher Program")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1' or choice == '2':
            message = input("Enter the message: ")
            shift = int(input("Enter the shift value (integer): "))
            
            if choice == '1':
                encrypted_message = caesar_cipher(message, shift, 'encrypt')
                print(f"Encrypted Message: {encrypted_message}")
            else:
                decrypted_message = caesar_cipher(message, shift, 'decrypt')
                print(f"Decrypted Message: {decrypted_message}")
        
        elif choice == '3':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()