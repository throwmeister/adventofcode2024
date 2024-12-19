import numpy as np
def calc_difference(i1, i2):
    """format = [i, j]"""
    x = i1[0] - i2[0]
    y = i1[1] - i2[1]
    return [x, y]
    
def solve(file):
    pathmap = [list(line.strip()) for line in file]
    pathmap = np.array(pathmap, dtype=object)
    
    hei = len(pathmap[:,0])
    wid = len(pathmap[0])
    print(pathmap)
    
    towers = {}
    for i, row in enumerate(pathmap):
        for j, item in enumerate(row):
            if item != '.':
                towers.setdefault(item, []).append([i, j])
    
    final = []
    for vals in towers.values():
        for i, pos in enumerate(vals):
            for j in range(0, len(vals)):
                if i == j:
                    final.append((pos[0], pos[1]))
                    continue
                diff = calc_difference(pos, vals[j])
                mult = 1
                while True:
                    t1 = pos[0] + (diff[0]*mult)
                    t2 = pos[1] + (diff[1]*mult)
                    if 0 <= t1 < hei and 0 <= t2 < wid:
                        final.append((t1, t2))
                        mult += 1
                    else:
                        break
    print(len(set(final)))
    print(set(final))
        
if __name__ == "__main__":
    file_path = "ADVENT/input/roof.txt"
    with open(file_path, "r") as f:
        solve(f)