"""
Write a function that takes in a string of one or more words,
and returns the same string,
but with all five or more letter words reversed
(Just like the name of this Kata).
Strings passed in will consist of only letters and spaces.
Spaces will be included only when more than one word is present.

Examples:
spinWords( "Hey fellow warriors" ) => returns "Hey wollef sroirraw"
spinWords( "This is a test") => returns "This is a test"
spinWords( "This is another test" )=> returns "This is rehtona test"
"""


def spinWords(sentence):
    result = [i[::-1] if len(i) >= 5 else i for i in sentence.split() ]
    # for i in sentence.split():
    #     if len(i)>=5:
    #         i= i[::-1]
    #     result.append(i)
    # joined = " ".join(result)
    return " ".join(result)


test = "Hey fellow warriors"
print(spinWords(test))
