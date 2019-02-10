# Greater than Function
def greater(s1, s2):
    return float(s1) > float(s2)

# Less than Function
def lesser(s1, s2):
    return float(s1) < float(s2)

# Equal to  Function
def equal(s1, s2):
    if (s1 is "0" and s2 is "-0") or (s1 is "0.0" and s2 is "-0.0"):
        return True
    else:
        return float(s1) == float(s2)

try:
        s1 = input('Enter the 1st STRING Number format X.X\n')
        s2 = input('Enter the 2nd STRING Number format X.X\n')
        print("Is the 1st String Greater than the 2nd: "+ str(greater(s1,s2)))
        print("Is the 1st String Smaller than the 2nd: "+ str(lesser(s1,s2)))
        print("Is the 1st String Equal to the 2nd: "+ str(equal(s1,s2)))

except ValueError:
    print('\n')
    print('Wrong format of String\n''Only Numbers are accepted.')