
numbers = [10, 15, 34, 56, 46] #list element starts from 0 sequence
print("Original Lists :", numbers)
numbers[0] = 555
print("New lists :", numbers) #assigning new value of 555 to first element

numbers[1] = numbers [4]
print("Copied the 4th sequence to 1st sequence :", numbers)
print("Copied number was :",numbers[4]) #accessing list content separately
print("List length :", len(numbers))#printing list's length
del numbers[0] #removing the zero sequence from the lists
print("After deleting zero sequence element of the list it becomes :", numbers)
print("After deleting the new length of the list :", len(numbers)) 
#now list has 0 to 3 sequence
#an index equal to -1, -2, -3, -4 organized from the last one in the list
numbers = [5, 53, 334, 644]
numbers = numbers[-1]
