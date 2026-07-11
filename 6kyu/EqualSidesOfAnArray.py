

# https://www.codewars.com/kata/5679aa472b8f57fb8c000047/train/python

# first passing solution: 

# def find_even_index(arr):
#     if len(arr) ==  1:
#          return 0 
#     totalSum = sum(arr)
#     leftSum = 0
#     rightSum = totalSum - arr[0]
#     print(rightSum)
#     if leftSum == rightSum:
#         return 0

#     for i in range(1,len(arr)):
        
#         leftSum+=arr[i - 1]
#         rightSum-= arr[i]
#         print("LEFT SUM",leftSum)
#         print("RIGHT SUM",rightSum)
#         if leftSum == rightSum:
#             return i
#     return -1

# print(find_even_index([1,2,3,4,1,2,3]))       
            

# PREFIX/SUFFIX PATTERN, LEFT SUM /  RIGHT SUM, CONSTANTLY GETTING LEFT SUM AS WE MOVE FORWARD AND RIGHT SUM

# optimized solution: ( removing the redundancy of iterating from index 1) 


def find_even_index(arr):
   
    leftSum = 0
    rightSum = sum(arr)
    for i,num in enumerate(arr):
         rightSum -= num
         if leftSum ==  rightSum:
              return i
         leftSum+=num
    return -1

print(find_even_index([1,2,3,4,1,2,3]))  


# update left and move forward and you'll have the left sum starting from the new index you're at :)





