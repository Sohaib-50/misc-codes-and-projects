def main():
	key = get_key()	
	
	ptxt = input("plaintext: ")
	print("")
		
	make_cipher(key, ptxt)
	
	

def get_key():
	while True:
		try:
			return int(input("key: "))
		except:
			print("Please enter a valid key(number).\n")
		
	
	
def make_cipher(k, pt):
	print("ciphertext: ", end = "")
	for c in pt:
		'''if not an alphabet, print out as it is;
		 otherwise manipulate it by formula:
		 (p + k) % 26'''
		if not c.isalpha():
			print(c, end ="")
			
		elif c.isupper():
			print((chr((((ord(c) - 65) + k) % 26) + 65)), end = "")
			
		else:
			print(chr((((ord(c) - 97) + k) % 26) + 97), end = "")
	
	print("")
	
	
if __name__ == "__main__":
	main()
