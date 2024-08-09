triangle_char = input('Enter a character: ')
triangle_height = int(input('Enter triangle height: '))
print('')

for j in range (triangle_height):
    print((triangle_char) * (j + 1))