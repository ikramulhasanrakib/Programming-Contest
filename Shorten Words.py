n = int(input())
while n>=1:
    w = input().lower()
    n-=1
    if len(w)>10:
        print(w[0]+str(len(w)-2)+w[-1])
    else:
        print(w)