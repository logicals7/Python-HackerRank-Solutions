if __name__ == '__main__':
    l = []
    marks=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        arr = [name,score]
        marks.append(score)
        l.append(arr)
    x = sorted(set(marks))[1]
    l.sort(key=lambda x: x[1])
    l.sort(key=lambda x: x[0])
    for n,s in l:
        if s==x:
            print(n)