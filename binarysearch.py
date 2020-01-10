def binary_search(lst, search_item):
	bottom = 0
	top = len(lst) - 1
	while bottom <= top:
		mid = (bottom + top)//2
		if lst[mid] == search_item:
			return mid
		elif search_item < lst[mid]:
			top = mid -1
		else:
			bottom = mid + 1
print(binary_search(list(range(1,101)), 1))
