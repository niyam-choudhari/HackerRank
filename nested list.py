n=int(input())
temp=[]
for _ in range(n):
    name = input()
    temp.append([])
    temp[_].append(name)
    score = float(input())
    temp[_].append(score)
print(temp)

for i in range(n):
    for j in range(n-1):
        if temp[j][1]>temp[j+1][1]:
            t=temp[j]
            temp[j]=temp[j+1]
            temp[j+1]=t

print(temp)

q=0
while True:
    if temp[q][1] != temp[q+1][1]:
        tt=temp[q+1][1]
        break
    else:
        q+=1
ans=[]
for i in range(n):
    if temp[i][1]==tt:
        ans.append(temp[i][0])


for a in ans:
    print(a)