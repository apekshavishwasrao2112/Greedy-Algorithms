'''
🟩 1. Proper Infosys-style Question

Question:

You are given N activities. Each activity has a start time and an end time.

You can perform only one activity at a time. Two activities cannot overlap.

Find the maximum number of activities that can be performed.

One possible selection is:

(1,2)
   ↓
(3,4)
   ↓
(5,7)
   ↓
(8,9)

So the answer is 4 activities.

🟩 2. How do you recognize this in the exam?

Look for these words:

activities
start time
finish/end time
maximum number
non-overlapping
cannot perform two at the same time
meetings
events
jobs
intervals

Especially:

START + END
        +
MAXIMUM NUMBER OF NON-OVERLAPPING
        ↓
ACTIVITY SELECTION
        ↓
GREEDY
🟩 3. The main idea

Suppose you have:

Activity     Start     End

A              1        4
B              2        3
C              3        5
D              5        7

Which one should we choose first?

We choose:

B → 2 to 3

Why?

Because B finishes earliest.

After B finishes at 3, we have more opportunities to select other activities.

So our rule is:

Always choose the activity that finishes earliest.

That's the Greedy choice.

🟩 4. Very important: Sort by END time

Input:

1 4
2 3
3 5
5 7

The activities are not sorted by ending time.

Sort them:

2 3
1 4
3 5
5 7

Now ending times are:

3
4
5
7

Then select activities one by one.

Test case-

Input

6
1 2
3 4
0 6
5 7
8 9
5 9

Output

4
'''

import sys

def solve():

    data=sys.stdin.read().split()

    if not data:
        return

    n=int(data[0])

    activites=[]
    index=1

    for i in range(n):
        start=int(data[index])
        end=int(data[index+1])

        activites.append([start , end])

        index+=2

    activites.sort(key=lambda x:x[1])

    count=1
    last_end=activites[0][1]

    for i in range(1 , n):
        start=activites[i][0]
        end=activites[i][1]

        if start >=last_end:
            count+=1
            last_end=end

    print(count)

if __name__=="__main__":
    solve()