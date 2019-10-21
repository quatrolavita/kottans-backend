# Finding the percentage
# link for this task: https://www.hackerrank.com/challenges/finding-the-percentage/problem?h_r=profile


if __name__ == '__main__':
    n = int(input())
    student_marks = {}

    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores

    query_name = input()
    result = 0

    for i in student_marks.get(query_name):
        result = result + i

    result = result/3
    print('%.2f'%result)
