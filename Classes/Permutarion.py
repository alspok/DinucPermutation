from itertools import permutations
from Classes.InitVar import InitVar as iv

class Permutation():
    
    def permutations(array):
        if len(iv.dinucList) == 1:
            yield array
        else:
            for i in range(len(array)):
                perms = permutations(array[:i] + array[i+1:])
                for p in perms:
                    yield [array[i], *p]
