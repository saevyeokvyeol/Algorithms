oct = {0:'0', 1:'1', 10:'2', 11:'3', 100:'4', 101:'5', 110:'6', 111:'7'}
nums = input()[::-1]
N = [nums[i:i + 3] for i in range(0, len(nums), 3)]
binary = ""
for n in N:
    binary += oct[int(n[::-1].zfill(3))]
print(int(binary[::-1]))