# Exam Scheduling Problem

## Problem Description

This problem involves scheduling exams in a way that meets the following constraints and objectives.

### Constraints

- Each class must have a designated exam slot and an exam room.
- Each class can only be assigned to one room.
- Each room can only accommodate one exam class per slot.
- Conflicting classes cannot be scheduled in the same slot.

### Objective

Minimize the number of days (time slots) used in the exam timetable.

## Input Format

The input consists of the following:

1. **Line 1:** Two integers, `N` and `M`:
   - `N`: Number of classes.
   - `M`: Number of test rooms.

2. **Line 2:** `N` integers, `d_1, d_2, ..., d_N`, representing the number of students in each class.

3. **Line 3:** `M` integers, `c_1, c_2, ..., c_M`, representing the capacity of each room.

4. **Line 4:** An integer, `K`, representing the number of pairs of classes that conflict.

5. **Lines 5 to 4+K:** `K` pairs of integers `(i, j)`, where classes `i` and `j` cannot be scheduled in the same time slot.

### Example Input
 ```
 10 3
72 77 71 71 53 45 53 53 66 70
79 53 70
6
1 2
1 3
1 8
1 10
2 5
2 9
```

