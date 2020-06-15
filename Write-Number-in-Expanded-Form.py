def expanded_form(num):
    final_string = []
    num_string = str(num)
    for x in range(len(num_string)):
        if num_string[x] != '0':
            final_string.append(str(int(num_string[x])) + str((len(num_string)  - 1 - x) * '0'))
    return ' + '.join(final_string)

print(expanded_form(120))

#this is a test...

# i am altering...
# the code on the thing back at home
