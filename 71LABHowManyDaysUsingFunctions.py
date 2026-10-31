def day_in_month(year, month, day):
    test_year = [1900, 2024,1878, 2050,1989, 2048,2038,1984, 1803]
    test_month = [2,6,9,3,7,11,12,10,5,3,8]
    test_day = [28, 30, 31, 31,31,31,30,31,30,29]
    for i in range(len(test_year)):
        year = test_year[i]
        month = test_month[i]
        print(year,month, end="")
        result =day_in_month(year, day)
print(result)
