import math
from collections import defaultdict

def gi(theNumber):
    if theNumber <= 999999999999997:
        return int(math.log10(theNumber)) + 1
    else:
        return len(str(theNumber))

def solve_map(iters):
    _stone = "2701 64945 0 9959979 93 781524 620 1"
    _stone = list(map(int, _stone.split(" ")))
    stone = defaultdict(int)
    for s in _stone:
        stone[s] = 1
    for q in range(iters):
        new_stone = defaultdict(int)
        for num, v in stone.items():
            if num == 0:
                new_stone[1] += v
                continue
            dig = gi(num)
            if (dig % 2) == 0:
                j = pow(10, int(dig/2))
                new_stone[num//j] += v
                new_stone[num%j] += v
            else:
                new_stone[num*2024] += v
        stone = new_stone

        print(q)
    total = 0
    for s in stone.values():
        total += s
    print(total)
    
if __name__ == "__main__":
    solve_map(75)