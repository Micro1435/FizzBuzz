# Michael Montella

# Fizz Buzz

number = input("Enter a number: ")

for i in range(0, number + 1, 1):
    if i % 3 == 0 and i % 5 == 0:
        print "fizzbuzz"
    elif i % 3 == 0:
        print "fizz"
    elif i % 5 == 0:
        print "buzz"
    else:
        print i