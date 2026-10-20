#this program replace numbers from a list with user inputted numbers and prints length
numbers = [1,2,3,4,5] #number bucket
new_number = int(input("Enter any number to replace with the middle number :")) #getting user input
numbers[2] = new_number #assigning the new number to the 2 sequence of the bucket
print("Here is the replaced number :",numbers) #printing replaced numbers
del numbers[4]#removing the sequence 4 from the bucket
print("After removing the last numbers from the new number the list becomes :", numbers)
print("The final length of the numbers is :", len(numbers)) #counting the length of rest numbers
