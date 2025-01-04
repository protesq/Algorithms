

#algorithm link: https://www.hackerrank.com/challenges/nested-list/problem

#solution
nested_list = []

for i in range(int(input())):
    name = input()
    score = float(input())
    nested_list.append([name, score])

sorted_scores = sorted(set([score for name, score in nested_list]))

second_lowest = sorted_scores[1]

second_lowest_students = sorted([name for name, score in nested_list if score == second_lowest])

for student in second_lowest_students:
    print(student)