# https://www.codewars.com/kata/56fe9ffbc25bf33fff000f7c/train/python

def sc(arr):
    
    toRemove = []
    freq = {}
    finalList = []
    
    for subarr in arr:
        if not subarr:
            continue
        for num in subarr:
            freq[num] = freq.get(num,0) + 1
    if freq:
        maxNum = max(list(freq.values()))

        for key in freq:
            if freq[key] == maxNum:
                 toRemove.append(key)
    
    for subarr in arr:
        tempList = []
        if not subarr:
            finalList.append(tempList)
            continue
        for num in subarr:
            if num not in toRemove:
                tempList.append(num) 
        finalList.append(tempList)
    print(finalList)    
    return finalList
         
         
