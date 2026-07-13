# https://www.codewars.com/kata/5a0efbb7c374cb69970000cf/train/python

def reverseMessage(text):
    return "".join( word .capitalize() for word in text[::-1].split())

print(reverseMessage("AaaaA"))

