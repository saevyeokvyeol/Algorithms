import sys

def binary_search(array, target, start, end):
    if start > end:
        return False
    mid = (start + end) // 2
    if array[mid] == target:
        return True
    elif array[mid] < target:
        return binary_search(array, target, mid + 1, end)
    else:
        return binary_search(array, target, start, mid - 1)

n = int(sys.stdin.readline())
n_array = sorted(list(map(int, sys.stdin.readline().split())))
m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

for i in m_array:
    print("yes" if binary_search(n_array, i, 0, n - 1) else "no", end=" ")