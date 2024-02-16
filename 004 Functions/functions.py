#Block of code which can reused again and again

def factorial(n):
    res=1
    for i in range(1,n+1):
        res*=i
    return res

l=factorial(5)
print(l)
