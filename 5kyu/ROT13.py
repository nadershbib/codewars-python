
# https://www.codewars.com/kata/52223df9e8f98c7aa7000062/train/python

def rot13(message):
    finalStr = ""
    rot13 = {
        "A":"N",
        "B":"O",
        "C":"P",
        "D":"Q",
        "E":"R",
        "F":"S",
        "G":"T",
        "H":"U",
        "I":"V",
        "J":"W",
        "K":"X",
        "L":"Y",
        "M":"Z",
    }
    # adding the rest of the letters in rot13 -> "N":"A",..... 
    for pair in list(rot13.items()):
        rot13[pair[1]] = pair[0]
    

    for c in message:
        if c.upper() in rot13:
            if c.isupper():
                finalStr+=rot13[c]
            else:
                finalStr+=rot13[c.upper()].lower()
        else:
            finalStr+=c
    return finalStr

print(rot13("EBG13 rknzcyr."))
    
        
# best solution for this problem:
            
# import string

# def rot13(message):
# 	    first = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
#    	trance = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
# 	return message.translate(string.maketrans(first, trance))  

# YOU CAN MAKE A TRANSLATION TABLE IN PYTHON using maketrans, then you .translate to transform original string to the translated table

