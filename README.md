# Row Transposition Cipher Implementation

Encryption is defined as a process of expressing data in the form of a code (encoding). This can
also be mentioned as converting Plaintext to Ciphertext.
Decryption is the process of decoding the encoded data. Converting the ciphertext into plain text.
This process requires a key that we used for encryption. We require a key for encryption. There
are two main types of keys used for encryption and decryption. As part of this project, we are
instructed to perform Encryption and Decryption on a Ciphertext in row transposition.

We chose the python programming language and implemented the tasks using two methods:
1. Encryption and Decryption data type using dictionaries and arrays.
2. Encryption and Decryption data type using matrix and arrays.

# Encryption data type using dictionaries and arrays 

The Encrypted function. 

``` 
def Encrypted(combine_dict, msg_filled):
 #create an array and its length is as same as that of key
 Array = [""] * key_length
 for column_length in range (key_length): #Run how many times in column
 msg_length = column_length
 while msg_length < len(msg_filled):
 # Store message string value to array
 Array[column_length] += msg_filled[msg_length]
 # The message pointer adds the key length
 msg_length = msg_length + key_length

 # Create a dictionary that has pairs of key and value
 for x in range (key_length):
 dict_x = {key[column_length] : Array[column_length]}
 combine_dict.update(dict_x)
 x +=1
 return combine_dict
```
The sorted function

``` 
def Sorted(combine_dict, sorted_str):
 #Sort Key alphabetical order in dictionary, and this also sorted the pair of
value
 sorted_keys = sorted(combine_dict)
 #Store sorted key corresponding value to empty string "sorted_str"
 sorted_dict ={}
 for w in sorted_keys:
 sorted_dict[w] = combine_dict[w]
 sorted_str += sorted_dict[w]
 print(sorted_str)
 return sorted_str
```
Plaintext Extend Function

``` 
def msg_extend(lowecase_msg,key_length):
 # calculate remainder empty spaces
 msg_list = list(lowecase_msg)
 row = len(lowecase_msg) % key_length
 # Padding empty spaces with X in the last row
 msg_list.extend('X' * int(key_length - row))
 msg_filled = ''.join(msg_list)
 return msg_filled
```
Main 
```
print("Encrypt The message M")
msg = input()
print("Enter the Key of w ") # The word w is a key
key = input()
key_length = len(key) # its length is k
#create an empty dictionary
combine_dict = {}
# msg.lower() means all input message covert to lowercase
Encrypted(combine_dict, msg_extend(msg.lower(),key_length))
print("Unencrypted Message is M =", msg)
print("Key is w = ", key)
print("Encrypted Message is C = ", Sorted(combine_dict, sorted_str = ""))
```

```

Example: Message M= How are you (array)
         Let the key= NYIT

    | N | Y | I | T |
    |---|---|---|---|
    | h | o | w |   |
    | a | r | e |   |
    | y | o | u | X |
Encrypted message: .py file
```

# Encryption data type using Matrix and arrays 

Main Encrypted_matrix_array Function 
```
def Main_Encrypted_matrix_arrays():
	M = input("\nEncrypt The Unencrypted Message M = ").replace(" ", "").lower()
	w = input("\nEnter the Key of w = ").lower()
	numbers_to_key = key_id(w)
	add_charac = len(M) % len(w)
	joker = len(w) - add_charac
	if add_charac != 0:
		for i in range(joker):
		    M += "X"
	matrix_rows = int(len(M) / len(w))
	matrix = [[0] * len(w) for i in range(matrix_rows)]
	z = 0
	for i in range(matrix_rows):
		for j in range(len(w)):
			matrix[i][j] = M[z]
			z += 1
	position_number = key_pointer(w, numbers_to_key)
	text_to_encrypt = ""
	encrypt_counter = 0
	for i in range(matrix_rows):
		if encrypt_counter == len(w):
			break
		else:
			h = int(position_number[encrypt_counter])
		for j in range(matrix_rows):
			text_to_encrypt += matrix[j][h]
		encrypt_counter += 1

	print("\nEncrypted Message is C = ",text_to_encrypt)



```

# Decryption algorithm data type using dictionaries and arrays:

Decrypted Main  Decrypted_dictionaries_arrays Function
```
def Main_Decrypted_dictionaries_arrays():
 print("\nEnter the Encrypted Message C = ")
 msg = input().lower()
 print("\nEnter The Key of W = ")
 key = input()
 # calculate how many raws
 num_row = math.ceil(len(msg)/len(key))
 #create an empty dictionary
 combine_dict = {}
 Decrypted(combine_dict,msg_extend(msg,len(key)),key,num_row)
 print("\nEncrypted Message is C = ",msg)
 print("\nThe key of w = ",key)
 print("\nDecrypted Message is M = ", Decrypted_sorted(combine_dict,key,num_ro
w,sorted_str = ""))

```
Decrypted Function
```
def Decrypted (combine_dict,msg,key,num_row):
 #create an array and its length is as same as that of key
 array = [""] * len(key)
 sorted_key = sorted(key)
 for i in range (len(key)):
 for msg_pointer in range(num_row):
 # Store message string value to array
 array [i] += msg[ msg_pointer + i * num_row]

 for column_counter in range(num_row):
 dictionary_x ={sorted_key[i] : array[i]}
 combine_dict.update(dictionary_x)
 return combine_dict
```
Sorted Function
```
def Decrypted_sorted(combine_dict,key, num_row,sorted_str):
 #create an array to print the plaintext from row to row
 plaintext = [""] * num_row
 for i in range (len(key)):
 sorted_str += combine_dict.get(key[i])
 for column_length in range (num_row): #Run how many times in column
 msg_length = column_length
 while msg_length < len(sorted_str):
 # Store message string value to array
 plaintext[column_length] += sorted_str[msg_length]
 # The message pointer adds the key length
 msg_length = msg_length + num_row
 return "".join(plaintext)
```  
# Decryption algorithm data type using matrixs and arrays:
######## Encrypt & Decrypted using matrix and arrays key pointer Function#########
```  
def key_pointer(w, key_id_number):
 position_number = ""
 for i in range(len(w) + 1):
 for j in range(len(w)):
 if key_id_number[j] == i:
 position_number += str(j)
 return position_number
```
######## Encrypt & Decrypted using matrix and arrays key id Function#########
```
def key_id(w):
 alphabet = "abcdefghijklmnopqrstuvwxyz"
 numbers_to_key = list(range(len(w)))

 total = 0
 for i in range(len(alphabet)):
 for j in range(len(w)):
 if alphabet[i] == w[j]:
 total += 1
 numbers_to_key[j] = total
```
Main  Decrypted_matrix_arrays Function
```
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
``` 

  
# Menu main() function 
```
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
```
# Docker Container Setup
```
This part shall be a verification of how the python file and docker file, showing that python runs in docker with output. 
The docker uses certain commands:
* “docker build. -f  INCS741Dockerfile(DOCKER FILE) –t 741assignemnt(FILENAME)”

* “ docker run –it 741assignment.”
Explanation: The reason using “.” and “ -f ” in the command means that. “ ” will build the docker
image to the working directory, “ -f ” will follow the specific name of docker file content as well.
