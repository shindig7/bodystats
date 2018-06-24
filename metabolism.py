#!/usr/bin/env python3

def TDEE(bmr): 
    """Calculates an estimated Total Daily Energy Expenditure (TDEE) based on
    inputted activity level and an estimated BMR
    
    Input:
        bmr (int)
            Basal Metabolic Rate, calculated from the BMR function or an
            outside function """
    activity_dict = {'Sedentary': {'Description': 'Little or No Exercise, Moderate Walking, Desk Job', 'Modifier': 1.2}, 'Slightly Active': {'Description': 'Exercise or Light Sports 1 to 3 Days a Week, Light Jogging or Walking 3 to 4 Days a Week', 'Modifier': 1.375}, 'Lightly Active': {'Description': 'Exercise or Moderate Sports 2 to 3 Days a Week, Light Jogging or Walking 5 to 7 Days a Week', 'Modifier': 1.425}, 'Moderately Active': {'Description': 'Physical Work, Exercise, or Sports 4 to 5 Days a Week, Construction Laborer', 'Modifier': 1.55},  'Very Active': {'Description': 'Heavy Physical Work, Exercise, or Sports 6 to 7 Days a Week, Hard Laborer', 'Modifier': 1.75}, 'Extremely Active': {'Description': 'Very Heavy Physical Work or Exercise Every Day, Professional/Olympic Athlete', 'Modifier': 1.9}                      }

    for i, L in enumerate(sorted(activity_dict, key=lambda k:
        activity_dict[k]['Modifier'])):
        print("{}. {}: {}".format(str(i+1), L, activity_dict[L]['Description']))

    level = int(input('Please select an activity level: ')) - 1
    selected_level = activity_dict[sorted(activity_dict, key=lambda k:
        activity_dict[k]['Modifier'])[level]]

    activity_modifier = selected_level['Modifier']

    tdee = bmr * activity_modifier

    print('BMR: {}\nTDEE: {}'.format(bmr, tdee))


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

def main():
    #bmr = BMR(21, 74, 272, 'M')
    #print(bmr)
    TDEE(2145)


if __name__ == "__main__":
    main()
