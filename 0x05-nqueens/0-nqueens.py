#!/usr/bin/python3
import sys

def is_safe(board, row, col, N):
    for i in range(col):
        if board[row][i] == 1:
            return False
    
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    for i, j in zip(range(row, N), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    
    return True

def solve_n_queens_util(board, col, N, result):
    if col == N:
        queens_positions = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    queens_positions.append([i, j])
        result.append(queens_positions)
        return True
    
    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens_util(board, col + 1, N, result) or res
            board[i][col] = 0
    
    return res

def print_solution(result):
    for sol in result:
        print(sol)

def solve_n_queens(N):
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    
    board = [[0 for _ in range(N)] for _ in range(N)]
    result = []
    solve_n_queens_util(board, 0, N, result)
    
    if not result:
        print("[]")
    else:
        for sol in result:
            print(sol)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    
    try:
        N = int(sys.argv[1])
        solve_n_queens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
