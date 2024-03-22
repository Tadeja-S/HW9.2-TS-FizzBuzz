# HW9.2-TS-FizzBuzz

print("Welcome to FizzBuzz!")
guess = int(input("Select a number between 1 and 100: "))

x = range(1, guess + 1, 1)

for num in x:
    if num % 3 == 0:
        print("fizz")
    elif num % 5 == 0:
        print("buzz")
    elif num % 3 == 0 and num % 5 == 0:
        print("fizzbuzz")
    else:
        print(num)