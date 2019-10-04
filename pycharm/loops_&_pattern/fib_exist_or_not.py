def checkMember(n):
    # Implement Your Code Here
    fib1 = 0
    fib2 = 1
    if n == 0:
        return True
    while n >= fib2:
        if n == fib2:
            return True
        fib1, fib2 = fib2, (fib1 + fib2)
    return False


n = int(input())
if (checkMember(n)):
    print("true")
else:
    print("false")