from itertools import permutations
for vec in permutations(range(8)):
    if (8 == len(set(vec[i]+i for i in range(8)))== len(set(vec[i]-i for i in range(8)))):
        print(vec)