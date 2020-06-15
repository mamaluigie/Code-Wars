def encrypt_this(text):
    
    words = text.split(" ")
    
    encrypted_word = ""
    
    print(words)
    for x in range(len(words)):
        character_list = list(words[x])
        
        if len(character_list) > 1:
            second_character = character_list[1]
            last_character = character_list[-1]

        for location in range(len(list(character_list))):
            
            if location == 0:
                character_list[0] =str(ord(character_list[0]))
            elif location == 1:
                character_list[1] = last_character
            elif location == len(character_list) - 1:
                character_list[-1] = second_character

        words[x] = "".join(character_list)

    final_text = ' '.join(words)
    
    return final_text

print("A wise old owl lived in an oak : " + encrypt_this("A wise old owl lived in an oak"))
print("The more he saw the less he spoke : " + encrypt_this("The more he saw the less he spoke"))



#print(encrypt_this("The less he spoke the more he heard"))
#print(encrypt_this("Why can we all not be like that wize old bird"))
#print(encrypt_this("Thankyou Piotr for all your help"))

