def factorial(n):
    if n == 1 :
        return 1
    return n * factorial(n - 1)


table={}
def fibonacci(n):
    if n==1 or n==2:
        return 1
    if n not in table:
        table[n]= fibonacci(n-1)+fibonacci(n-2)
        return table[n]
    return table[n]

