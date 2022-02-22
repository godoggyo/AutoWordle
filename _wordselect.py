import fileinput as fi
from queue import Empty
import random

### Word list arrays TODO: Add weights for auto solvers ###
### Maybe make am ore complex list using native unix dic ###

word_list = []

def establishWordPool():
    if word_list is not Empty:
        f = fi.input(files="files/dict.txt")
        
        for line in f:
            line = line.strip("\n")
            word_list.append(line)
                
        f.close()


def selectWord():
    return random.choice(word_list) 