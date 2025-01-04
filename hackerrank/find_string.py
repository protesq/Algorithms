
#algorithm link: https://www.hackerrank.com/challenges/find-a-string

#solution
def count_substring(string, sub_string):

    count = 0
    index = 0

    while index < len(string):
        index = string.find(sub_string, index)
        

        if index != -1:
            count += 1
            index += 1 
        else:
            break

    return count
