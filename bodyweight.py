#!/usr/bin/env python

def BMI_category(bmi):
    if bmi < 18.5:
        return 'Underweight'
    elif bmi < 25:
        return 'Healthy'
    elif bmi < 30:
        return 'Overweight'
    else:
        return 'Obese'


def BMI(weight, height, units='imperial', precision=1, return_cat=False):
    if units == 'imperial':
        modifier = 703
    else:
        modifier = 1

    bmi = (float(weight) / (float(height) ** 2)) * modifier
    if return_cat:
        return round(bmi, precision), bmi_category(bmi)
    else:
        return round(bmi, precision)


def main():
    print(BMI(272, 74, return_cat=True)) 



if __name__ == '__main__':
    main()
