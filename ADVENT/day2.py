class RValid:
    
    def __init__(self):
        self.range = range(1, 4)
    
    def solve(self, cnums):
        asc = True
        valid = True
        for i in range(0, len(cnums)-1):
            num1 = int(cnums[i])
            num2 = int(cnums[i+1])
            
            if i == 0:
                # Find ascending or descending
                if (num2 - num1) < 0:
                    asc = False
            if asc:
                out = num2-num1
            else:
                out = num1-num2
            
            if out not in self.range:
                return False
        return valid
            

def report_validator(file):
    total = 0
    for line in file:
        nums: list = line.strip().split(" ")
        v = RValid()
        if v.solve(nums):
            total += 1
            print(nums)
        else:
            for j in range(0, len(nums)):
                print(nums)
                new_nums = nums.copy()
                del new_nums[j]
                if v.solve(new_nums):
                    total += 1
                    print(nums)
                    break
    print(total)

if __name__ == "__main__":
    file_path = "input/reports.txt"
    with open(file_path, "r") as f:
            report_validator(f)