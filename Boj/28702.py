n = 0
for term in range(3, 0, -1):
    s = input()
    if s not in ["Fizz", "Buzz", "FizzBuzz"]:
        n = int(s) + term

if n % 3 == 0 and n % 5 == 0:
    print("FizzBuzz")
elif n % 3 == 0:
    print("Fizz")   
elif n % 5 == 0:
    print("Buzz")
else:
    print(n)