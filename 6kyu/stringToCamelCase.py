# https://www.codewars.com/kata/517abf86da9663f1d2000003/train/python


def to_camel_case(text):
 finalList = []
 text = text.replace("_","-")
 words = text.split("-")
 for i,word in enumerate(words):
   if i == 0:
     finalList.append(word)
   else:
     finalList.append(word.capitalize())

 return "".join(finalList)
    



    