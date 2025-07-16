import stringCalc


def calculate():
    type_of_string = stringCalc.get_type_of_string()
    kern = stringCalc.get_kern()
    length = stringCalc.get_lengthCooper()
    diam_general = stringCalc.get_general()
    if type_of_string == 1:
        cooper = round(calc.cooperDiam(diam_general, kern), 3)
        lengthCooper = int(calc.lengthCooper(kern, cooper, length))
        form.diamPrimary.setText(str(cooper))
        form.lengthPrimary.setText(str(lengthCooper))
    else:
        cooperFirst = round(calc.cooperFirst(diam_general, kern), 3)
        cooperSecond = round(calc.cooperSecond(diam_general, kern), 3)
        lengthPrimary = int(calc.lengthCooperPrimary(kern, length, cooperFirst))
        lengthSecond = int(calc.lengthCooperSecondary(kern, length, cooperFirst, cooperSecond))
        form.diamPrimary.setText(str(cooperFirst))
        form.diamSecondary.setText(str(cooperSecond))
        form.lengthPrimary.setText(str(lengthPrimary))
        form.lengthSecondary.setText(str(lengthSecond))