#normal code without classes: 

import binascii
# Python code to demonstrate 
# conversion of a hex string 
# to the binary string 

# function that converts hexadecimal string into binary
def hex_to_binary(hex_string):
    bin_num = ""
    hex_len = len(hex_string)
    i = 0

    while i < hex_len:
        if hex_string[i] == '0':
            bin_num += "0000"
        elif hex_string[i] == '1':
            bin_num += "0001"
        elif hex_string[i] == '2':
            bin_num += "0010"
        elif hex_string[i] == '3':
            bin_num += "0011"
        elif hex_string[i] == '4':
            bin_num += "0100"
        elif hex_string[i] == '5':
            bin_num += "0101"
        elif hex_string[i] == '6':
            bin_num += "0110"
        elif hex_string[i] == '7':
            bin_num += "0111"
        elif hex_string[i] == '8':
            bin_num += "1000"
        elif hex_string[i] == '9':
            bin_num += "1001"
        elif hex_string[i] in {'a', 'A'}:
            bin_num += "1010"
        elif hex_string[i] in {'b', 'B'}:
            bin_num += "1011"
        elif hex_string[i] in {'c', 'C'}:
            bin_num += "1100"
        elif hex_string[i] in {'d', 'D'}:
            bin_num += "1101"
        elif hex_string[i] in {'e', 'E'}:
            bin_num += "1110"
        elif hex_string[i] in {'f', 'F'}:
            bin_num += "1111"
        i += 1

    return bin_num

#function given a binary string, permutes it according to a permutation table
def permute_binary(binary_string, permutation_table):
    # Convert the input string to a list of characters
    input_list = list(binary_string)

    # Ensure input_list is long enough to cover the maximum index in permutation_table
    max_index = max(permutation_table)
    input_list.extend(['0'] * (max_index - len(input_list) + 1))

    # Create an empty list to store the permuted bits
    permuted_bits = []

    # Apply the permutation
    for index in permutation_table:
        # Adjust the 1-indexed index to 0-indexed
        adjusted_index = index - 1

        # Append the corresponding bit to the permuted list
        permuted_bits.append(input_list[adjusted_index])

    # Join the list of bits into a string
    result_string = ''.join(permuted_bits)

    return result_string

def initial_permutation(plain_text):
    binary_text = hex_to_binary(plain_text)
    ip_table = [
        58, 50, 42, 34, 26, 18, 10, 2,
        60, 52, 44, 36, 28, 20, 12, 4,
        62, 54, 46, 38, 30, 22, 14, 6,
        64, 56, 48, 40, 32, 24, 16, 8,
        57, 49, 41, 33, 25, 17, 9, 1,
        59, 51, 43, 35, 27, 19, 11, 3,
        61, 53, 45, 37, 29, 21, 13, 5,
        63, 55, 47, 39, 31, 23, 15, 7
    ]
    result_IP= permute_binary(binary_text, ip_table)
    # Split the result into two halves
    half_length = len(result_IP) // 2
    L_zero = result_IP[:half_length]
    R_zero = result_IP[half_length:]

    return L_zero, R_zero


def left_circular_shift(bits, shift):
    return bits[shift:] + bits[:shift]
    
def generate_PC1(key):
    binary_key = hex_to_binary(key)
    pc1_table = [
        57, 49, 41, 33, 25, 17, 9,
        1, 58, 50, 42, 34, 26, 18,
        10, 2, 59, 51, 43, 35, 27,
        19, 11, 3, 60, 52, 44, 36,
        63, 55, 47, 39, 31, 23, 15,
        7, 62, 54, 46, 38, 30, 22, 
        14, 6, 61, 53, 45, 37, 29,
        21, 13, 5, 28, 20, 12, 4
    ]
        # Perform Permuted Choice 1 (PC1)
    PC1 = permute_binary(binary_key, pc1_table)
    return PC1

def generate_PC2(key, leftcs):
    binary_key = hex_to_binary(key)
    # print("binary key:", binary_key+ '\n') 
    pc2_table = [
        14, 17, 11, 24, 1, 5, 3, 28,
        15, 6, 21, 10, 23, 19, 12, 4,
        26, 8, 16, 7, 27, 20, 13, 2,
        41, 52, 31, 37, 47, 55, 30, 40,
        51, 45, 33, 48, 44, 49, 39, 56,
        34, 53, 46, 42, 50, 36, 29, 32
    ]




    # print ("PC1: ", PC1+ '\n')

    # Split the key into left and right halves

    
        # Perform Permuted Choice 2 (PC2)
    PC2 = permute_binary(leftcs, pc2_table)
    return PC2


# Function to find the 
# XOR of the two Binary Strings
def xor(a, b, n):
	ans = ""
	
	# Loop to iterate over the
	# Binary Strings
	for i in range(n):
		
		# If the Character matches
		if (a[i] == b[i]): 
			ans += "0"
		else: 
			ans += "1"
	return ans 
s1 = [
    [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
    [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
    [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
    [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
]

s2 = [
    [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
    [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
    [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
    [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
]

s3 = [
    [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
    [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
    [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
    [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
]

s4 = [
    [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
    [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
    [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
    [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
]

s5 = [
    [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
    [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
    [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
    [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
]

s6 = [
    [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
    [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
    [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
    [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
]

s7 = [
    [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
    [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
    [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
    [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
]

s8 = [
    [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
    [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
    [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
    [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
]
def substitute_sbox(before_subst):

    s_boxes = [s1, s2, s3, s4, s5, s6, s7, s8]
    after_subst = ""

    # Divide the 48-bit input into 8 chunks of 6 bits each
    chunks = [before_subst[i:i+6] for i in range(0, len(before_subst), 6)]

    for i, chunk in enumerate(chunks):
        row = int(chunk[0] + chunk[5], 2)  # Concatenate first and last bit to get the row
        col = int(chunk[1:5], 2)  # Take bits 2-5 to get the column

        # Look up the value in the corresponding S-box
        s_box_value = s_boxes[i][row][col]

        # Convert the S-box value to a 4-bit binary representation
        s_box_binary = format(s_box_value, '04b')

        after_subst += s_box_binary

    return after_subst
## Function to create map between binary
## number and its equivalent hexadecimal
def createMap(um):
    ## Function to create map between binary
## number and its equivalent hexadecimal
	um["0000"] = '0'
	um["0001"] = '1'
	um["0010"] = '2'
	um["0011"] = '3'
	um["0100"] = '4'
	um["0101"] = '5'
	um["0110"] = '6'
	um["0111"] = '7'
	um["1000"] = '8'
	um["1001"] = '9'
	um["1010"] = 'A'
	um["1011"] = 'B'
	um["1100"] = 'C'
	um["1101"] = 'D'
	um["1110"] = 'E'
	um["1111"] = 'F'


def convertBinToHex(bin):
## function to find hexadecimal 
## equivalent of binary
	l = len(bin)
	t = bin.find('.')
	
	## length of string before '.'
	len_left = None
	if (t != -1):
		len_left = t
	else:
		len_left = l
	
	## add min 0's in the beginning to make
	## left substring length divisible by 4 
	for i in range(1, 1 + (4 - len_left % 4) % 4):
		bin = '0' + bin;
	
	## if decimal point exists 
	if (t != -1):
		## length of string after '.'
		len_right = l - len_left - 1
		
		## add min 0's in the end to make right
		## substring length divisible by 4 
		for i in range(1, 1 + (4 - len_right % 4) % 4):
			bin = bin + '0'
	
	## create map between binary and its
	## equivalent hex code
	bin_hex_map = {}
	createMap(bin_hex_map)
	
	i = 0;
	hex = ""
	
	while True:
		## one by one extract from left, substring
		## of size 4 and add its hex code
		hex += bin_hex_map[bin[i: i+4]];
		i += 4;
		if (i == len(bin)):
			break;
			
		## if '.' is encountered add it
		## to result
		if (bin[i] == '.'):
			hex += '.';
			i+=1
	
	## required hexadecimal number
	return hex;



def des_encrypt(message, key):
    # Initial Permutation
    L_zero, R_zero = initial_permutation(message)

    PC1 = generate_PC1(key)
    for round_num in range(16):
        print(f"\nRound {round_num + 1}:")
        e_box = [
        32, 1,  2,  3,  4,  5,
        4, 5,  6,  7,  8,  9,
        8, 9, 10, 11, 12, 13,
        12,13, 14, 15, 16, 17,
        16,17, 18, 19, 20, 21,
        20,21, 22, 23, 24, 25,
        24,25, 26, 27, 28, 29,
        28,29, 30, 31, 32, 1
        ]
        expansion_p = permute_binary(R_zero, e_box)
        print("  Expansion Permutation (E-box):", expansion_p)
        shifts = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]
        # Perform Left Circular Shift
        if (round_num==0):
            C, D = PC1[:28], PC1[28:]
            leftcs= PC1         
        else:
            C,D= leftcs[:28], leftcs[28:]

        C = left_circular_shift(C, shifts[round_num])
        D = left_circular_shift(D, shifts[round_num])
        leftcs = C + D

        PC2 = generate_PC2(key, leftcs)
        print("  Round Key:", convertBinToHex(PC2))

        before_subst = xor(expansion_p, PC2, len(PC2))
        print("  XOR with round key:", before_subst)

        before_P = substitute_sbox(before_subst)
        print("  Substitution with S-box:", before_P)


        table_p = [16, 7, 20, 21, 29, 12, 28, 17,
                    1, 15, 23, 26,  5, 18, 31, 10,
                    2,  8, 24, 14, 32, 27,  3,  9,
                    19, 13, 30,  6, 22, 11,  4, 25
                    ]
        after_P = permute_binary(before_P, table_p)
        print("  Permutation Function P:", after_P)

        R_one = xor(after_P, L_zero, len(L_zero))
        # Display R0 and R1 in hexadecimal
        print(f"  R_zero: {convertBinToHex(R_zero)}")
        print(f"  R_one : {convertBinToHex(R_one)}")

        # Prepare for the next round
        L_zero = R_zero
        R_zero = R_one 
        # After 16 rounds, perform 32-bit swap
    R_zero, L_zero = L_zero, R_zero

    print("\nAfter 32-bit Swap:")
    print(f"  R_zero: {convertBinToHex(R_zero)}")
    print(f"  L_zero: {convertBinToHex(L_zero)}")

    # Inverse Initial Permutation
    final_result = inverse_initial_permutation(R_zero, L_zero)
    print("\nFinal Result after Inverse Initial Permutation:")
    print(f"  Result: {convertBinToHex(final_result)}")

iip_table = [
    40, 8, 48, 16, 56, 24, 64, 32,
    39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30,
    37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28,
    35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26,
    33, 1, 41, 9, 49, 17, 57, 25
]

def inverse_initial_permutation(left, right):
    return permute_binary(left + right,iip_table)

# Example usage
# message = "02468aceeca86420"
# key = "0f1571c947d9e859"
# des_encrypt(message, key)

#----------------- TRUE CODE------------#

# Hexadecimal to binary conversion


def hex2bin(s):
	mp = {'0': "0000",
		'1': "0001",
		'2': "0010",
		'3': "0011",
		'4': "0100",
		'5': "0101",
		'6': "0110",
		'7': "0111",
		'8': "1000",
		'9': "1001",
		'A': "1010",
		'B': "1011",
		'C': "1100",
		'D': "1101",
		'E': "1110",
		'F': "1111"}
	bin = ""
	for i in range(len(s)):
		bin = bin + mp[s[i]]
	return bin

# Binary to hexadecimal conversion


def bin2hex(s):
	mp = {"0000": '0',
		"0001": '1',
		"0010": '2',
		"0011": '3',
		"0100": '4',
		"0101": '5',
		"0110": '6',
		"0111": '7',
		"1000": '8',
		"1001": '9',
		"1010": 'A',
		"1011": 'B',
		"1100": 'C',
		"1101": 'D',
		"1110": 'E',
		"1111": 'F'}
	hex = ""
	for i in range(0, len(s), 4):
		ch = ""
		ch = ch + s[i]
		ch = ch + s[i + 1]
		ch = ch + s[i + 2]
		ch = ch + s[i + 3]
		hex = hex + mp[ch]

	return hex

# Binary to decimal conversion


def bin2dec(binary):

	binary1 = binary
	decimal, i, n = 0, 0, 0
	while(binary != 0):
		dec = binary % 10
		decimal = decimal + dec * pow(2, i)
		binary = binary//10
		i += 1
	return decimal

# Decimal to binary conversion


def dec2bin(num):
	res = bin(num).replace("0b", "")
	if(len(res) % 4 != 0):
		div = len(res) / 4
		div = int(div)
		counter = (4 * (div + 1)) - len(res)
		for i in range(0, counter):
			res = '0' + res
	return res

# Permute function to rearrange the bits


def permute(k, arr, n):
	permutation = ""
	for i in range(0, n):
		permutation = permutation + k[arr[i] - 1]
	return permutation

# shifting the bits towards left by nth shifts


def shift_left(k, nth_shifts):
	s = ""
	for i in range(nth_shifts):
		for j in range(1, len(k)):
			s = s + k[j]
		s = s + k[0]
		k = s
		s = ""
	return k

# calculating xow of two strings of binary number a and b


def xor(a, b):
	ans = ""
	for i in range(len(a)):
		if a[i] == b[i]:
			ans = ans + "0"
		else:
			ans = ans + "1"
	return ans


# Table of Position of 64 bits at initial level: Initial Permutation Table
initial_perm = [58, 50, 42, 34, 26, 18, 10, 2,
				60, 52, 44, 36, 28, 20, 12, 4,
				62, 54, 46, 38, 30, 22, 14, 6,
				64, 56, 48, 40, 32, 24, 16, 8,
				57, 49, 41, 33, 25, 17, 9, 1,
				59, 51, 43, 35, 27, 19, 11, 3,
				61, 53, 45, 37, 29, 21, 13, 5,
				63, 55, 47, 39, 31, 23, 15, 7]

# Expansion D-box Table
exp_d = [32, 1, 2, 3, 4, 5, 4, 5,
		6, 7, 8, 9, 8, 9, 10, 11,
		12, 13, 12, 13, 14, 15, 16, 17,
		16, 17, 18, 19, 20, 21, 20, 21,
		22, 23, 24, 25, 24, 25, 26, 27,
		28, 29, 28, 29, 30, 31, 32, 1]

# Straight Permutation Table
per = [16, 7, 20, 21,
	29, 12, 28, 17,
	1, 15, 23, 26,
	5, 18, 31, 10,
	2, 8, 24, 14,
	32, 27, 3, 9,
	19, 13, 30, 6,
	22, 11, 4, 25]

# S-box Table
sbox = [[[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
		[0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
		[4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
		[15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],

		[[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
		[3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
		[0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
		[13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],

		[[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
		[13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
		[13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
		[1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],

		[[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
		[13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
		[10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
		[3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],

		[[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
		[14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
		[4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
		[11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],

		[[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
		[10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
		[9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
		[4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],

		[[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
		[13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
		[1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
		[6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]],

		[[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
		[1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
		[7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
		[2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]]

# Final Permutation Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
			39, 7, 47, 15, 55, 23, 63, 31,
			38, 6, 46, 14, 54, 22, 62, 30,
			37, 5, 45, 13, 53, 21, 61, 29,
			36, 4, 44, 12, 52, 20, 60, 28,
			35, 3, 43, 11, 51, 19, 59, 27,
			34, 2, 42, 10, 50, 18, 58, 26,
			33, 1, 41, 9, 49, 17, 57, 25]


def encrypt(pt, rkb, rk):
	pt = hex2bin(pt)

	# Initial Permutation
	pt = permute(pt, initial_perm, 64)
	print("After initial permutation", bin2hex(pt))

	# Splitting
	left = pt[0:32]
	right = pt[32:64]
	for i in range(0, 16):
		# Expansion D-box: Expanding the 32 bits data into 48 bits
		right_expanded = permute(right, exp_d, 48)

		# XOR RoundKey[i] and right_expanded
		xor_x = xor(right_expanded, rkb[i])

		# S-boxex: substituting the value from s-box table by calculating row and column
		sbox_str = ""
		for j in range(0, 8):
			row = bin2dec(int(xor_x[j * 6] + xor_x[j * 6 + 5]))
			col = bin2dec(
				int(xor_x[j * 6 + 1] + xor_x[j * 6 + 2] + xor_x[j * 6 + 3] + xor_x[j * 6 + 4]))
			val = sbox[j][row][col]
			sbox_str = sbox_str + dec2bin(val)

		# Straight D-box: After substituting rearranging the bits
		sbox_str = permute(sbox_str, per, 32)

		# XOR left and sbox_str
		result = xor(left, sbox_str)
		left = result

		# Swapper
		if(i != 15):
			left, right = right, left
		print("Round ", i + 1, " ", bin2hex(left),
			" ", bin2hex(right), " ", rk[i])

	# Combination
	combine = left + right

	# Final permutation: final rearranging of bits to get cipher text
	cipher_text = permute(combine, final_perm, 64)
	return cipher_text


pt = "02468ACEECA86420"
key = "0F1571C947D9E859"

# Key generation
# --hex to binary
key = hex2bin(key)

# --parity bit drop table
keyp = [57, 49, 41, 33, 25, 17, 9,
		1, 58, 50, 42, 34, 26, 18,
		10, 2, 59, 51, 43, 35, 27,
		19, 11, 3, 60, 52, 44, 36,
		63, 55, 47, 39, 31, 23, 15,
		7, 62, 54, 46, 38, 30, 22,
		14, 6, 61, 53, 45, 37, 29,
		21, 13, 5, 28, 20, 12, 4]

# getting 56 bit key from 64 bit using the parity bits
key = permute(key, keyp, 56)

# Number of bit shifts
shift_table = [1, 1, 2, 2,
			2, 2, 2, 2,
			1, 2, 2, 2,
			2, 2, 2, 1]

# Key- Compression Table : Compression of key from 56 bits to 48 bits
key_comp = [14, 17, 11, 24, 1, 5,
			3, 28, 15, 6, 21, 10,
			23, 19, 12, 4, 26, 8,
			16, 7, 27, 20, 13, 2,
			41, 52, 31, 37, 47, 55,
			30, 40, 51, 45, 33, 48,
			44, 49, 39, 56, 34, 53,
			46, 42, 50, 36, 29, 32]

# Splitting
left = key[0:28] # rkb for RoundKeys in binary
right = key[28:56] # rk for RoundKeys in hexadecimal

rkb = []
rk = []
for i in range(0, 16):
	# Shifting the bits by nth shifts by checking from shift table
	left = shift_left(left, shift_table[i])
	right = shift_left(right, shift_table[i])

	# Combination of left and right string
	combine_str = left + right

	# Compression of key from 56 to 48 bits
	round_key = permute(combine_str, key_comp, 48)

	rkb.append(round_key)
	rk.append(bin2hex(round_key))

print("Encryption")
cipher_text = bin2hex(encrypt(pt, rkb, rk))
print("Cipher Text : ", cipher_text)

print("Decryption")
rkb_rev = rkb[::-1]
rk_rev = rk[::-1]
text = bin2hex(encrypt(cipher_text, rkb_rev, rk_rev))
print("Plain Text : ", text)



# # # Example usage
# message = "02468aceeca86420"
# key = "0f1571c947d9e859"
# des_instance = DES(message, key)
# des_instance.des_encrypt()







