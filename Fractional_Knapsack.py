'''
🟩 Fractional Knapsack

1. Proper exam-style question

Question:

You are given N items. Each item has a weight and a value. You have a bag with capacity W.
You can take all or part of an item.

Find the maximum value that can be placed in the bag.

Input
3 50
10 60
20 100
30 120

Meaning:

3 → number of items
50 → bag capacity

Items:

Weight    Value
10        60
20        100
30        120

Output
240.0

2. How do you recognize it?

Look for:

weight
value
capacity
maximum value
+
fraction / part of item is allowed

Then:

Fractional Knapsack
        ↓
Greedy
        ↓
value / weight

'''

import sys

def solve():

    data=sys.stdin.read().split()

    if not data:
        return

    n=int(data[0])
    capacity=int(data[1])

    items=[]
    index=2

    for i in range(n):
        weight=int(data[index])
        value=int(data[index+1])

        ratio=value/weight

        items.append([ratio , weight , value])

        index+=2

    items.sort(reverse=True)

    total_value=0

    for i in range(n):
        ratio=items[i][0]
        weight=items[i][1]
        value=items[i][2]

        if capacity >=weight:
            capacity -= weight
            total_value += value
            
        else:
            total_value += ratio * capacity
            capacity=0
            break

    print(total_value)

if __name__=="__main__":
    solve()
