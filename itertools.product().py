# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

if __name__ == '__main__':
    list_1 = []
    n_1 = input().split()
    list_1 = list(map(int, n_1))
    list_2 = []
    n_2 = input().split()
    list_2 = list(map(int, n_2))
    print(*product(list_1, list_2))





