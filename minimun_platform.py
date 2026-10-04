'''
🔴 Greedy Pattern: Minimum Platforms

1. Question
You are given the arrival and departure times of N trains.
Find the minimum number of platforms required so that no train has to wait.

Input
6
900 910
940 1200
950 1120
1100 1130
1500 1900
1800 2000

Here:

6 → number of trains
Each next line → arrival departure

Output
3

2. How to recognize the pattern

Don't focus on the railway story.

The important thing is:

We have two types of events: START and END, and we need the maximum number happening at the same time.

For trains:

Arrival = START
Departure = END

So think:

START + END
        ↓
sort both
        ↓
two pointers
        ↓
maximum overlap

This pattern can appear with meetings, machines, servers, bookings, events, etc.

3. Main idea

Separate arrivals and departures.

For our input:

Arrival:
900 940 950 1100 1500 1800

Departure:
910 1200 1120 1130 1900 2000

Sort both:

Arrival:
900 940 950 1100 1500 1800

Departure:
910 1120 1130 1200 1900 2000

Now compare the smallest arrival and departure.

At 900

Train arrives.

platforms = 1
At 910

A train departs.

platforms = 0
At 940

Train arrives.

platforms = 1
At 950

Another train arrives.

platforms = 2
At 1100

Another train arrives.

platforms = 3

Now maximum is:

3

So answer = 3 platforms.
'''

import sys

def solve():

    data=sys.stdin.read().split()

    if not data:
        return

    n=int(data[0])

    arrival=[]
    depature=[]

    index=1
    for i in range(n):
        arrival.append(int(data[index]))
        depature.append(int(data[index+1]))
        index+=2

    arrival.sort()
    depature.sort()

    i=0
    j=0

    platform=0
    maxi=0

    while i < n and j < n:

        if arrival[i] <depature[j]:
            platform+=1

            if platform > maxi:
                maxi=platform

            i+=1
        else:
            platform-=1
            j+=1

    print(maxi)

if __name__=="__main__":
    solve()


