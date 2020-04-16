# Enter your code here. Read input from STDIN. Print output to STDOUT

from itertools import combinations_with_replacement
word, n = input().split()
for el in combinations_with_replacement(sorted(word),int(n)):
    print(*el, sep='')
