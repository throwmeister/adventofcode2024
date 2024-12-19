from operator import xor

class CValidator:
    def __init__(self, code):
        self.letter = code[1][0]
        self.password = code[2]
        
        lrange = code[0].split("-")
        self.lrange = range(int(lrange[0]), int(lrange[1])+1)
    
    def calculate_validity(self):
        num = self.password.count(self.letter)
        if num in self.lrange:
            return True
        return False

class C2Validator:
    def __init__(self, code):
        self.letter = code[1][0]
        self.password = code[2]
        
        lrange = code[0].split("-")
        self.lind = int(lrange[0]) - 1
        self.rind = int(lrange[1]) - 1
    
    def calculate_validity(self):
        if xor(self.letter == self.password[self.lind], self.letter == self.password[self.rind]):
            return True
        return False

def pass_validator(file):
    total = 0
    for line in file:
        c = line.split(" ")
        code = C2Validator(c)
        if code.calculate_validity():
            total += 1
    print(total)
    
def main():
    pass

if __name__ == "__main__":
    file_path = "passwords.txt"
    with open(file_path, "r") as f:
            pass_validator(f)