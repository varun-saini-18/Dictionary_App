import json
from difflib import get_close_matches

data=json.load(open("data.json"))

def translate(word):
    word=word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn = input("Did you mean %s ? If yes than press Y else N" % get_close_matches(word,data.keys())[0])
        if yn=="Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn=="N":
            return "The word dosn't exists. Please recheck it."
        else:
            return "We didn't understand your entry. "
    else:
        return "Word is not found. Recheck the word."
    

word=input("Enter a word: ")

output = translate(word)

if type(output)==list:
    for items in output:
        print(items)
else:
    print(output)
