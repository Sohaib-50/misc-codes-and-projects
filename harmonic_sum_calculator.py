n = int(input("n: "))
sum = 0
for i in range(1, n):
  sum += 1/i
  print(f"1/{i} + ", end = "")
sum += 1/n
print(f"1/{n} = ", end = "")
print(round(sum, 3), "\n")
