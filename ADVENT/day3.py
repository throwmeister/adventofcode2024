import re

def solve(file):
    final = []
    fline = ""
    for line in file:
        line = line.strip()
        fline += line
    
    do = fline.split("do()")
    print(f"len of do: {len(do)}")
    for l in do:
        dont = l.split("don't()")
        now_do = dont[0]
        x = re.findall("mul\([0-9]+,[0-9]+\)", now_do)
        for mul in x:
            mul = mul[4:-1]
            mul = mul.split(",")
            final.append(int(mul[0])*int(mul[1]))
    print(sum(final))


if __name__ == "__main__":
    file_path = "input/corrupt.txt"
    with open(file_path, "r") as f:
            solve(f)