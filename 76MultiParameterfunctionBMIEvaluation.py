#this program evaluates bmi using multi parameter and arg
def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
       weight < 20 or weight > 200:
        return None #using \ we can deal with long lines of code
    return weight / height ** 2
print(bmi(352.5, 1.65))


#we can convert lb to kg
def lb_to_kg(lb):
    return lb * 0.45359237
print(lb_to_kg(1))

#we can convert ft to m
def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254
print(ft_and_inch_to_m(6,0))

#so the whole code would be
#this program answer what is the bmi of a person 5'7'' tall and weighing 176lbs

def lb_to_kg(lb):
    return lb * 0.45359237


def ft_and_inch_to_m(ft, inch):
    return ft * 0.3048 + inch * 0.0254


def bmi(weight, height):
    if height < 1.0 or height > 2.5 or \
       weight < 20 or weight > 200:
        return None #using \ we can deal with long lines of code
    return weight / height ** 2
print(bmi(weight= lb_to_kg(176), height = ft_and_inch_to_m(5,7)))
