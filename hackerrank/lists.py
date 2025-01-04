
#algorithm link: https://www.hackerrank.com/challenges/python-lists

#solution
def main():
    my_list = []

    n = int(input())

    for _ in range(n):
        command = input().strip().split()

        cmd = command[0]
        
        if cmd == "append":
            my_list.append(int(command[1]))
        elif cmd == "insert":
            my_list.insert(int(command[1]), int(command[2]))
        elif cmd == "remove":
            my_list.remove(int(command[1]))
        elif cmd == "pop":
            if len(command) == 1:
                my_list.pop()
            else:
                my_list.pop(int(command[1]))
        elif cmd == "print":
            print(my_list)
        elif cmd == "sort":
            my_list.sort()
        elif cmd == "reverse":
            my_list.reverse()

if __name__ == "__main__":
    main()
