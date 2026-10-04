'''
🟢 Jump Game II — Minimum Jumps
Question

You are given an array of N integers. The value A[i] represents the maximum number of positions you can jump forward from index i.

Starting from index 0, find the minimum number of jumps required to reach the last index.

Input
5
2 3 1 1 4
Output
2

Because:

0 → 1 → 4

Another test case
5
3 0 1 1 0
Output
2

Because:

0 → 3 → 4
Recognize it

"Minimum number of jumps?" → Jump Game II → Greedy → farthest + current_end + jumps
'''

import sys

def solve():
    data=sys.stdin.read().split()

    n=int(data[0])

    arr=[]

    for i in range(1 , n+1):
        arr.append(int(data[i]))

    jump=0
    curr_end=0
    far=0

    for i in range(n-1):
        reach=i+arr[i]

        if reach > far:
            far = reach

        if i==curr_end:
            jump += 1
            curr_end = far

            if curr_end >=n-1:
                break

    print(jump)

if __name__=="__main__":
    solve()

