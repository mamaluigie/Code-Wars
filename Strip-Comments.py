def solution(string,markers):
    # Everything after the two markers that are passed in
    # should be deleted up until there is a new line character

    #sectioning off the string
    new_string = string.split("\n")
    
    #iterating through each seciton and performing the calculation on each
    for x in range(len(new_string)):
        for marker in markers:
            #if marker is in section then find location and alter string
            if marker in new_string[x]:
                #filter through string to find char_location with the marker
                for char_location in range(len(new_string[x])):
                    # if that is the correct marker for that location 
                    # then delete everything to the right and strip the 
                    # remaining whitespace off
                    if new_string[x][char_location] == marker:
                        new_string[x] = new_string[x][:char_location]
                        new_string[x] = new_string[x].strip()
                        break
    
    #join the strings together with a newline character
    return "\n".join(new_string)


print(solution("apples, pears # and bananas\ngrapes\nbananas !apples", ["#", "!"]))
#solution("a #b\nc\nd $e f g", ["#", "$"])