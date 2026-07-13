# https://www.codewars.com/kata/54da5a58ea159efa38000836/train/python

# def find_it(seq):
#     freq = {}
#     for num in seq:
#         freq[num] = freq.get(num,0) + 1
#     for num in freq:
#         if freq[num] % 2 != 0:
#             return num 


# print(find_it([1,1,1,1,3]))

def find_it(seq):
    return [ val for val in seq if seq.count(val) % 2 != 0][0]
    

