# We can make use of the reverse() function to reverse a list in python
# It does not necessarily sort the list in ascending or descending order.
# It just reverses the order of array given
# Eg : list=[1,4,2]
# reverse(list) => provides an output of [2,4,1]

# If descending order of input list is required, we can make use of:
# <list>.sort(reverse=True)
# or
# sorted(<list>, reverse=True)
# depending on our requirements

list = ['bike', 'car', 'aeroplane', 'ship']
print('The original list:\n', list)
print('The list sorted using the sorted(<list>) method:\n', sorted(list))
list.reverse()
print('The reverse of original list using "list.reverse()" method:\n', list)