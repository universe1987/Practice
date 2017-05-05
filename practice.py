def test(f, arr):
    global call_count
    call_count = 0
    best_v, best_split = f(arr, 5)
    print 'result is', best_v
    print 'best split is', best_split
    print 'array size is', len(arr)
    print call_count, 'function calls'


def cumsum(arr):
    result = [0] * (len(arr) + 1)
    cum = 0
    for i, a in enumerate(arr):
        cum += a
        result[i+1] = cum
    return result


def opt_split(cum, begin, k):
    global call_count
    call_count += 1
    if k == 1:
        return cum[-1] - cum[begin], []
    # find the first time that the sum of first chunk surpasses
    # the optimal splitting of the rest of the array
    left, right = begin, len(cum) - 1
    while right > left + 1:
        mid = (left + right) / 2
        s1 = cum[mid] - cum[begin]
        s2 = opt_split(cum, mid, k-1)[0]
        if s1 < s2:
            left = mid
        else:
            right = mid

    result_left = opt_split(cum, left, k-1)
    best_v = max(cum[left] - cum[begin], result_left[0])
    best_split = [left]
    best_split.extend(result_left[1])

    if right != left:
        result_right = opt_split(cum, right, k-1)
        challenge_v = max(cum[right] - cum[begin], result_right[0])
        if challenge_v < best_v:
            best_split = [right]
            best_split.extend(result_right[1])
            best_v = challenge_v

    return best_v, best_split


def solution(arr, k):
    cum = cumsum(arr)
    return opt_split(cum, 0, k)


if __name__ == '__main__':
    arr = [1] * 10000
    arr.extend([10] * 1000)
    arr.extend([100] * 100)
    arr.extend([1000] * 10)
    arr.append(9001)
    call_count = 0
    test(solution, arr)
