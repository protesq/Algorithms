
#algorithm link: https://www.hackerrank.com/challenges/python-string-split-and-join/problem

#solution
def split_and_join(line):
    a = "-".join(line.split(" "))
    return a

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)

