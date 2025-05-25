
# make dictionary of keys of hindi word and haaving value in english

words = {
    "madad": "Help",
    "kursi": "Chair",
    "billi": "cat"
}

word = input("Enter the word: ")

print(words.get(word)) # this will return None if the word is not present in the dictionary
print(words[word]) # this will give error if the word is not present in the dictionary