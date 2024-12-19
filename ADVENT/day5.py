
def solve(file):
    manual = {}
    for line in file:
        line = line.strip().split("|")
        if line[0] in manual:
            manual.get(line[0]).append(line[1])
        else:
            add = [line[1]]
            manual[line[0]] = add
    
    input_p = "ADVENT/input/safetyinput.txt"
    with open(input_p, "r") as f:
        solve2(f, manual)

def solve1(file, manual):
    total = 0
    for line in file:
        line = line.strip().split(",")
        prev = []
        valid = True
        for num in line:
            if num in manual:
                if set(prev) & set(manual[num]):
                    valid = False
                    
                    print(f"false: val {num}")
                    break
            prev.append(num)
        if valid:
            print(prev)
            total += int(prev[len(prev)//2])
    print(total)

def solve2(file, manual):
    invalid = []
    for line in file:
        line = line.strip().split(",")
        prev = []
        for num in line:
            if num in manual:
                if set(prev) & set(manual[num]):
                    invalid.append(line)
                    break
            prev.append(num)
    
    solve3(invalid, manual)

def solve3(lines, manual):
    total = 0
    for line in lines:
        total += solve_rec(line, manual)
    print(total)
        

def solve_rec(line, manual):
    prev = []
    for i, num in enumerate(line):
        if num in manual:
            p = set(prev)
            m = set(manual[num])
            intersect = p.intersection(m)
            if intersect:
                indexes = []
                new_line = line.copy()
                for swap in intersect:
                    indexes.append(new_line.index(swap))
                s = min(indexes)
                new_line[i], new_line[s] = new_line[s], new_line[i]
                return solve_rec(new_line, manual)        
        prev.append(num)
    return int(prev[len(prev)//2])

if __name__ == "__main__":
    file_path = "ADVENT/input/safetymanual.txt"
    with open(file_path, "r") as f:
        solve(f)