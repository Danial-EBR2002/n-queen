def solve_n_queens(n):
    solution = []
    cols = set()
    pos_diags = set()  # (r + c)
    neg_diags = set()  # (r - c)
    queens = [-1] * n
    found = [False]

    def backtrack(r):
        if found[0]:
            return
        if r == n:
            solution.extend(queens[:])
            found[0] = True
            return
        for c in range(n):
            if c in cols or (r + c) in pos_diags or (r - c) in neg_diags:
                continue
            queens[r] = c
            cols.add(c)
            pos_diags.add(r + c)
            neg_diags.add(r - c)

            backtrack(r + 1)

            cols.remove(c)
            pos_diags.remove(r + c)
            neg_diags.remove(r - c)
            queens[r] = -1

    backtrack(0)
    return solution if solution else None


if __name__ == "__main__":
    n = 8
    sol = solve_n_queens(n)
    print(sol)
