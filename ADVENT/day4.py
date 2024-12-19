"""I: vertical index
J: horizontal index
"""
import numpy as np

word = "XMAS"

def print_index(i, j, func):
    print(f"Found: Position {i} {j} func {func}")

def find_horizontal(i, j, store):
    total = 0
    line = store[i]
    
    """left"""
    for d in range(1, j):
        n = line[j-d]
        check = word[d]
        if n == check:
            if d == len(word)-1:
                total += 1
                print_index(i, j, "left")
                break
        else:
            break
    
    """right"""
    for d in range(1, len(line)-j):
        n = line[j+d]
        check = word[d]
        if n == check:
            if d == len(word)-1:
                total += 1
                print_index(i, j, "right")
                break
        else:
            break
    
    return total

def find_vertical(i, j, store):
    total = 0
    column = store[:,j]
    
    """up"""
    for d in range(1, i+1):
        n = column[i-d]
        check = word[d]
        if n == check:
            if d == len(word)-1:
                print_index(i, j, "up")
                total += 1
                break
        else:
            break
    
    """down"""
    for d in range(1, len(column)-i):
        n = column[i+d]
        check = word[d]
        if n == check:
            if d == len(word)-1:
                print_index(i, j, "down")
                total += 1
                break
        else:
            break
            
    return total
    

def find_diagonal(i, j, store):
    total = 0
    

    """up left"""
    for d in range(1, len(word)):
        print(f"pos: {j}")
        try:
            if i-d < 0 or j-d < 0:
                break
            n = store[i-d][j-d]
            check = word[d]
            if n == check:
                if d == len(word)-1:
                    print_index(i, j, "up left")
                    total += 1
                    break
            else:
                break
        except IndexError:
            break
        
    """up right"""
    for d in range(1, len(word)):
        try:
            if i-d < 0:
                break
            n = store[i-d][j+d]
            check = word[d]
            if n == check:
                if d == len(word)-1:
                    print_index(i, j, "up right")
                    total += 1
                    break
            else:
                break
        except IndexError:
            break
        
    """down left"""
    for d in range(1, len(word)):
        try:
            if j-d < 0:
                break
            n = store[i+d][j-d]
            check = word[d]
            if n == check:
                if d == len(word)-1:
                    print_index(i, j, "down left")
                    total += 1
                    break
            else:
                break
        except IndexError:
            break

    """down right"""
    for d in range(1, len(word)):
        try:
            n = store[i+d][j+d]
            check = word[d]
            if n == check:
                if d == len(word)-1:
                    print_index(i, j, "down right")
                    total += 1
                    break
            else:
                break
        except IndexError:
            break
        
    
    return total

def solve(file):
    total = 0
    store = [list(line.strip()) for line in file]
    store = np.array(store, dtype=object)
    
    print(len(store[:,0]))
    
    for i, row in enumerate(store):
        for j, character in enumerate(row):
            if character == word[0]:
                total += find_horizontal(i, j, store)
                total += find_vertical(i, j, store)
                total += find_diagonal(i, j, store)
    
    print(total)

def inside(row, column, H, W):
    return 0 <= row and row < H and 0 <= column and column < W

def solve2(file):
    total = 0
    store = [list(line.strip()) for line in file]
    store = np.array(store, dtype=object)
    
    height = len(store[:,0])
    width = len(store[0])
    
    for row, rowl in enumerate(store):
        for column, character in enumerate(rowl):
            if character == word[0]:
                for drow in range(-1, 2):
                    for dcolumn in range(-1, 2):
                        if drow == 0 and dcolumn == 0:
                            continue
                        ok = True
                        for i in range(0, 4):
                            r2 = row + drow*i
                            c2 = column + dcolumn*i
                            if inside(r2, c2, height, width) and store[r2][c2] == word[i]:
                                pass
                            else:
                                ok = False
                                break
                        
                        if ok:
                            total += 1
    print(total)


def solve3(file):
    directions = [[-1,-1],[-1,1],[1,1],[1,-1]]
    total = 0
    store = [list(line.strip()) for line in file]
    store = np.array(store, dtype=object)
    
    height = len(store[:,0])
    width = len(store[0])
    
    for row, rowl in enumerate(store):
        for column, character in enumerate(rowl):
            if character == "A":
                collect = ""
                for dir in directions:
                    r2 = row+dir[0]
                    c2 = column+dir[1]
                    if not inside(r2, c2, height, width):
                        continue
                    collect += store[row+dir[0]][column+dir[1]]
                
                if collect == "MMSS" or collect == "MSSM" or collect == "SSMM" or collect == "SMMS":
                    total += 1
    
    print(total)

if __name__ == "__main__":
    file_path = "input/wordsearch.txt"
    with open(file_path, "r") as f:
        solve3(f)