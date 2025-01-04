
#algorithm link: https://www.hackerrank.com/challenges/swap-case/

#solution
def swap_case(s):
    swapped = ''
    for char in s:
        if char.islower():
            swapped += char.upper()
        else:
            swapped += char.lower()
    return swapped
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

