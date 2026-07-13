# https://www.codewars.com/kata/55c45be3b2079eccff00010f/train/python

def order(sentence):

    dict = {}

    for word in sentence.split():
        for c in word:
            if c.isdigit():
                dict[int(c)] = word
    return " ".join(dict[key] for key in sorted(dict))
    


print(order("is2 Thi1s T4est 3a")) 






