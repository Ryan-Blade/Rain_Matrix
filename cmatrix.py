import sys
import time
import random

rows, cols = 25, 120

characters = ['0', '1']

matrix = [[random.choice(characters) for _ in range(cols)] for _ in range(rows)]

while True:
    for col in range(cols):
        if random.random() > 0.9:
            matrix[0][col] = random.choice(characters)
            
    for row in range(rows - 1, 0, -1):
        matrix[row] = matrix[row - 1][:]

    sys.stdout.write('\x1b[H')
    for row in matrix:
        colored_row = ''.join(
            '\x1b[38;5;%dm%s\x1b[0m' % (16 + 36 * characters.index(char), char) for char in row
        )
        print(colored_row)

    sys.stdout.flush()
    time.sleep(0.05)
