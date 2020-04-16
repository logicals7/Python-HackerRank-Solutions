# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == '__main__':
    n = int(input())
    sum = 0
    list = []
    for i in range(0,n):
        country = input()
        if country not in list:
                list.append(country)
    for i in list:
        sum = sum + 1
    print(sum)
