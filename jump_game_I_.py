'''
🟢 Jump Game I — Can Reach the End?
Question

You are given an array of N integers. The value A[i] represents the maximum number of positions you can jump forward from index i.

Starting from index 0, determine whether you can reach the last index.

Input
5
2 3 1 1 4

Output
YES

Another test case
5
3 2 1 0 4

Output
NO

Recognize it

"Can reach the last index?" → Jump Game I → Greedy → farthest
'''

import sys

def solve():

    data=sys.stdin.read().split()

    n=int(data[0])

    arr=[]

    for i in range(1,n+1):
        arr.append(int(data[i]))

    if n<=1:
        print("Yes")
        return

    farthest=0

    for i in range(n):

        if i>farthest:
            print("No")
            return

        reach=i+arr[i]

        if reach > farthest:
            farthest =reach

        if farthest >=n-1:
            print("Yes")
            return
        
    print("No")

if __name__=="__main__":
    solve()
