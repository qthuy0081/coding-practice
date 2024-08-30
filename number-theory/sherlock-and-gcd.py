from math import gcd
def sherlockAndGcd(arr):
    res = arr[0]
    for i in range(1, len(arr)):
        res = gcd(res, arr[i])
        if res == 1:
            return "YES"
    return "NO"

print(sherlockAndGcd([2, 3, 9]))
print(sherlockAndGcd([2, 4, 4]))