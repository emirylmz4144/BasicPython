from collections import defaultdict

n,m=map(int,input().split())

A=defaultdict(list)
for i in range(n):
    word=input()
    A[word].append(i)

B=[]
for i in range(m):
    word=input()
    B.append(word)

for word in B:
    if word in A:
        for location in A[word]:
            print(location+1,end=" ")
        print()
    else:
        print(-1)

print(A)
print(B)
