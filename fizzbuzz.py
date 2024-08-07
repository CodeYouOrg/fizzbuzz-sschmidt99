# This should print numbers 1-100
# If %3 print Fizz instead of number
# If %5 print Buzz instead of number
# If %3, 5 print FizzBuzz

def Fizz_Buzz():
    for i in range (101):
        if i %3 == 0 and i %5 == 0:
            print("Fizz Buzz")
        elif i %3 == 0:
            print("Fizz")
        elif i %5 == 0:
            print("Buzz")
        else:
            print (i)

Fizz_Buzz()

