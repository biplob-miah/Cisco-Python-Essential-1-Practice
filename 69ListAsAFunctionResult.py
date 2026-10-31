def strange_list_fun(n): #n numbers parameter has been setted
    strange_list = [] #inital empty list for the result
    for i in range (0,n): #from 0 to n
        strange_list.insert(0, i) #adding i's value using insert() to the 0 position in strange list for the descending list
    return strange_list #if condition is false then stop the strange_list variable to insert
print(strange_list_fun(4)) #input 4 as n to the strange_list_function
