'''
Now You Code 3: Sentiment 2.0

Let's improve on our basic sentiment analyzer in Python.

Copy the code from 1.0 most of it will be the same.

We will improve on this program by writing a user-defined
function load_words() to load the positve or negative words from a file.

For example, instead of:

pos = "happy glad joy"

we do this:

pos = load_words("NYC3-pos.txt")

We can now make the program "smarter" simply by adding positive and
negative words to the text files!


'''

# TODO: Write Todo list then beneath write your code

# Write code here
def sentiment(postive_text,negative_text, input_text):
    pos_text = postive_text.split()
    neg_text = negative_text.split()
    in_text = input_text.split()
    score = 0
    for x in in_text:
        for y in pos_text:
            if x == y:
                score = score + 1
    for i in in_text:
        for j in neg_text:
            if i == j:
                score = score - 1
    return score;


def load_words(fileName):
    file = open(fileName, 'r')
    FileText = file.read()
    return FileText

print("Sentiment Analyzer 2.0")
pos = load_words("NYC3-pos.txt")
neg = load_words("NYC3-neg.txt")

text = input("enter text: ")
while (text != "quit"):
   score = sentiment(pos, neg, text)
   if score == 0:
        print ("%0 neutral")
   elif score > 0:
        print ("%i postive" %(score))
   else:
        print("%i negative" %score)
   text = input("enter text:")




