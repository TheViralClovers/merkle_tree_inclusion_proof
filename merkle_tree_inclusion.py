from hashlib import sha256

print("Enter 8 words")
word_list = [input("Enter a word: ") for i in range(8)]
# word_list = ['hello', 'from', 'the ', 'other', 'side', 'i', 'must', 'have']

level_1 = []
level_2 = []

level_3 = [sha256(word.encode("utf-8")).hexdigest() for word in word_list]
[level_2.append(sha256((level_3[i*2]+level_3[i*2+1]).encode("utf-8")).hexdigest()) for i in range(4)]
[level_1.append(sha256((level_2[i*2]+level_2[i*2+1]).encode("utf-8")).hexdigest()) for i in range(2)]
merkle_node = sha256((level_1[0] + level_1[1]).encode("utf-8")).hexdigest()


[print(f"{word_list.index(word)} : {word}") for word in word_list]
[print(f"H({level_3.index(hash_value)}) : {hash_value}") for hash_value in level_3]
[print(f"H(H({(level_2.index(hash_value))*2})+H({(level_2.index(hash_value))*2+1})) : {hash_value}") for hash_value in level_2]
[print(f"H(H(H({(level_1.index(hash_value))*4})+H({(level_1.index(hash_value))*4+1}))+H(H({(level_1.index(hash_value))*4+2})+(H({(level_1.index(hash_value))*4+3}))): {hash_value}") for hash_value in level_1]
print(f"merkle node : {merkle_node}")

hash_to_check = input("Enter the hash of a value to check whether is present in the tree or not: ")
hash_index = int(input("Enter the index to check the value at: "))

if(hash_index<4):
	level_1_hash = input("Enter the value of H(H(H(4)+H(5))+H(H(6)+(H(7))): ")
	level_1_hash_pos = 1
	if(hash_index<2):
		level_2_hash = input("Enter the value of H(H(2)+H(3)): ")
		level_2_hash_pos = 1
		if(hash_index<1):
			level_3_hash = input("Enter the value of H(1): ")
			level_3_hash_pos = 1
		else:
			level_3_hash = input("Enter the value of H(0): ")
			level_3_hash_pos = 0
	else:
		level_2_hash = input("Enter the value of H(H(0)+H(1)): ")
		level_2_hash_pos = 0
		if(hash_index<3):
			level_3_hash = input("Enter the value of H(3): ")
			level_3_hash_pos = 1
		else:
			level_3_hash = input("Enter the value of H(2): ")
			level_3_hash_pos = 0
else:
	level_1_hash = input("Enter the value of H(H(H(0)+H(1))+H(H(2)+(H(3))): ")
	level_1_hash_pos = 0
	if(hash_index<6):
		level_2_hash = input("Enter the value of H(H(6)+H(7)): ")
		level_2_hash_pos = 1
		if(hash_index<5):
			level_3_hash = input("Enter the value of H(5): ")
			level_3_hash_pos = 1
		else:
			level_3_hash = input("Enter the value of H(4): ")
			level_3_hash_pos = 0
	else:
		level_2_hash = input("Enter the value of H(H(4)+H(5)): ")
		level_2_hash_pos = 0
		if(hash_index<7):
			level_3_hash = input("Enter the value of H(7): ")
			level_3_hash_pos = 1
		else:
			level_3_hash = input("Enter the value of H(6): ")
			level_3_hash_pos = 0

if(level_3_hash_pos):
	hash_calc = sha256((hash_to_check+level_3_hash).encode("utf-8")).hexdigest()
else:
	hash_calc = sha256((level_3_hash+hash_to_check).encode("utf-8")).hexdigest()

if(level_2_hash_pos):
	hash_calc = sha256((hash_calc+level_2_hash).encode("utf-8")).hexdigest()
else:
	hash_calc = sha256((level_2_hash+hash_calc).encode("utf-8")).hexdigest()

if(level_2_hash_pos):
	hash_calc = sha256((hash_calc+level_1_hash).encode("utf-8")).hexdigest()
else:
	hash_calc = sha256((level_1_hash+hash_calc).encode("utf-8")).hexdigest()

if(merkle_node==hash_calc):
	print("Given value exists in merkle tree")
else:
	print(f"Value doesn't exists as {merkle_node} is not equal to {hash_calc}")