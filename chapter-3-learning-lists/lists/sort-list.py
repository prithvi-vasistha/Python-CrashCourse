#Sorting a List Permanently with the sort() Method
"""The sort() method changes the order of the list permanently. The cars are now in alphabetical order, and we can never revert to the original order"""
#Once sorted, we cannot get the original list back
marks=[4,5,3,2,1,7,8]
print('Before sorting:')
print(marks)
print()
print()
marks.sort()
print('After sorting:')
print(marks)

print()
print()
print('printing in reverse order/descending order can be done by using reverse=True')
marks.sort(reverse=True)
print(marks)



#Sorting a List Temporarily with the sorted() Function
print()
print()
print('We will use the sorted() method now:')
marks=[4,5,3,2,1,7,8]
print(marks)
print()
print('The sorted list is as follows:')
print(sorted(marks))
print()
print('unsorted list is as follows:')
print(marks)

print()
print()
print('The sorted() method can also accept the "reverse=True" condition by putting a comma next to the list desired to reverse the list')
print(f'Original list:\n{marks}')
print("List sorted using the sorted() method:\n",sorted(marks))
print(f"List sorted using sorted(reverse=True) condition:\n{sorted(marks, reverse=True)}")
print()
print('The original list was not disturbed in any of the examples. So, it can still be printed as follows:\n', marks)