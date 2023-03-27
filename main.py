# TASK: Update both functions to reverse the letters in the name and provide the square root of the users age.
import math

def reverseName(me):
  result = me[::-1]
  return result

def rootAge(im):
  result = math.sqrt(im)
  return result
  
me = input("What is your name? ")
im = int(input("What is your age? "))

print("Your name in reverse is: ",reverseName(me))
print("The square root of your age is: ",rootAge(im))
