# Nested Lists
# link for this task: https://www.hackerrank.com/challenges/nested-list/problem?h_r=profile


if __name__ == '__main__':
    classroom = []

    for _ in range(int(input())):
        name = input()
        score = float(input())
        a = [name, score]
        classroom.append(list(a))

    min_mark = classroom[0][1]

    for i in classroom:
        if i[1] < min_mark:
            min_mark = i[1]

    for i in classroom:
        if i[1] == min_mark:
            classroom.remove(i)

    min_mark = classroom[0][1]

    for i in classroom:
        if i[1] < min_mark:
            min_mark = i[1]

    classroom.sort()

    for i in classroom:
        if i[1] == min_mark:
            print(i[0])
