n=int(input())
lst=input().split()
c=list(map(eval,lst))
b=[]
for i in range (n-1):
    a=c[i]-c[i+1]
    b.append(abs(a))
print(min(b))
