n = int(input())
k = int(input())
while k:
    if n%10==0:
        n=n/10
        k-=1
    else:
        n=n-1
        k-=1
print(int(n))

