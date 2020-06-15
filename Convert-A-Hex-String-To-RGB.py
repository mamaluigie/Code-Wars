import string

def hex_string_to_RGB(hex_string):
    # your code here
    string_list = []
    dictionary = {'r': 0, 'g': 0, 'b': 0}
    for begin, end in zip(range(1, len(hex_string), 2), range(3, len(hex_string) + 1, 2)):
        string_list.append(hex_string[begin:end].lower())
    
    for x, entry in zip(string_list, dictionary):
        dictionary[entry] = int(x, 16)
        
    return dictionary

print(hex_string_to_RGB("#FF9933"))
