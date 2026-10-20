marks = [

    [80, 39,34],
    [83, 38, 59],
    [88, 33, 66]

    ]
print(marks[1][2]) #to find a specific number from 2d list, [row1][coulmn1] as the seqence row 1 and colum 1 is 59
marks[2][1] = 85 #changing value in 2d lists
print(marks)
for row in marks: #using for loop in 2d lists
    print(row)
