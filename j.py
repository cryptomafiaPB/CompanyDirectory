from itertools import permutations

def backtrack(i, lines, cnt, words, N, M):
    global maxCnt
    if i == len(words):
        maxCnt = max(maxCnt, cnt)
        return
    if cnt + (len(words) - i) <= maxCnt:
        return
    for j in range(N):
        if lines[j] == 0:
            lines[j] = len(words[i])
            backtrack(i + 1, lines, cnt + 1, words, N, M)
            lines[j] = 0
            break
        elif lines[j] + 1 + len(words[i]) <= M:
            lines[j] += 1 + len(words[i])
            backtrack(i + 1, lines, cnt + 1, words, N, M)
            lines[j] -= 1 + len(words[i])
    backtrack(i + 1, lines, cnt, words, N, M)

# Input
K = int(input())
words = [input().strip() for _ in range(K)]
N, M = map(int, input().split())

# Filter valid words
valid = [word for word in words if len(word) <= M]

# Sort valid words by size and lexicographical order
valid.sort(key=lambda x: (-len(x), x))

# Initialize variables
lines = [0] * N
maxCnt = 0

# Start backtracking
backtrack(0, lines, 0, valid, N, M)

# Output the result
print(maxCnt)