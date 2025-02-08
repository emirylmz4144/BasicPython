from collections import defaultdict #DefaultDict yapısı import edildi

n,m=map(int,input().split()) # n ve m değerleri ard arda girileceğinden split edildi

A=defaultdict(list)#içi liste olacak defaultDict oluşturuldu

#Liste elemanının (harfin) hangi yerlerde oldukları value değerine ekleniyor
for i in range(n):
    word=input()
    A[word].append(i)

B=[]
for i in range(m):
    word=input()
    B.append(word)

for word in B:# B içindeki her harfin
    if word in A:#A içinde key olarak tutulan her harfin içinde
        for location in A[word]:#value olarak nerelerde tutulduğunu gösteren liste
            print(location+1,end=" ")#yazılıyor
        print()
    else:
        print(-1)#B deki eleman A da yoksa -1 yazılıyor

print(A)
print(B)
