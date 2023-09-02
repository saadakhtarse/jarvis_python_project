# import modules
import json
from difflib import get_close_matches
import os

# load the data of json file
# (here file name is dict.json)
file = os.path.abspath("C:\JARVIS\Data\Contacts\dict.json")

data=json.load(open(file))

# create a function to get the the meaning
def Get_meaning(word):
    if word in data:
        # as data will be in the form of dictionary
        # and this condition is to check if the 
        # meaning of the words are more than one 
        # and the value of each key is in the form of list
        if len(data[word])>1:
            # print each meaning
            for i in data[word]:
                print(i)
                return i
        # else will print the only element in the list
        else:
            print(data[word][0])
            return (data[word][0])
    # we will check the input in all forms
    elif word.lower() in data:
        if len(data[word.lower()])>1:
            # print each meaning
            for i in data[word.lower()]:
                print(i)
                return (i)
        # else will print the only element in the list
        else:
            print(data[word.lower()][0])
            return (data[word.lower()][0])
    elif word.upper() in data:
        if len(data[word.upper()])>1:
            # print each meaning
            for i in data[word.upper()]:
                print(i)
                return(i)
        # else will print the only element in the list
        else:
            print(data[word.upper()][0])
            return(data[word.upper()][0])
    elif word.title() in data:
        if len(data[word.title()])>1:
            # print each meaning
            for i in data[word.title()]:
                print(i)
                return(i)
        # else will print the only element in the list
        else:
            print(data[word.title()][0])
            return(data[word.title()][0])
    # now if these three doesnt match with the input
    # then we will find the closest match
    else:
        # get close match will return us the list of all
        # close words with the input
        close_match=get_close_matches(word,data.keys())
        # if there are 1 or more elements
        if len(close_match)>0:
            # now we will print the meaning of closest words
            # that is the first element
            print("Could not find the exact word but here is the meaning of closest words ")
            if True:
                # print the meaning of the closest word
                print(f"The closest word to this is {close_match[0]}")
                return (f"The closest word to this is {close_match[0]}")
                for i in data[close_match[0]]:
                    print(i)

            else:
                print("There is no word related to it")
                return ("There is no word related to it")
        else:
            print("Cant Found this word")
            return ("Cant Found this word")


# word=input("Enter the word: ")
# Get_meaning('word')
