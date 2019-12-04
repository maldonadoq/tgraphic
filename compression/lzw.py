import numpy as np
import sys

# Geeks for Geek

# Encoding
def encoding(word):
    table = {}
    code = 256

    for i in range(code):
        table[chr(i)] = i

    output = []

    p = word[0]
    c = ''

    t = len(word)
    #print('{:5s}{:10s}{:4s}{:4s}'.format('Str', 'Out Code', 'Add', 'Code'))
    for i in range(t):
        if(i != (t - 1)):
            c += word[i + 1]

        if(table.get(p + c) != None):
            p += c
        else:
            #print('{:4s}{:4d}       {:4s}{:4d}'.format(p, table[p], p+c, code))
            output.append(table[p])
            table[p+c] = code
            code += 1
            p = c

        c = ''

    #print('{:4s}{:4d}\n'.format(p, table[p]))
    output.append(table[p])
    return output

# Decoding
def decoding(codes):
    table = {}
    code = 256

    for i in range(code):
        table[i] = chr(i)

    old = codes[0]
    s = table[old]

    c = s[0]
    word = s[0]

    for i in range(len(codes) - 1):
        n = codes[i+1]

        if(table.get(n) == None):
            s = table[old]
            s += c
        else:
            s = table[n]

        word += s

        c = s[0]
        table[code] = table[old] + c
        code += 1
        old = n
        
    return word

if __name__ == "__main__":

    word = 'maldonado'

    if(len(sys.argv) == 2):
        word = sys.argv[1]

    encode = encoding(word)
    decode = decoding(encode)

    snorm = len(word)
    senco = len(encode)    

    print('Encode      : ', encode)
    print('Decode      : ', decode, '\n')

    print('Normal      : ', snorm)
    print('Compression : ', senco)
    print('Rate of C.  : ', snorm/senco)
