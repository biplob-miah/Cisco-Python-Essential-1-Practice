#tax calculator using if else
income= float(input("Enter the income to calculate the TAX: "))
tax_relief = 556.02

if income <= 85528:
    tax = (income*18/100)- tax_relief
    
else:
    tax = (14839.02 + 32/100)*(income - 85528)

if tax < 0.0:
    tax = 0.0

tax=float(round(tax, 0))
print("The tax is:",tax, "thalers")

