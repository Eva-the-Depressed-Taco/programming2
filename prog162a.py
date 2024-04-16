import sys
sys.setrecursionlimit(10**6)
def MRvaribe(n):
    return 0 if n <= 0 else n*3 + MRvaribe(n-1)
print("dude like, the sum of the series is like totally:", MRvaribe(3222))