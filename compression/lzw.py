import numpy as np
import sys

def encoding(word):
    table = {}

    code = 256
    for i in range(code):
        table[chr(i)] = i

    output = []

    p = word[0]
    c = ''

    t = len(word)
    print('{:5s}{:10s}{:4s}{:4s}'.format('Str', 'Out Code', 'Add', 'Code'))
    for i in range(t):
        if(i != (t - 1)):
            c += word[i + 1]

        if(table.get(p + c) != None):
            p += c
        else:
            print('{:4s}{:4d}       {:4s}{:4d}'.format(p, table[p], p+c, code))
            output.append(table[p])
            table[p+c] = code
            code += 1
            p = c

        c = ''

    print('{:4s}{:4d}\n'.format(p, table[p]))
    output.append(table[p])
    return output

if __name__ == "__main__":

    #word = 'maldonado'
    word = 'ABRACADABRA'

    if(len(sys.argv) == 2):
        word = sys.argv[1]

    out = encoding(word)
    print('codes: ', out)