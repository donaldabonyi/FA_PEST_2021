
#converts number to pflotran floating point. returns a string
def numberToPflotran(number):
    float_number = float(number)
    string_number = "{:e}".format(float_number).replace('+','')
    string_number2 = ""
    exp = False
    notzero = False
    for c in string_number:
        if not exp:
            string_number2 += c
        else:
            if c == '-':
                string_number2 += c
            if c != '0' and c != '-':
                notzero = True
            if notzero:
                string_number2 += c
        if c == 'e':
            exp = True
    if string_number2.endswith("e"):
        string_number2 += "0"
    return string_number2.replace('e','d')

#Tests
test = False
if(test):
    print(numberToPflotran(5))
    print(numberToPflotran(50))
    print(numberToPflotran(5.4))
    print(numberToPflotran(54.6))
    print(numberToPflotran(0.24))
    print(numberToPflotran(0.0054))