def back(n, numerals):
    finished_string = ''
    num_string = str(n).split('.')
    num_string = num_string[1]
    
    for x in num_string:
        finished_string += numerals[int(x)]

    return finished_string

def front(n, numerals):
    finished_string = '' 
    string_list = []
    num_string = str(n).split('.')
    num_string = num_string[0]

    if n < 20 and n > -20:
            #adds the chinese negative character to the final string if it is negative
            if int(num_string) < 0:
                finished_string += numerals['-']
                num_string = str(int(num_string) * -1)
            
            #gets the correct format if it is less than 20 and greater than -20
            if len(num_string) < 2:
                return finished_string + numerals[int(num_string[0])]
            elif num_string == '10':
                return finished_string + numerals[10]
            else:
                return finished_string + numerals[10] + numerals[int(num_string[1])]
            
    else:
        
        # if the string is negative
        if int(num_string) < 0:
            finished_string += numerals['-']
            num_string = str(int(num_string) * -1)
        
        #inserting all of the numbers into the format of being ones, tens, thousands, etc...
        for x in range(len(num_string)):                
            if num_string[x] != '0':
                string_list.append(num_string[x] + str((len(num_string)  - 1 - x) * '0'))
        
        for y in range(len(string_list)):
            if '0' in string_list[y]:
                finished_string += numerals[int(string_list[y][0])]
                finished_string += numerals[int('1' + string_list[y][1:])]
                if int(y) < len(string_list) - 1:
                    if len(string_list[y]) - len(string_list[y + 1]) > 1:
                        finished_string += numerals[0]
            else:
                finished_string += numerals[int(string_list[y])]
        return finished_string

def to_chinese_numeral(n):
    numerals = {
        "-":"负",
        ".":"点",
        0:"零",
        1:"一",
        2:"二",
        3:"三",
        4:"四",
        5:"五",
        6:"六",
        7:"七",
        8:"八",
        9:"九",
        10:"十",
        100:"百",
        1000:"千",
        10000:"万"
    }

    #if the number is not a decimal
    if '.' not in str(n):
        
        return front(n, numerals)

    #above is finished but the portion wiht the decimals still has to be finished...
    else:

        return front(n, numerals) + numerals['.'] + back(n, numerals)

print(to_chinese_numeral(-10.000001))
