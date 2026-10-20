#this program checks the bet hits
drawn = [4,32,3,4343,5334,33,56,7]
bets = [3,56,4,11,89,5334,32]
hits= 0
for matched in bets:
    if matched in drawn:
        hits +=1
print("The total hits is :",hits)
    
