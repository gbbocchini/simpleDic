import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def sinonimo(word):
    
    word = word.lower()
    
    if word in data:     
        return data[word]    
    elif len(get_close_matches(word, data.keys(), cutoff = 0.8)) > 0:
         YN = input("Did you mean %s? Enter Y or N: \n" % get_close_matches(word, data.keys())[0])
         if YN == "Y":
             return data[get_close_matches(word, data.keys())[0]]
         elif YN == "N":
            return "Does this word exist?"   
         else:
            return "Wut? Let's try again, shall we?"
    else:        
        return "Somenthing wrong is not right! Try again (if you want, of course...)"


while True:
    palavra = input("Please insert a word in English: ")

    funcoutput = sinonimo(palavra)

    if type(funcoutput) == list:
        for item in funcoutput:
            print(item)
    else:
        print(funcoutput)


