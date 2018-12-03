import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def meaning(w):

    if w in data:
        return data[w]

    elif w.upper() in data:
        return data[w.upper()]

    elif w.lower() in data:
        return data[w.lower()]

    elif len(get_close_matches(w.lower(), data.keys())) > 0:
        yn = input("Do you lokking for : %s ? Enter Y if yes, or N if no : " %get_close_matches(w.lower(), data.keys())[0])
        yn = yn.lower()

        if yn == "y":
            return data[get_close_matches(w.lower(), data.keys())[0]]
        elif yn == "n":
            return "Please check your word again..."
        else:
            return "We didn't understand your entry."

    else:
        return "Sorry! This word doesn't exist. Try another word..."

word = input("Enter your word : ")

output = meaning(word)

if type(output) == list:
    for item in output:
        print(item)

else:
    print(output)
