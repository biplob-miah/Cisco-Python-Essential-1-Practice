
#this program works with collatz's hypothesis

cO = int(input("Enter any positive non-zero number: "))
steps = 0


while cO != 1:
     if cO % 2 == 0:
        cO = cO//2    
     else:
          cO=3*cO+1
     print(cO)
     steps +=1
        
print("\nSteps:", steps)
