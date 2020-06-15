def capital(capitals): 
    # your code here
    sentences = []
    
    for capital in capitals:
        sentence = ""
        for x in capital:
            if x == "state" or x == "country":
                sentence = "The capital of " + capital.get(x)
            else:
                sentence += " is " + capital.get(x)
        sentences.append(sentence)
    return sentences

def main():
    print(capital([{'state': 'Maine', 'capital': 'Augusta'}]))

main()
