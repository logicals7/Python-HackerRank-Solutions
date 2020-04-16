count = 0
a = int(input())
rolla = set(map(int,input().split()))
b = int(input())
rollb =set(map(int,input().split()))
l = list(rolla.difference(rollb))
for i in l:
    count = count+1
print(count)
# Enter your code here. Read input from STDIN. Print output to STDOUT

