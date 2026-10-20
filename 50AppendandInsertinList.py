#this program shows how toadd elements in a list
#using append() and insert() function as a method of the list
#function takes an argument and prints it's result
#we can use result = data.method(arg)

numbers = [5, 6, 3, 94]
print("Numbers we have :", numbers)
numbers.append(56) #using append() and adding 56 to last of the lists
print("After using append function the numbers are :", numbers)
numbers.insert(0,233) #using smart insert function and adding in 0 sequence the 233 to the lists
print("After using insert function the numbers are :", numbers)
