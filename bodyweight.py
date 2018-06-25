#!/usr/bin/env python

def FFMI(weight, height, bf, units='imperial'):
    """
    Fat-Free Mass Index
    Source: https://imgur.com/a/1ZviT or
    https://journals.lww.com/cjsportsmed/Abstract/1995/10000/Fat_Free_Mass_Index_in_Users_and_Nonusers_of.3.aspx
    """
    if units == 'imperial':
        weight = weight / 2.2
        height = height * .0254  # height in meters
    elif units == 'metric':
        height = height * .01 # height in meters
    else:
        raise ValueError("Invalid unit type: please choose either 'imperial' or 'metric'")
    
    lean_mass = weight * (1.0 - (bf / 100))
    ffmi = lean_mass / height**2
    adj_ffmi = ffmi + (6.1 * (1.8 - height))
    return round(adj_ffmi, 2)
    


def LBM(weight, height, gender, units='imperial'):
    """
    https://www.calculator.net/lean-body-mass-calculator.html?ctype=standard&cage=21&csex=m&cheightfeet=6&cheightinch=2&cpound=272&cheightmeter=180&ckg=60&x=114&y=19
    """
    if units == 'imperial':
        weight = weight / 2.2
        height = height * 2.54

    if gender.upper() == 'M':
        lbm = 0.407*weight + 0.267*height - 19.2
    else:
        lbm = 1.07*weight + 0.473*height - 48.3

    if units == 'imperial':
        lbm = round(lbm*2.2, 1)
    else:
        lbm = round(lbm, 1)

    return lbm


def bodyfat(weight, height, gender, units='imperial'):
    lbm = LBM(weight, height, gender, units)
    bf = round(((weight - lbm) * 100) / weight, 2)
    return bf    


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
    ffmi = FFMI(270.8, 74, 32.8)
    print(ffmi)


if __name__ == '__main__':
    main()
