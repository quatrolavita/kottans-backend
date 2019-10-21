# Find the Runner-Up Score!
# link for this task: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem?h_r=profile


def my_max(array):
    start_max = array[0]
    for _ in array:
        if i > start_max:
            start_max = i
    return start_max


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    max_v = my_max(arr)

    for i in range(arr.count(max_v)):
        arr.remove(max_v)

    print(my_max(arr))
