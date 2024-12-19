import itertools

def opCalc(op, n1, n2):
    res = 0
    if op == "+":
        return n1+n2
    elif op == "|":
        return int(str(n1)+str(n2))
    return n1*n2

def solve(file):
    _ops = ["+", "*", "|"]
    total = 0
    for line in file:
        line = line.strip().split(": ")
        t = int(line[0])
        nums = list(map(int, line[1].split(" ")))
        opCombos = set(itertools.product(_ops, repeat=len(nums)-1))
        for ops in opCombos:
            calc = nums[0]
            for i in range(1, len(nums)):
                calc = opCalc(ops[i-1], calc, nums[i])
            
            if calc == t:
                total += t
                print(f"found: {t} opcombo: {ops}")
                break
    
    print(total)
    
if __name__ == "__main__":
    file_path = "ADVENT/input/bridge.txt"
    with open(file_path, "r") as f:
        solve(f)