def solve(file):
    line = ""
    for l in file:
        l = l.strip()
        line += l
    
    """generate"""
    gen = []
    for i, num in enumerate(line):
        if (i % 2) == 0:
            f = str(i // 2)
            gen.extend([f for _ in range(int(num))])
        else:
            gen.extend(["." for _ in range(int(num))])
    s = 0
    e = len(gen)-1
    checksum = 0
    while e > s:
        start = gen[s]
        end = gen[e]
        if start != ".":
            s += 1
            continue
        if end == ".":
            e -= 1
            continue
        gen[s], gen[e] = gen[e], gen[s]
        s += 1
        e -= 1

    for i, num in enumerate(gen):
        try:
            n = int(num)
            checksum += n*i
        except ValueError:
            pass
    print(checksum)

def solve2(file):
    line = ""
    for l in file:
        l = l.strip()
        line += l
    
    """generate"""
    gen = []
    indicies = []
    for i, num in enumerate(line):
        if (i % 2) == 0:
            f = str(i // 2)
            gen.extend([f for _ in range(int(num))])
            indicies.append([int(num), len(gen)-int(num)])
        else:
            gen.extend(["." for _ in range(int(num))])
    
    dots = []
    count = 0
    for i, dot in enumerate(gen):
        if dot == ".":
            count += 1
        else:
            if count:
                dots.append([count, i-count])
            count = 0
    
    indicies.reverse()
    print("start")

    for ind in indicies:
        start = ind[1]
        length = ind[0]
        check = [[valid, j] for j, valid in enumerate(dots) if valid[1]<start and valid[0]>=length]
        if check:
            swap = check[0][0]
            start_dot = swap[1]
            end = start+length
            dec = 0
            for i in range(start, end):
                gen[i], gen[start_dot+dec] = gen[start_dot+dec], gen[i]
                dec += 1
            new_dot_len = (swap[0]-dec)
            if new_dot_len:
                dots[check[0][1]] = [new_dot_len, start_dot+dec]
            else:
                del dots[check[0][1]]
    
    checksum = 0
    for i, num in enumerate(gen):
        try:
            n = int(num)
            checksum += n*i
        except ValueError:
            pass
    print(checksum)
    


        
    
if __name__ == "__main__":
    file_path = "ADVENT/input/diskmap.txt"
    with open(file_path, "r") as f:
        solve2(f)