import string
text = input("enter text")
for char in string.punctuation:
    text = text.replace(char, "")

words = text.title().split()

hashtag = "#" + "".join(words)
if len(hashtag) > 140:
    hashtag = hashtag[:140]
print(hashtag)