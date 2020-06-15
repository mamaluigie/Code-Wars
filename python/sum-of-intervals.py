def sum_of_intervals(intervals):
    dictionary = {}
    
    final_value = 0
    
    for list in intervals:
        for x in range(list[0], list[1]):
            if x in dictionary:
                dictionary[x] += 1
            else:
                dictionary[x] = 1
    
    for location in dictionary:
        final_value += dictionary[location] 
    
    return final_value

print(sum_of_intervals([(1, 5)]))
