num = int(input("Enter a number to check if it is prime: "))
is_prime = True

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            is_prime = False
            break

if is_prime and num > 1:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")
