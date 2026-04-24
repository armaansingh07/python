terms = int(input("How many terms of the Fibonacci sequence do you want? "))
n1, n2 = 0, 1

print("Fibonacci sequence:")
for _ in range(terms):
    print(n1)
    next_num = n1 + n2
    n1 = n2
    n2 = next_num
