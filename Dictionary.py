import json
import difflib #spelling checker
from difflib import get_close_matches
data = json.load(open("JSON.json"))
#print(type(data))
#print(data["water"])

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word,data.keys()))>0:
        yn=input("Did you mean %s instead ? Enter Y if yes ,or N if no" % get_close_matches(word,data.keys())[0])
        if yn == "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif yn== "N":
            return "The Word does not exist. Please double check it."
        else:
            return("we did not understand your query.")
    
    else:
        return "The Word does not exist. Please double check it."
word = input("Enter a word: ")
#Saving the output 
output= translate(word)
#printing the response
if isinstance(output,list):
    for i in output:
        print(i)
else:
    print(output)