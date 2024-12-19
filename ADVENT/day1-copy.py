
def solve(file):
    left = []
    right = []
    for line in file:
        line = line.strip().split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))
    
    left.sort()
    right.sort()
    
    total = 0
    for i in range(len(left)):
        total += abs(left[i]-right[i])

    print(total)
    total = 0
    
    for num in left:
        total += (num * right.count(num))
    
    print(total)
    
if __name__ == "__main__":
    file_path = "ADVENT/input/num-l.txt"
    with open(file_path, "r") as f:
            solve(f)