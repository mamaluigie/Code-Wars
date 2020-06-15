# return masked string
def maskify(cc):
    length_of_string = len(str(cc))
    end_string = str(cc)[-4:]
    length_of_string = length_of_string - 4
    if length_of_string > 0:
        for x in range(length_of_string):
            end_string = '#' + end_string
    return end_string
    pass
