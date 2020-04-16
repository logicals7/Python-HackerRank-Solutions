if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for i in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    querry_name = input()
    for i in student_marks:
        if (querry_name==i):
            a,b,c = student_marks[i]
            z=a+b+c
            z=z/3
    print ('%.2f'%z)



