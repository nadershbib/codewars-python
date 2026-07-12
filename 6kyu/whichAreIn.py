
# https://www.codewars.com/kata/550554fd08b86f84fe000a58/train/python

def in_array(array1, array2):
    
    finalList = []
    for word in array1:
      for w in array2:
         if word in w:
            finalList.append(word)
            break
    return sorted(set(finalList))






















