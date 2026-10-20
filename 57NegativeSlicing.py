#this program shows how to slice negative indices
#if we dont't add steps in python, Python will go left to right normally
#to solve this problem we need to add steps like :-1 to go right to left
my_list = [5,634,45,43,34,56]
new_list = my_list[2:-2] #slicing my_list and creating new var from 2 to -2 but -2 seq in not included
print("Negative sliced :", new_list)

my_list = [5,634,45,43,34,56]
new_list = my_list[-2:1:-1] #adding steps to go from -2 seq to 1 but not include 1 seq
print("Right to left sliced :", new_list)

#if we don't mention end ,python will to the end of the elements and includes all
my_list = [5,634,45,43,34,56]
new_list = my_list[-2:] #we didn't mention any end not to include
print("Without mentioning end sequence :", new_list) #this includes all from -2 seq to right
#previous code goes left to right but if we want to reverse it we will add steps
my_list = [5,634,45,43,34,56]
new_list = my_list[-2: :-1] #we setting steps :-1 to right to left
print("Without mentioning end sequence with steps right to left :", new_list)

#we use del to specifically remove the elements of a lists

my_list = [5,634,45,43,34,56]
del  my_list[-2:] #this will delete -2 seq to right
print("After deleting a specific elements :", my_list)
# to check a element is in the list we use "in" operator and to check its not in we use "not in" operator
#it returns true or false
my_list = [5,634,45,43,34,56]
print(5 in my_list) #it checks is 5 in my list? Yes
print(6 in my_list) #it checks is 6 in my list? No
print(43 not in my_list) #it checks is 43 is not in my list? No
