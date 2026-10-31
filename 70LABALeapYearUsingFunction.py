def leap_year_test(year):
        if year % 400 == 0:
            return True
        elif year % 100 == 0:
            return False
        elif year % 4 == 0:
            return True
        else:
            return False


#now we will use list and for loop to check from a predefined list
test_data = [2024, 1999, 2016, 2020, 1995, 2000, 1900]
test_result = []
for year in test_data:
    result = leap_year_test(year)
    test_result.append(result)
print(test_result)
    
