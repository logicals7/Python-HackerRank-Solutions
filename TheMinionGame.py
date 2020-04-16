def minion_game(string):
    # your code goes here
    vowels = ['A', 'E', 'I', 'O', 'U']
    Stuart = 0
    Kevin = 0
    n = len(string)
    for i in range(0, n):
        if string[i] in vowels:
            Kevin = Kevin + n - i
        else:
            Stuart = Stuart + n - i
    if (Stuart > Kevin):
        print('Stuart', Stuart)
    elif (Stuart < Kevin):
        print('Kevin', Kevin)
    else:
        print("Draw")


