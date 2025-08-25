# Daily LeetCode Challenge: Diagonal Traverse

Welcome to Day 1 of this daily coding journey! Today, we tackle the **Diagonal Traverse** problem (Medium) from LeetCode, a great exercise to sharpen problem-solving skills. This guide explains the problem, solution approach, challenges faced, and how they were resolved, making it a helpful resource for anyone exploring this problem.

## Problem Description

We are given an `m x n` matrix, like `[[1,2,3],[4,5,6],[7,8,9]]`, and need to return all its elements in a diagonal (zig-zag) order, such as `[1,2,4,7,5,3,6,8,9]`. This means starting at the top-left `(0,0)`, moving up-right, then down-left, alternating directions while respecting the matrix boundaries.

## Solution Approach

The initial strategy involved grouping elements by the sum of their row and column indices (0 to `m + n - 2`). For even sums, we moved up-right (decreasing row, increasing column) and reversed the order. For odd sums, we went down-left (increasing row, decreasing column) in natural order. This aimed to collect elements diagonally, adjusting at the matrix edges.

## What Went Wrong

The first attempt produced `[1,2,4,3,5,7,6,8,9]` instead of `[1,2,4,7,5,3,6,8,9]`. The mistake was in the order of elements—down-left diagonals (e.g., `[2,4]`) were collected correctly but flipped incorrectly due to improper reversal. The direction logic didn’t align with the expected zig-zag pattern.

## How We Solved It

We shifted to a simpler method using a single pointer starting at `(0,0)`. We moved up-right until hitting a boundary (top or right), then switched to down-left, adjusting row or column accordingly. A `direction` flag toggled between moves, ensuring the correct order—e.g., `[7,5,3]` for the third diagonal. This fixed the traversal issue and matched the expected output.

## Code

See the solution in [solution.py](2025-08-25/solution.py)!

## Reflections

This experience highlighted the value of visualizing traversal patterns and testing edge cases. The final approach proved more effective than the initial complex method. This guide aims to assist others in understanding and solving this problem. Look forward to the next challenge!

## Contact

- GitHub: [ShreyaSolves](https://github.com/ShreyaSolves)
- Email: [shreyamanibu@gmail.com](mailto:shreyamanibu@gmail.com)

Happy coding, and feel free to use this as a learning resource!