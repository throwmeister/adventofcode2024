import numpy as np

def reigonrec(i, j, cha, reigon, visited, garden):
    if visited[i,j]:
       return
    visited[i,j] = 1
    reigon.append([i,j])
    rj = j+1
    di = i+1
    lj = j-1
    ui = i-1
    right = garden[i,rj] if rj < W else None
    down = garden[di,j] if di < H else None
    left = garden[i,lj] if 0 <= lj < W else None
    up = garden[ui,j] if 0 <= ui < H else None
    if right == cha:
        reigonrec(i, rj, cha, reigon, visited, garden)
    if down == cha:
        reigonrec(di, j, cha, reigon, visited, garden)
    if left == cha:
        reigonrec(i, lj, cha, reigon, visited, garden)
    if up == cha:
        reigonrec(ui, j, cha, reigon, visited, garden)

def perim1(reigon, garden):
    p = 0
    cha = garden[reigon[0][0], reigon[0][1]]
    for ind in reigon:
        i = ind[0]
        j = ind[1]
        for r in range(-1, 2):
            for c in range(-1, 2):
                if not bool(r) ^ bool(c):
                    continue
                newi = i+r
                newj = j+c
                check = garden[newi, newj] if 0 <= newi < W and 0 <= newj < H else None
                if check != cha:
                    p += 1
    return p

def perim2(reigon, garden):
    s = 0
    cha = garden[reigon[0][0], reigon[0][1]]
    """Find inflexion points"""
    """
    Secanrios:
    only connected to one: two corners
    two points perpendicular: one corner
    connected sideways: one corner
    """
    for ind in reigon:
        i = ind[0]
        j = ind[1]
        rj = j+1
        di = i+1
        lj = j-1
        ui = i-1
        right = (garden[i,rj] if rj < W else None) == cha
        down = (garden[di,j] if di < H else None) == cha
        left = (garden[i,lj] if 0 <= lj < W else None) == cha
        up = (garden[ui,j] if 0 <= ui < H else None) == cha
        upright = (garden[ui,rj] if 0 <= ui < H and rj < W else None) == cha
        upleft = (garden[ui,lj] if 0 <= ui < H and 0 <= lj < W else None) == cha
        downright = (garden[di,rj] if di < H and rj < W else None) == cha
        downleft = (garden[di,lj] if di < H and 0 <= lj < W else None) == cha
        t = 0
        if ((upright^up) and (upright^right)) or not (up or right or upright):
            t += 1
        if ((downright^right) and (downright^down)) or not (right or down or downright):
            t += 1
        if ((downleft^down) and (downleft^left)) or not (down or left or downleft):
            t += 1
        if ((upleft^left) and (upleft^up)) or not (left or up or upleft):
            t += 1
        s += t
        
    return s
        
def solve(file):
    garden = [list(line.strip()) for line in file]
    garden = np.array(garden, dtype=object)
    
    print(garden)
    visited = np.array([[0 for _ in row] for row in garden])
    
    global H
    global W
    H = len(garden[:,0])
    W = len(garden[0])
    reigons = []
    for i, row in enumerate(garden):
        for j, col in enumerate(row):
            if visited[i,j]:
                continue
            reigon = []
            reigonrec(i, j, col, reigon, visited, garden)
            reigons.append(reigon)
    
    prices = []
    for block in reigons:
        area = len(block)
        perm = perim2(block, garden)
        prices.append(area*perm)
    print(sum(prices))
    
if __name__ == "__main__":
    file_path = "ADVENT/input/garden.txt"
    with open(file_path, "r") as f:
        solve(f)