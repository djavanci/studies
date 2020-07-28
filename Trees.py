def solution(X, Y):
    X.sort()
    max_ = 0
    for i in range(1, len(X)):
        if X[i] - X[i - 1] > max_:
            max_ = X[i] - X[i - 1]

    return max_


print(solution([1, 8, 7, 3, 4, 1, 8], [6, 4, 1, 8, 5, 1, 7]))
print(solution([5, 5, 5, 7, 7, 7], [3, 4, 5, 1, 3, 7]))
print(solution([6, 10, 1, 4, 3], [2, 5, 3, 1, 6]))
print(solution([4, 1, 5, 4], [4, 5, 1, 3]))
print(solution([4, 5], [4, 5]))
