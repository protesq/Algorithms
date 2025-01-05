#link: https://www.hackerrank.com/challenges/string-validators/problem


#solution
def main():
    s = input()
    print(any(c.isalnum() for c in s)) #alphanumeric
    print(any(c.isalpha() for c in s)) #alphabetic
    print(any(c.isdigit() for c in s)) #digit
    print(any(c.islower() for c in s)) #lowercase
    print(any(c.isupper() for c in s)) #uppercase

if __name__ == "__main__":
    main()
