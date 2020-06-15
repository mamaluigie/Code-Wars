def move_zeros(array):
    #your code here
   

    print(array)
    print('\n\n')

    final_array = array 
    length_array = []

    counter = 0
    

    for x in range(len(array)):
        if isinstance(array[x], int) or isinstance(array[x], float):    
            if str(array[x]) == '0' or str(array[x]) == '0.0':
                    length_array.append(x)


    for length in length_array:
        print("length \n" + str(length))
        print("Final_array \n" + str(final_array) + "\n\nPOP\n\n")

        final_array.pop(length - counter)
        counter += 1

        print(final_array)

    for x in range(len(length_array)):
        final_array.append(0)

    
    return final_array

def main():
    print(move_zeros([1,2,0,1,0,1,0,3,0,1]))

main()

