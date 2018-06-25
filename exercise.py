#!/usr/bin/env python3
""" Calculations regarding exercise """

def OneRepMax(weight, reps):
    """ Estimated 1-Rep Max, based on weight and number of reps """
    return round(weight + ((weight * reps) * .033333), 0)


def XRepMax(weight, current_reps, X_reps):
    """ Estimated weight for X number of reps """
    orm = OneRepMax(weight, current_reps)
    w = orm / (0.03333 * (30 + X_reps))
    return round(w, 0)

def main():
    print(OneRepMax(98, 5))
    #print(XRepMax(98, 5, 8))
    
if __name__ == "__main__":
    main()
