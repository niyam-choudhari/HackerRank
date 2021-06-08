n,m =map(int,input().split())

def p():
    print(".|.", end="")
c=1
d=1
for i in range(int(n/2)):
    for j in range(int((n*3-(d*3))/2)):
        print("-", end="")
    for q in range(d):
        p()
    for j in range(int((n*3-(d*3))/2)):
        print("-",end="")
    c += 1
    d+=2
    print("")
for j in range(int((m-7)/2)):
    print("-", end="")
print("WELCOME", end="")
for j in range(int((m-7)/2)):
    print("-", end="")
print("")
c-=1
d-=2
for i in range(int(n/2)):
    for j in range(int((n*3-(d*3))/2)):
        print("-", end="")
    for q in range(d):
        p()
    for j in range(int((n*3-(d*3))/2)):
        print("-",end="")
    c -= 1
    d-=2
    print("")