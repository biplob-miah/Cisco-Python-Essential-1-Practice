#this program removes repeated numbers in a list and print only once at a time
my_list = [1,2,44,55,44,55,77,9966,99,77,34,23]
unique_list = []
for unique in my_list:
    if unique not in unique_list:
        unique_list.append(unique)

print("The list with unique elements only is :", unique_list)
