def generate_matrix(word):
    alphabet = 'abcdefghiklmnopqrstuvwxyz'  # excluding 'j' to avoid repeating letters
    matrix = []
    
    # Remove 'j' from the given word
    word = word.replace('j', 'i')
    
    # Add unique characters from the word to the matrix
    for char in word:
        if char not in matrix:
            matrix.append(char)
    
    # Add remaining characters from the alphabet to complete the matrix
    for char in alphabet:
        if char not in matrix:
            matrix.append(char)
    
    # Reshape the list into a 5x5 matrix
    matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
    
    return matrix

def find_indices(matrix, char):
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if matrix[i][j] == char:
                return i, j

def playfair_encrypt(plaintext, matrix1, matrix2):
    ciphertext = ""
    
    # Remove any spaces and convert the plaintext to lowercase
    plaintext = plaintext.replace(" ", "").lower()
    
    for i in range(0, len(plaintext), 2):
        char1, char2 = plaintext[i], 'x' if i+1 == len(plaintext) else plaintext[i+1]
        char1n= char1
        char2n= char2
        if char1 == 'j':
            char1n = 'i'
        if char2 == 'j':
            char2n = 'i'

        row1_m1, col1_m1 = find_indices(matrix1, char1n)
        row2_m2, col2_m2 = find_indices(matrix2, char2n)
        
        if col1_m1 == col2_m2:
            # If both characters are in the same column, take the characters as is
            encrypted_char1 = char1
            encrypted_char2 = char2
        else:
            # If the characters are not in the same column, use the rules of Playfair cipher
            encrypted_char1 = matrix1[row1_m1][col2_m2]
            encrypted_char2 = matrix2[row2_m2][col1_m1]

        ciphertext += encrypted_char1 + encrypted_char2
    
    return ciphertext
def playfair_decrypt(ciphertext, matrix1, matrix2):
    plaintext = ""
    
    for i in range(0, len(ciphertext), 2):
        char1, char2 = ciphertext[i], ciphertext[i+1]
        char1n= char1
        char2n= char2
        if char1 == 'j':
            char1n = 'i'
        if char2 == 'j':
            char2n = 'i'

        row1_m1, col1_m1 = find_indices(matrix1, char1n)
        row2_m2, col2_m2 = find_indices(matrix2, char2n)
        
        if col1_m1 == col2_m2:
            decrypted_char1 = char1
            decrypted_char2 = char2
        else:
            decrypted_char1 = matrix1[row1_m1][col2_m2]
            decrypted_char2 = matrix2[row2_m2][col1_m1]

        plaintext += decrypted_char1 + decrypted_char2
    
    return plaintext

def main():
    choice = input("Do you want to encrypt or decrypt? Enter 'encrypt' or 'decrypt': ")

    if choice == 'encrypt':
        word1 = input("Enter first word: ")
        word2 = input("Enter second word: ")
        plaintext = input("Enter the plaintext message: ")

        matrix1 = generate_matrix(word1)
        matrix2 = generate_matrix(word2)

        encrypted_text = playfair_encrypt(plaintext, matrix1, matrix2)
        print("Encrypted Text:", encrypted_text)

    elif choice == 'decrypt':
        word1 = input("Enter first word: ")
        word2 = input("Enter second word: ")
        ciphertext = input("Enter the ciphertext message: ")

        matrix1 = generate_matrix(word1)
        matrix2 = generate_matrix(word2)

        decrypted_text = playfair_decrypt(ciphertext, matrix1, matrix2)
        print("Decrypted Text:", decrypted_text)
    else:
        print("Invalid choice. Please enter 'encrypt' or 'decrypt'.")

if __name__ == "__main__":
    main()