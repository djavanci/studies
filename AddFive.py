def solution(N):
    # write your code in Python 3.6
    if not -8000 <= N <= 8000:
        raise ValueError("Value should be between -8000 and 8000")

    number_as_string = list(str(N))
    for i, number in enumerate(number_as_string):
        if (N >= 0 and number <= '5') or (N < 0 and number >= '5'):
            number_as_string.insert(i, '5')
            break
    else:
        number_as_string.insert(i + 1, '5')

    print(int(''.join(number_as_string)))


solution(268)
solution(670)
solution(0)
solution(-999)
solution(-444)
solution(10000)
