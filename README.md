# Greedy Algorithms

This repository contains my practice problems based on **Greedy Algorithms** using Python.

The problems in this folder focus on making the **best possible choice at each step** to reach the required result efficiently.

---

## 🧠 What I am Practicing

Through these problems, I am practicing:

* Understanding the Greedy approach
* Identifying Greedy patterns from problem statements
* Making the best local choice at each step
* Sorting-based Greedy problems
* Interval and scheduling problems
* Maximum and minimum optimization problems
* Tracking the farthest reachable position
* Managing overlapping events
* Using sorting and two-pointer techniques

---

## 📚 Problems

| # | Problem             | Greedy Pattern                 |
| - | ------------------- | ------------------------------ |
| 1 | Activity Selection  | Earliest Finish Time           |
| 2 | Fractional Knapsack | Maximum Value / Weight         |
| 3 | Job Sequencing      | Maximum Profit + Deadline      |
| 4 | Jump Game I         | Farthest Reach                 |
| 5 | Jump Game II        | Farthest Reach + Minimum Jumps |
| 6 | Minimum Platforms   | Maximum Overlap                |

---

## 1. Activity Selection

### Problem

You are given `N` activities. Each activity has a start time and an end time.

Only one activity can be performed at a time, so two activities cannot overlap.

Find the **maximum number of activities** that can be performed.

### Greedy Pattern

```text
START + END
     +
MAXIMUM NUMBER OF NON-OVERLAPPING
     ↓
ACTIVITY SELECTION
     ↓
GREEDY
```

### Key Idea

Always select the activity that **finishes earliest**.

The activities are sorted by their end time, and then selected one by one if their start time is greater than or equal to the end time of the previously selected activity.

---

## 2. Fractional Knapsack

### Problem

You are given `N` items. Each item has a weight and a value.

You have a bag with capacity `W`.

Unlike 0/1 Knapsack, you are allowed to take **all or part of an item**.

Find the maximum value that can be placed in the bag.

### Greedy Pattern

```text
WEIGHT + VALUE + CAPACITY
          +
FRACTION ALLOWED
          ↓
FRACTIONAL KNAPSACK
          ↓
GREEDY
          ↓
VALUE / WEIGHT
```

### Key Idea

Calculate the **value-to-weight ratio** for every item.

Then process the items in decreasing order of this ratio. If the entire item cannot fit, take the fraction that fits.

---

## 3. Job Sequencing

### Problem

You are given `N` jobs.

Each job has:

* Job ID
* Deadline
* Profit

Each job takes exactly one unit of time.

A job earns its profit only when it is completed before or on its deadline.

Find the **maximum total profit**.

### Greedy Pattern

```text
JOB
 +
DEADLINE
 +
PROFIT
 +
MAXIMUM PROFIT
      ↓
JOB SEQUENCING
      ↓
GREEDY
```

### Key Idea

The jobs are considered based on their profit, and each job is placed into the latest available slot before its deadline.

The goal is to maximize the total profit.

---

## 4. Jump Game I

### Problem

You are given an array where `A[i]` represents the maximum number of positions you can jump forward from index `i`.

Starting from index `0`, determine whether you can reach the last index.

### Greedy Pattern

```text
CAN REACH LAST INDEX?
        ↓
   JUMP GAME I
        ↓
      GREEDY
        ↓
  FARTHEST REACH
```

### Key Idea

Keep track of the **farthest position that can currently be reached**.

If the current index goes beyond the farthest reachable position, the destination cannot be reached.

---

## 5. Jump Game II

### Problem

You are given an array where `A[i]` represents the maximum number of positions you can jump forward from index `i`.

Starting from index `0`, find the **minimum number of jumps** required to reach the last index.

### Greedy Pattern

```text
MINIMUM NUMBER OF JUMPS
          ↓
     JUMP GAME II
          ↓
        GREEDY
          ↓
FARTHEST + CURRENT END + JUMPS
```

### Key Idea

Track the farthest position that can be reached within the current jump range.

When the current position reaches the end of that range, increase the jump count and extend the range to the farthest reachable position.

---

## 6. Minimum Platforms

### Problem

You are given the arrival and departure times of `N` trains.

Find the **minimum number of platforms required** so that no train has to wait.

### Greedy Pattern

This problem is based on identifying the maximum number of events happening at the same time.

```text
START + END
     ↓
SORT BOTH
     ↓
TWO POINTERS
     ↓
MAXIMUM OVERLAP
```

For trains:

```text
Arrival   → START
Departure → END
```

The maximum number of simultaneously active trains determines the required number of platforms.

---

# 🔎 Greedy Pattern Recognition

These problems can be recognized using a few important clues.

### Activity Selection

```text
START + END
+
MAXIMUM NON-OVERLAPPING ACTIVITIES
        ↓
EARLIEST FINISH TIME
```

### Fractional Knapsack

```text
VALUE + WEIGHT + CAPACITY
+
FRACTION ALLOWED
        ↓
VALUE / WEIGHT
```

### Job Sequencing

```text
JOB + DEADLINE + PROFIT
+
MAXIMUM PROFIT
        ↓
GREEDY
```

### Jump Game

```text
CAN REACH?
OR
MINIMUM JUMPS
        ↓
FARTHEST REACH
```

### Minimum Platforms

```text
ARRIVAL + DEPARTURE
        ↓
OVERLAPPING EVENTS
        ↓
TWO POINTERS
```

---

# 🎯 Key Learning

The main idea I am practicing in this folder is:

> **Make the best possible choice at the current step and use that choice to build the final solution.**

The important part is not just knowing the Greedy technique, but learning to **recognize when a problem can be solved using a Greedy strategy**.

---

# 💻 Language

**Python**

The solutions use Python and `sys.stdin` for coding-exam-style input handling.

---

## 🚀 Goal

Continue practicing different **Greedy Algorithm patterns** and improve my ability to identify the correct greedy choice from a problem statement before implementing the solution.
