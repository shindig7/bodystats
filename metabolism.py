#!/usr/bin/env python3

def BMR(age, height, weight, gender, units='imperial'):
    if units == 'imperial':
        height = height * 2.54
        weight = weight / 2.2

    if gender == 'male':
        coeff = 5
    else:
        coeff = -161

    bmr = 10*weight + 6.25*height - 5*age + coeff
    bmr = int(bmr)

    return bmr


if __name__ == "__main__":
    bmr = BMR(21, 74, 272, 'M')
    print(bmr)
