import math
def prime(n):
    if(n==1):
        return (n,False)
    i = 2
    while (i<=math.sqrt(n)):
        if(n%i==0):
            return (n,False)
        i+=1
    return (n,True)

print(sum(map(lambda x:x,range(101))))

g = lambda x:x%2 == 0
f = lambda x,y,z : int((x+y+z)/3)
print(g(8))
print(f(1,2,3))

a = list(map(f,range(1,101),range(1,101),range(1,101)))
print(a)
