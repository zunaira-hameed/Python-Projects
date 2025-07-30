# Encryption method
def encrypt(input_string, encryption_key):
    return "".join(chr(ord(char) + encryption_key) for char in input_string)
    # ord(char) method is used to get ASCII value of each character
    # chr() method is used to convert ASCII value back to the character
    # "".join() method concatenates the encrypted characters into a single string


# Decryption method
def decrypt(encrypted_data, encryption_key):
    return "".join(chr(ord(char) - encryption_key) for char in encrypted_data)


# main method
def main():
    input_string = input("Enter a string: ")
    encryption_key = 3
    encrypted_data = encrypt(input_string, encryption_key)
    decrypted_data = decrypt(encrypted_data, encryption_key)
    print("Encrypted data is: ", encrypted_data)
    print("Decrypted data is: ", decrypted_data)


# Call the main function to get output
main()
