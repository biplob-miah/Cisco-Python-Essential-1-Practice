#this program append beatles members in an empty list
#also for loop used for the two name
#user inputed the two name and those was added to the new list
#then removed those two member from the list and
#added another member at the 0 sequence
beatles = [ ]
beatles.append("John Leannon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print(beatles)

for new_star in ["Stu Sutcliffe", "Pete Best"]:
    new_star = input("Enter the members name :")
    beatles.append(new_star)
print("Now the beatles becomes :", beatles)
del beatles[-1]
del beatles[-1]
beatles.insert(0,"RingStarr")
print("Now the beates becomes :", beatles)
    
