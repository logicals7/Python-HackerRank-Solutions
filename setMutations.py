sum = 0
ele = int(input())
set1 = set(input().split())
querries = int(input())
for i in range(querries):
    querry,value=input().split()
    value = int(value)
    set2=set(input().split())
    if (querry=='intersection_update'):
        set1.intersection_update(set2)
    if (querry=='update'):
        set1.update(set2)
    if  (querry=='symmetric_difference_update'):
        set1.symmetric_difference_update(set2)
    if  (querry=='difference_update'):
        set1.difference_update(set2)
for i in (set1):
    i = int(i)
    sum = sum + i
print(sum)
