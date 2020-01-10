n = int(input("Enter size of board: "))
count = 1
print()
print("-"*(4*n))
for i in range (n):
	for j in range(n):
		if 10 <= count < 100:
			s = "  "
		elif count == 100:
			s = " "
		else:
			s = "   "
		print(count, end = s)
		count += 1
	print()
print("-"*(4*n))
