def print_formatted(number):
    width = len(str(bin(n))) - 2
    for num in range(1, n + 1):
        decimal = int(num)
        octal = oct(num)
        hexadecimal = hex(num)
        binary = bin(num)
        print(str(decimal).rjust(width), octal[2:].rjust(width), hexadecimal[2:].title().rjust(width),
              binary[2:].rjust(width))

