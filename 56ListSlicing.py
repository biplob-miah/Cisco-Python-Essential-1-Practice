#this program shows the difference between normal variable vs list variable
list_1 = [1]
list_2 = list_1 #indicates both are same list
list_1[0]= 2 #adding 2 to 0 sequence in list_1 means also adding to the list_2
print(list_2)


#powerful slicing
#we can copy using [:} to make the varibale not changable
list_1 = [1]
list_2 = list_1[:]
list_1[0]= 2
print(list_2)

#we can specifically slice the list using my_list[start:end]
#start is included but end is not like (start,end] in mathematics

my_list = [4,53,64,35,64,33,43]
new_list = my_list[3:6] # this will slice our my_list from the seq 3 to 6 but not include 6 seq
print(new_list)

#negative slicing
#negative slicing maintains the 
