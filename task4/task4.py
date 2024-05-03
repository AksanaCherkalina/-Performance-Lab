import sys

def read_file(file_path):
    with open(file_path, 'r') as file:
        return [int(line.strip()) for line in file]

def min_moves(nums):
    nums.sort()
    median = nums[len(nums) // 2]
    return sum(abs(num - median) for num in nums)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: python task4.py path_to_your_file.txt")
        sys.exit(1)
    file_path = sys.argv[1]
    nums = read_file(file_path)
    print(min_moves(nums))
