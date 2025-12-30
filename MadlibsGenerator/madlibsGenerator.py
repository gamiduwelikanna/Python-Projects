with open("text.txt", "r") as f:
    text= f.read()

words = []
start_of_word = -1

taregt_start = "<"
target_end = ">"

for i , char in enumerate(text):
    if char == taregt_start:
        start_word= i

    if char == target_end and start_word!= -1:
        word = text[start_word:i+1]
        words.add(word)
        start_word = -1