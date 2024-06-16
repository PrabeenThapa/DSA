
def minOperation(n, arr):
    count = 0
    i = 0
    while i < n - 1:
        if arr[i] % 2 == arr[i + 1] % 2:
            arr[i] *= arr[i + 1]
            arr.pop(i + 1)
            n -= 1
            count += 1
            if i > 0:
                i -= 1
        else:
            i += 1
    return count

t = int(input())
n = input()
arr = n.split()
arr = [int(a) for a in arr]
print(minOperation(t, arr))
