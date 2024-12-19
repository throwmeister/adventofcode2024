import numpy as np
from dataclasses import dataclass
from enum import Enum

class Clock(Enum):
    fwd = 1
    rt = 2
    dwn = 3
    lft = 4

@dataclass
class Pos:
    x: int
    y: int
    clock: Clock

    def __init__(self, x, y, clock=Clock.fwd):
        self.x = x
        self.y = y
        self.clock = clock
    
    def increments(self):
        match self.clock:
            case Clock.fwd:
                return Pos(self.x-1, self.y, self.clock)
            case Clock.rt:
                return Pos(self.x, self.y+1, self.clock)
            case Clock.dwn:
                return Pos(self.x+1, self.y, self.clock)
            case Clock.lft:
                return Pos(self.x, self.y-1, self.clock)
    
    def turn(self):
        match self.clock:
            case Clock.fwd:
                self.clock = Clock.rt
            case Clock.rt:
                self.clock = Clock.dwn
            case Clock.dwn:
                self.clock = Clock.lft
            case Clock.lft:
                self.clock = Clock.fwd
    
    def dupe(self):
        return Pos(self.x, self.y, self.clock)

def traverse(pos, pathmap):
    while True:
        npos = pos.increments()
        try:
            next = pathmap[npos.x,npos.y]
        except IndexError:
            pathmap[pos.x,pos.y] = "X"
            break
        if next == "#":
            pos.turn()
        else:
            pathmap[pos.x,pos.y] = "X"
            pos = npos
    
    t = 0
    for row in pathmap:
        for col in row:
            if col == 'X':
                t += 1
    
    print(t)

def traverse2(pos, pathmap):
    directions = {}
    while True:
        npos = pos.increments()
        try:
            next = pathmap[npos.x,npos.y]
            if npos.x < 0 or npos.y < 0:
                return 0
        except IndexError:
            return 0
        if next == "#":
            pos.turn()
        else:
            dstring = f"{pos.x}__{pos.y}"
            direction = directions.setdefault(dstring, [])
            if pos.clock in direction:
                return 1
            direction.append(pos.clock)
            
            pos = npos
            


def solve2(pos, pathmap):
    total = 0
    for i, row in enumerate(pathmap):
        for j, col in enumerate(row):
            if col == ".":
                pathmap[i,j] = "#"
                p = pos.dupe()
                total += traverse2(p, pathmap)
                pathmap[i,j] = "."
    
    print(total)
    
def solve(file):
    pathmap = [list(line.strip()) for line in file]
    pathmap = np.array(pathmap, dtype=object)
    
    print(pathmap)
    pos = [0,0]
    for i, row in enumerate(pathmap):
        for j, col in enumerate(row):
            if col == '^':
                pos = Pos(i, j)

    solve2(pos, pathmap)
    
    
if __name__ == "__main__":
    file_path = "ADVENT/input/guard.txt"
    with open(file_path, "r") as f:
        solve(f)