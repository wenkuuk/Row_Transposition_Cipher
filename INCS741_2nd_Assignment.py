import math
######## Encrypt & Decrypted using dictionary and arrays Message extend Function(Padding the empty spaces at the last row with character 'X')#########
def msg_extend(msg,key_length):
	# caculate remainder empty spaces
	msg_list = list(msg) 
	row = len(msg) % key_length 
	# Padding empty spaces with X in the last row 
	msg_list.extend('X' * int(key_length - row))
	msg_filled = ''.join(msg_list)
	return msg_filled
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
######## Encrypt using dictionaries and arrays Function#########
def Main_Encrypted_dictionaries_arrays():
	print("\nEncrypt The Unencrypted Message M = ") 	
	msg = input().replace(" ", "")
 	# The word w is a key
	print("\nEnter the Key of w ")
	key = input()   
	#create an empty dictionary
	combine_dict = {}

	# msg.lower() means all input message covert to lowercase
	Encrypted(combine_dict, msg_extend(msg.lower(),len(key)),key)

	print("\nUnencrypted Message is M = ", msg)
	print("\nThe Key of w = ", key)
	print("\nEncrypted Message is C = ", Encrypted_sorted(combine_dict, sorted_str = "")) 
	# Q4 Plaintext
	#CRYPTOLOGY IS THE PRACTICE AND STUDY OF TECHNIQUES FOR SECURE COMMUNICATION IN THE PRESENCE OF THIRD PARTIES CALLED ADVERSARIES
def Encrypted(combine_dict, msg_filled,key):
	#create an array and its length is as same as that of key
	Array = [""] * len(key)
	for column_length in range (len(key)): #Run how many times in column
		msg_length = column_length
		while msg_length < len(msg_filled):
			Array[column_length] += msg_filled[msg_length] # Store message string value to array
			msg_length = msg_length + len(key) 	       # The message pointer adds the key length		
		
		# Create a dictionary that has pairs of key and value  
		for x in range (len(key)):
			dict_x = {key[column_length] : Array[column_length]} 	
			combine_dict.update(dict_x)
			x +=1
	return combine_dict
def Encrypted_sorted(combine_dict, sorted_str):
	#Sort Key alphabetical order in dictionary, and this also sorted the pair of value
	sorted_keys = sorted(combine_dict)
	#Store sorted key corresponding value to empty string "sorted_str"
	sorted_dict ={}		
	for w in sorted_keys:
		sorted_dict[w] = combine_dict[w]
		sorted_str += sorted_dict[w]
	return sorted_str
######## Decrypt using dictionaries and arrays Function#########
def Main_Decrypted_dictionaries_arrays():
	print("\nEnter the Encrypted Message C = ")
	msg = input().lower()
	print("\nEnter The Key of W  = ")
	key = input()
	# calculate how many raws 
	num_row = math.ceil(len(msg)/len(key))
	#create an empty dictionary
	combine_dict = {}
	Decrypted(combine_dict,msg_extend(msg,len(key)),key,num_row)
	print("\nEncrypted Message is C = ",msg)
	print("\nThe key of w = ",key)
	print("\nDecrypted Message is M = ", Decrypted_sorted(combine_dict,key,num_row,sorted_str = ""))

	# Q5 Ciphertext
	#eroohalpsmeptroohalsefxphtnlefhhxtwstiiiieoecrastitosplmgeasentmitrasnefylypnhiasnetoiroitaetaxoeetonicrasetltesnicrfwmurnhrrhitrcrxhtpipsrmaimiitpiphlaleiucciptotpe
def Decrypted (combine_dict,msg,key,num_row):
	#create an array and its length is as same as that of key
	array = [""] * len(key)
	sorted_key = sorted(key)
	for i in range (len(key)):
		for msg_pointer in range(num_row):
			array [i] += msg[ msg_pointer + i * num_row] # Store message string value to array				 
		for	column_counter in range(num_row):
			dictionary_x ={sorted_key[i] : array[i]}	
			combine_dict.update(dictionary_x)		
	return combine_dict
def Decrypted_sorted(combine_dict,key, num_row,sorted_str):
	#create an array to print the plaintext from row to row
	plaintext = [""] * num_row
	for i in range (len(key)):
		sorted_str += combine_dict.get(key[i])
	for column_length in range (num_row): #Run how many times in column
		msg_length = column_length
		while msg_length < len(sorted_str):
			plaintext[column_length] += sorted_str[msg_length] # Store message string value to array
			msg_length = msg_length + num_row 	       # The message pointer adds the key length		
	return "".join(plaintext)
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
######## Encrypt & Decrypted using matrix and arrays key pointer Function#########
def key_pointer(w, key_id_number):
    position_number = ""
    for i in range(len(w) + 1):
        for j in range(len(w)):
            if key_id_number[j] == i:
                position_number += str(j)
    return position_number
######## Encrypt & Decrypted using matrix and arrays key id Function#########
def key_id(w):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    numbers_to_key = list(range(len(w)))
    # print(kywrdNumList)
    total = 0
    for i in range(len(alphabet)):
        for j in range(len(w)):
            if alphabet[i] == w[j]:
                total += 1
                numbers_to_key[j] = total
            # if
        # inner for
    # for
    return numbers_to_key
######## Encrypt & Decrypted using matrix and arrays print matrix Function#########
def print_matrix(rows, w, matrix):

    for i in range(rows):
        for j in range(len(w)):
            print(matrix[i][j], end=" ", flush=True)
        print()
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
######## Encrypt using matrix and arrays Function#########
def Main_Encrypted_matrix_arrays():
	M = input("\nEncrypt The Unencrypted Message M = ").replace(" ", "").lower()
	w = input("\nEnter the Key of w = ").lower()
	numbers_to_key = key_id(w)
    # in case characters don't fit the entire grid perfectly.
	add_charac = len(M) % len(w)
    # print(extraLetters)
	joker = len(w) - add_charac
    # print(dummyCharacters
	if add_charac != 0:
		for i in range(joker):
		    M += "X"
    # if


	matrix_rows = int(len(M) / len(w))

    # Converting message into a grid
	matrix = [[0] * len(w) for i in range(matrix_rows)]
	z = 0
	for i in range(matrix_rows):
		for j in range(len(w)):
			matrix[i][j] = M[z]
			z += 1
        # for
    # for
    # getting locations of numbers
	position_number = key_pointer(w, numbers_to_key)
    # cipher
	text_to_encrypt = ""
	encrypt_counter = 0
	for i in range(matrix_rows):
		if encrypt_counter == len(w):
			break
		else:
			h = int(position_number[encrypt_counter])
        # if
		for j in range(matrix_rows):
			text_to_encrypt += matrix[j][h]
        # for
		encrypt_counter += 1
    # for

	print("\nEncrypted Message is C = ",text_to_encrypt)
	
######## Decrypt using matrix and arrays Function#########
def Main_Decrypted_matrix_arrays():
	M = input("\nEnter the Encrypted Message C = ").lower()
	w = input("\nEnter the Key of w = ").lower()
	# assigning numbers to keywords
	numbers_to_key = key_id(w)

	matrix_rows = int(len(M) / len(w))

    # getting locations of numbers
	position_number = key_pointer(w, numbers_to_key)
    # Converting message into a grid
	matrix = [[0] * len(w) for i in range(matrix_rows)]
    
	plain_text = ""
	decrypt_counter = 0
	decrypt_counter2 = 0
  

	for i in range(len(M)):
		h = 0
		if decrypt_counter == len(w):
			decrypt_counter = 0
		else:
			h: int = int(position_number[decrypt_counter])
		for j in range(matrix_rows):
			matrix[j][h] = M[decrypt_counter2]
			decrypt_counter2 += 1
		if decrypt_counter2 == len(M):
			break
		decrypt_counter += 1
	print()
	for i in range(matrix_rows):
		for j in range(len(w)):
			plain_text += str(matrix[i][j])
	print("\nEncrypted Message is C = " + plain_text)
#--------------------------------------------------------------#
#--------------------------------------------------------------#
#--------------------------------------------------------------#
######## Menu Main Function###############
def main():	
	print("\n------------We use two approaches to finish the assignemnt in our group----------\n")		
	print("Choose 1 for Encrypt algorithm data type using dictionaries and arrays\n")
	print("Choose 2 for Encrypt algorithm data type using matrix and arrays\n")
	print("Choose 3 for Decrypt algorithm data type using dictionaries nd arrays\n")
	print("Choose 4 for Decrypt algorithm data type using matrix and arrays")
	print("\nPlease select a choice:")
	choice = int(input())

	if choice ==  1:
		Main_Encrypted_dictionaries_arrays()
        
	elif choice == 2:
		Main_Encrypted_matrix_arrays()

	elif choice == 3:
		Main_Decrypted_dictionaries_arrays()

	elif choice == 4:
		Main_Decrypted_matrix_arrays()

	else:
		print("Exit the menu")
main()
