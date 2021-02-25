def fib_getNext(i, n):
    for k in range(n):
        i = i + i

    return i

def Dfactorial(n):
    fact = 1
    for i in range(1,n+1): 
        fact = fact * i 
    return fact

if __name__ == "__main__":
    fib_getNext()