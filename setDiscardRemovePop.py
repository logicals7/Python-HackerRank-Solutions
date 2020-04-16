if __name__ == '__main__':
    n = input()
    s = set(map(int,input().split()))
    a = int(input())
    for i in range(0,a):
        querry,*values = input().split()
        values = list(map(int,values))
        if (querry == 'pop'):
            s.pop()
        elif (querry == 'remove'):
            s.remove(values[0])
        elif (querry == 'discard'):
            s.discard(values[0])
    set = list(s)
    print(sum(set))
