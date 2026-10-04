'''
🟢 Job Sequencing — Assessment Format
Typical question

You are given N jobs. Each job has a job ID, deadline, and profit. Each job takes exactly one unit of time. A job earns its profit only if it is completed before or on its deadline.

Find the maximum total profit that can be obtained.

How to recognize it

Look for these 3 things:

Job + Deadline + Profit
        ↓
Each job takes 1 unit time
        ↓
Maximum profit
        ↓
GREEDY
Input

A common format is:

Input
4
A 2 100
B 1 50
C 2 20
D 1 30

Output:
150

Meaning:

N = 4 jobs

Job   Deadline   Profit
A        2         100
B        1          50
C        2          20
D        1          30
Important

The first number:

4

means 4 jobs, not 4 slots.

The maximum deadline is 2, so we have:

Slot 1    Slot 2
Output

We want the maximum total profit.

Choose:

Slot 1 → B → 50
Slot 2 → A → 100

Total:

50 + 100 = 150

So:

Output:
150
⭐ How to recognize in an Infosys question

If you see wording like:

"N jobs"
"deadline"
"profit"
"each job takes one unit of time"
"maximize profit"
"schedule jobs"

Immediately think:

Job Sequencing with Deadlines → Greedy
'''

import sys

def solve():

    data=sys.stdin.read().split()

    if not data:
        return
    n=int(data[0])

    jobs=[]
    index=1

    for i in range(n):
        job=data[index]
        deadline=int(data[index+1])
        profit=int(data[index+2])

        jobs.append((profit , deadline , job))
        index+=3

    jobs.sort(reverse=True)

    max_deadline=0

    for profit , deadline , job in jobs:

        if deadline >= max_deadline:
            max_deadline=deadline


    slots=[-1]*(max_deadline + 1)

    total_profit=0
    for profit , deadline , job in jobs:

        for slot in range(deadline , 0 , -1):

            if slots[slot]==-1:
                slots[slot]=job
                total_profit += profit
                break

    print(total_profit)

if __name__=="__main__":
    solve()
           
