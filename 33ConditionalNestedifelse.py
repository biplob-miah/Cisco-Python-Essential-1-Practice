'''this  theory program checks: If the weather is fine, we'll go for a walk.
If we find anice restaurant, we'll have lunch there. Otherwise,
we'll eat a sandwich.
If the wather is poor, we'll go to the theater.
If there are no tickets, we'll go shopping in the nearest mall.

'''

if fine_weather:
    go_for_walk()
    if find_nice_restaurant():
        have_lunch()
    else:
        eat sandwich()
else:
    if tickets_available()
        go_theater()
        else:
            go_for_shopping()
