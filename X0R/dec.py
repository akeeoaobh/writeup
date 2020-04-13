import string
from string import ascii_letters
from itertools import cycle

def xor(msg, key):
    o = ''
    for i in range(len(msg)):
        o += chr(ord(msg[i]) ^ ord(key[i % len(key)]))
    return o

with open('flag.enc', 'r') as f:
    msg = ''.join(f.readlines())
with open("flag.txt", "w+") as fileClear:
    fileClear.write("\n")
# Phase 1 - Find part of key
part_of_msg = 'hexCTF{'

for i in range(len(msg)):
    candidate = xor(msg[i:i+len(part_of_msg)], part_of_msg)
    if candidate.isalnum():
        #print(candidate)
        theKey = 'JtmZzCJ'
        for j in range(len(ascii_letters)):
            key_temp1 = theKey+ascii_letters[j]
            if key_temp1 == 'JtmZzCJG' or key_temp1 == 'JtmZzCJt' or key_temp1 == 'JtmZzCJc':
                continue
            for k in range(len(ascii_letters)):
                key_temp2 = key_temp1+ascii_letters[k]
                key_gen = cycle(key_temp2)
                if ascii_letters[k] == 'm' or ascii_letters[k] == 'Y' or ascii_letters[k] == 'S' or ascii_letters[k] == 'O':
                    continue
                data = []
                for i in range(len(msg)):
                    data.append(chr(ord(msg[i]) ^ ord(next(key_gen))))
                if '}' in data:
                    if not ',' in data:
                        if not '\\' in data:
                            if not '\x7f' in data:
                                if not '@' in data:
                                    if not '|' in data:
                                        if not '~' in data:
                                            if not '`' in data:
                                                if not '[' in data:
                                                    if not '^' in data:
                                                        if not ']' in data:

                                                                print(key_temp2)
                                                                print(data)
                                                                with open("flag.txt", "a") as file:
                                                                #    file.seek(0)
                                                                #    data = file.read(100)
                                                                #    if len(data) > 0 :
                                                                    file.write("\n")
                                                                    file.write(''.join(data))
