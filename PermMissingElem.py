# An array A consisting of N different integers is given. The array
# contains integers in the range [1..(N + 1)], which means that
# exactly one element is missing.
#
# Your goal is to find that missing element.
#
# Write a function:
#
# def solution(A)
#
# that, given an array A, returns the value of the missing element.
#
# For example, given array A such that:
#
#   A[0] = 2
#   A[1] = 3
#   A[2] = 1
#   A[3] = 5
# the function should return 4, as it is the missing element.
#
# Write an efficient algorithm for the following assumptions:
#
# N is an integer within the range [0..100,000];
# the elements of A are all distinct;
# each element of array A is an integer within the range [1..(N + 1)].
# Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


def solution(A: int):
    if not A:
        return 1

    A.sort()
    for i, n in enumerate(A):
        if n != i + 1:
            return i + 1

    return i + 2


print(solution([2, 3, 1, 5]))  # prints 4
print(solution([1]))  # N is 1, prints 2
print(solution([]))  # N is 0, prints 1
print(solution([2]))  # N is 1, prints 1
print(solution([2, 3, 4]))  # N is 3, prints 1
print(solution([1, 2, 3]))  # N is 3, prints 4
print(solution([2, 4, 3, 6, 7, 8, 5, 1, 11, 9]))  # N is 10, prints 10
