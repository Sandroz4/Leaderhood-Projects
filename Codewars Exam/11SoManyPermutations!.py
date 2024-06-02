import itertools

def permutations(s):
    permed = itertools.permutations(s)
    unique = sorted(set([''.join(i) for i in permed]))
    return unique