
import string
def print_rangoli(size):
    # your code goes here
    s = string.ascii_lowercase
    list = []
    for i in range(0,size):
        line = "-".join(s[i:n])
        reverse = (line[::-1]+line[1:]).center((n*4)-3,'-')
        list.append(reverse)
    print('\n'.join(list[:0:-1]+list))

