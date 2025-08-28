import itertools

if __name__ == '__main__':
    letters = ['B', 'O', 'B', 'A']
    perms = set(itertools.permutations(letters))
    for p in perms:
        print(''.join(p))