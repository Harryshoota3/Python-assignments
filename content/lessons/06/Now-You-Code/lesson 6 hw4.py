def char_in_text(char,text):
    num_of_char = 0
    length = len(text)
    i = 0
    while i < (length - 1):
        if text[i] == char:
            num_of_char = num_of_char + 1
        i = i + 1
    return num_of_char



character = input("Enter Character: ")
text = input("Enter text: ")
print("Th character %s appear %f times in the text" %(character, char_in_text(character,text)))
