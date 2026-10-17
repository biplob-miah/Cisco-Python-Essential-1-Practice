
hour = int(input("Enter the starting time hour :"))
mins = int(input("Enter the starting time minutes :"))
dura= int(input("Enter the event duration in minutes :"))              
mins =mins + dura
hour=hour + mins //60 #find hours hidden in minutes and update hour
mins = mins %60 #correct minutes not to excede 59
hour = hour % 24 #correct hours not to exede 23
print(hour, ":" ,mins, sep="")
