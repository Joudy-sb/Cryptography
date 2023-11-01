import numpy as np 

# global variable storing the alphabet
alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

#THIS FUNCTION COMPUTES THE MATRIX MULTIPLICATION
def matrix_mult_HC(plaintext_int, key,mod):
    ciphertext_int=[]
    for i in range(len(key)):
        char_enc=0
        for j in range(len(plaintext_int)):
            char_enc += (key[i][j]*plaintext_int[j])
        ciphertext_int.append(char_enc%mod)
    return ciphertext_int

#THIS FUNCTION REMOVES AND PRESERVE SPECIAL CHARACTERS
def preserve_special_char(plaintext):
    special_char = []
    preserved_text = ""
    for i in range(0,len(plaintext)):
        if plaintext[i].isalpha()!=True:
            special_char.append((plaintext[i],i))
        else:
            preserved_text += plaintext[i]
    return (preserved_text, special_char)

#THIS FUNCTION ADD BACK THE SPECIAL CHARACTERS
def add_preserved_special_char(ciphertext, special_char):
    ciphertext = list(ciphertext)
    for i in special_char: 
        ciphertext.insert(i[1],i[0])
    return ''.join(ciphertext)

#FUNCTION THAT FINDS THE MODULAR INVERSE
def mod_inv(a, m):
    a = a % m
    for x in range(1, m):
        if (a * x) % m == 1:
            return x
    raise ValueError(f"{a} has no inverse mod {m}")

#FUNCTION THAT CHECKS IF A MATRIX IS INVERTIBLE
def matrix_mod_inv(matrix, mod):
    matrix = np.array(matrix, dtype=int)
    det = int(round(np.linalg.det(matrix))) % mod
    if det == 0:
        raise ValueError(f"{matrix} has a determinant of 0 and therefor is not inversible.")
    det_inv = mod_inv(det, mod)
    adj = matrix_cofactor(matrix).T
    matrix_inv = np.mod(det_inv * adj, mod)
    return matrix_inv

#THIS FUNCTION WILL ENCRYPT/DECRYPT A TEXT USING A KEY/INVERSE KEY
def HillCipher(plaintext: str, key: list[list[int]], mod: int) -> str:
    #check if key is invertible, i.e. if the determinant of the matrix is not 0
    matrix_mod_inv(key, mod)
    preserved_text, special_char = preserve_special_char(plaintext)
    #check if the string is compatible with key
    if len(preserved_text)%len(key)!=0:
        preserved_text+=(len(key)-len(preserved_text)%len(key))*"x"
    ciphertext=[]
    # for every k character in the plain text, k being the size of the matrix
    for i in range (0,len(preserved_text),len(key)):
        plaintext_int = []
        for j in range (i,i+len(key)):
            plaintext_int.append(alphabet.index(preserved_text[j]))
        ciphertext_int = []
        ciphertext_int = matrix_mult_HC(plaintext_int, key,mod) 
        for j in range (len(ciphertext_int)):
            ciphertext.append(alphabet[ciphertext_int[j]])
    ciphertext = add_preserved_special_char(ciphertext,special_char)
    return ''.join(ciphertext)

#THIS FUNCTION FINDS THE COFACTOR MATRIX TO FIND THE INVERSE
def matrix_cofactor(matrix):
    nrows, ncols = matrix.shape
    cofactor_matrix = np.zeros((nrows, ncols), dtype=int)
    for i in range(nrows):
        for j in range(ncols):
            minor = np.delete(matrix, i, 0)
            minor = np.delete(minor, j, 1)
            cofactor_matrix[i, j] = ((-1) ** (i + j)) * int(round(np.linalg.det(minor)))
    return cofactor_matrix

#THIS FUNCTION ENCRYPT A TEXT
def encrypt_HC(plaintext: str, key: list[list[int]], mod: int) -> str:
    return HillCipher(plaintext, key, mod)

#THIS FUNCTION DECRYPT A TEXT
def decrypt_HC(ciphertext, key, mod):
    key = matrix_mod_inv(key,mod)
    return HillCipher(ciphertext,key, mod)

#INITIATE INPUT KEY FROM USER
key = []
n = int(input("Enter the size of the key matrix (e.g., for 2x2 enter 2): "))
for i in range(n):
    row_str = input(f"Enter row {i+1} of the matrix, separated by spaces: ")
    row_list = [int(num) for num in row_str.split()]
    key.append(row_list)

#INITIATE MESSAGE FROM USER
s = input("Enter message to encrypt: ")

#INITIATE MOD FROM USER
mod = int(input("Enter mod to use: "))

encrypted_message = encrypt_HC(s,key,mod)
print(encrypted_message)
decrypted_message = decrypt_HC(encrypted_message,key,mod)
print(decrypted_message)


