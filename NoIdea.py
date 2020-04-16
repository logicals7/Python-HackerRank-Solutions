happiness = 0
n,m = input().split()
n = int(n)
m = int(m)
n = int(n)
m = int(m)
array = list(map(int,input().split()))
set1 = set(map(int,input().split()))
set2 = set(map(int,input().split()))
for i in array:
    if i in set1:
        happiness +=1
    elif i in set2:
        happiness -=1
    else:
        happiness = happiness
print(happiness)
