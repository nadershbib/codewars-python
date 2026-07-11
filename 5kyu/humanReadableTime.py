# https://www.codewars.com/kata/52685f7382004e774f0001f7/train/python




def make_readable(seconds):
   hours = seconds // 3600 
   hoursRemainder = seconds % 3600 
   minutes = hoursRemainder // 60
   seconds = hoursRemainder % 60
   return str(hours).rjust(2,"0")+":"+ str(minutes).rjust(2,"0")+":"+str(seconds).rjust(2,"0")


print(make_readable(7338))














