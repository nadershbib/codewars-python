def count_zeros(x):
   return sum( str(i).count("0")  for i in range(1,x+1))
      

print(count_zeros(10000))
