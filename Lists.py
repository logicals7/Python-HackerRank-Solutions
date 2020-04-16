if __name__ == '__main__':
    N = int(input())
    l=[]
    for i in range (N):
        command, *values=input().strip().split()
        values=list(map(int,values))
        if (command=='insert'):
            l.insert(values[0],values[1])
        if (command=='print'):
            print(l)
        if (command=='remove'):
            l.remove(values[0])
        if (command=='append'):
            l.append(values[0])
        if (command=='sort'):
            l.sort()
        if (command=='pop'):
            l.pop()
        if (command=='reverse'):
            l.reverse()

